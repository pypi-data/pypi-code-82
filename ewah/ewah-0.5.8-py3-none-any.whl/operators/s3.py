from ewah.operators.base import EWAHBaseOperator
from ewah.constants import EWAHConstants as EC

from airflow.providers.amazon.aws.hooks.s3 import S3Hook

from datetime import datetime, timedelta

import json
import csv
import gzip

class ExtendedS3Hook(S3Hook):
    """Extends and improves the provider package's S3Hook's capability"""

    credentials_by_region = {}

    def _get_credentials(self, region_name):
        "Avoid creation of a new session each time an S3 file is downloaded."
        if not region_name in self.credentials_by_region:
            self.credentials_by_region[region_name] = super()._get_credentials(region_name=region_name)
        return self.credentials_by_region[region_name]

class EWAHS3Operator(EWAHBaseOperator):
    """Only implemented for JSON and CSV files from S3 right now!"""

    _NAMES = ["s3"]

    _ACCEPTED_EXTRACT_STRATEGIES = {
        EC.ES_FULL_REFRESH: True,
        EC.ES_INCREMENTAL: True,
    }

    _IMPLEMENTED_FORMATS = [
        "JSON",
        "AWS_FIREHOSE_JSON",
        "CSV",
    ]

    _BOM = b"\xef\xbb\xbf"

    def __init__(
        self,
        bucket_name,
        file_format,
        prefix="",  # use for subfolder structures
        suffix=None,  # use e.g. for file types
        key_name=None,  # if not specified, uses data_from and data_until
        csv_format_options={},
        csv_encoding="utf-8",
        decompress=False,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        if not file_format in self._IMPLEMENTED_FORMATS:
            raise Exception(
                "File format not implemented! Available formats:"
                + " {0}".format(str(self._IMPLEMENTED_FORMATS))
            )

        if key_name:
            if self.load_data_from or self.load_data_until:
                raise Exception(
                    "Both key_name and either data_from or data_"
                    + "until specified! Cannot have both specified."
                )

        if not file_format == "CSV" and csv_format_options:
            raise Exception("csv_format_options is only valid for CSV files!")

        if decompress and not file_format == "CSV":
            raise exception("Can currently only decompress CSVs!")

        self.bucket_name = bucket_name
        self.prefix = prefix
        self.suffix = suffix
        self.key_name = key_name
        self.file_format = file_format
        self.csv_format_options = csv_format_options
        self.csv_encoding = csv_encoding
        self.decompress = decompress

    def _iterate_through_bucket(
        self, s3hook, bucket, prefix, modified_from=None, modified_until=None
    ):
        """The bucket.objects.filter() method only returns a max of 1000
        objects. If more objects are in an S3 bucket, pagniation is
        required. See also: https://stackoverflow.com/questions/44238525/how-to-iterate-over-files-in-an-s3-bucket
        """
        cli = s3hook.get_client_type("s3")
        paginator = cli.get_paginator("list_objects_v2")
        page_iterator = paginator.paginate(Bucket=bucket, Prefix=prefix)

        all_objects = [
            o
            for o in page_iterator.build_full_result()["Contents"]
            if (not modified_from or o["LastModified"] >= modified_from)
            and (not modified_until or o["LastModified"] < modified_until)
        ]

        self.log.info("Iterating through {0} objects..".format(len(all_objects)))

        for item in all_objects:
            yield item

    def ewah_execute(self, context):
        if self.file_format == "JSON":
            return self.execute_json(
                context=context,
                f_get_data=lambda hook, key, bucket: json.loads(
                    hook.read_key(key, bucket)
                ),
            )
        elif self.file_format == "AWS_FIREHOSE_JSON":
            return self.execute_json(
                context=context,
                f_get_data=lambda hook, key, bucket: json.loads(
                    "[" + hook.read_key(key, bucket).replace("}{", "},{") + "]"
                ),
            )
        elif self.file_format == "CSV":
            return self.execute_csv(
                context=context,
            )
        else:
            raise Exception("File format not implemented!")

    def execute_csv(self, context):
        def chunk_upload(csv_reader):
            i = 0
            data = []
            for row in csv_reader:
                i += 1
                data.append(row)
                if i >= 100000:
                    self.upload_data(data=data)
                    data = []
                    i = 0
            if data:
                self.upload_data(data=data)

        hook = ExtendedS3Hook(self.source_conn.conn_id)
        suffix = self.suffix
        if self.key_name:
            obj = hook.get_key(self.key_name, self.bucket_name)
            raw_data = obj.get()["Body"].read()
            if self.decompress:
                raw_data = gzip.decompress(raw_data)
            if raw_data[:3] == self._BOM:
                raw_data = raw_data[3:]
                csv_encoding = "utf-8"
            else:
                csv_encoding = self.csv_encoding
            try:
                raw_data = raw_data.decode(csv_encoding).splitlines()
            except UnicodeDecodeError:
                if csv_encoding == self.csv_encoding:
                    raise
                raw_data = raw_data.decode(self.csv_encoding).splitlines()
            reader = csv.DictReader(raw_data, **self.csv_format_options)
            chunk_upload(reader)

        else:
            objects = self._iterate_through_bucket(
                s3hook=hook,
                bucket=self.bucket_name,
                prefix=self.prefix,
                modified_from=self.data_from,
                modified_until=self.data_until,
            )
            for obj_iter in objects:
                # skip all files outside of loading scope
                if suffix and not suffix == obj_iter["Key"][-len(suffix) :]:
                    continue

                self.log.info("Loading data from file {0}".format(obj_iter["Key"]))
                raw_data = (
                    hook.get_key(obj_iter["Key"], self.bucket_name).get()["Body"].read()
                )
                if self.decompress:
                    raw_data = gzip.decompress(raw_data)
                # remove BOM if it exists
                # also, if file has a BOM, it is 99.9% utf-8 encoded!
                if raw_data[:3] == self._BOM:
                    raw_data = raw_data[3:]
                    csv_encoding = "utf-8"
                else:
                    csv_encoding = self.csv_encoding
                # there may be a BOM while still not utf-8 -> use the
                # given csv_encoding argument if so
                try:
                    raw_data = raw_data.decode(csv_encoding).splitlines()
                except UnicodeDecodeError:
                    if csv_encoding == self.csv_encoding:
                        raise
                    raw_data = raw_data.decode(self.csv_encoding).splitlines()
                reader = csv.DictReader(raw_data, **self.csv_format_options)
                self._metadata.update(
                    {
                        "bucket_name": self.bucket_name,
                        "file_name": obj_iter["Key"],
                        "file_last_modified": str(obj_iter["LastModified"]),
                    }
                )
                chunk_upload(reader)

    def execute_json(self, context, f_get_data):
        hook = ExtendedS3Hook(self.source_conn.conn_id)
        suffix = self.suffix

        if self.key_name:
            data = f_get_data(
                hook=hook,
                key=self.key_name,
                bucket=self.bucket_name,
            )
            self.upload_data(data=data)
        else:
            data = []
            objects = self._iterate_through_bucket(
                s3hook=hook,
                bucket=self.bucket_name,
                prefix=self.prefix,
                modified_from=self.data_from,
                modified_until=self.data_until,
            )
            for obj_iter in objects:
                if suffix and not suffix == obj_iter["Key"][-len(suffix) :]:
                    continue

                self.log.info(
                    "Loading data from file {0}".format(
                        obj_iter["Key"],
                    )
                )
                self._metadata.update(
                    {
                        "bucket_name": self.bucket_name,
                        "file_name": obj_iter["Key"],
                        "file_last_modified": str(obj_iter["LastModified"]),
                    }
                )
                data = f_get_data(
                    hook=hook,
                    key=obj_iter["Key"],
                    bucket=self.bucket_name,
                )
                self.upload_data(data=data)
