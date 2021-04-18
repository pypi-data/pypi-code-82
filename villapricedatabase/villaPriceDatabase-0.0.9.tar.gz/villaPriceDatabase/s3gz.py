# AUTOGENERATED! DO NOT EDIT! File to edit: convertToS3Gz.ipynb (unless otherwise specified).

__all__ = ['UploadGz']

# Cell
import os
try:
  BUCKET_NAME = os.environ['PRICE_BUCKET_NAME']
except Exception as e:
  print(f'missing environment variable {e} in Database s3 NB')
  BUCKET_NAME = None

# Cell
import os, logging
from s3bz.s3bz import S3
from .s3 import DatabaseS3

# Cell
class UploadGz:
  @staticmethod
  def run():
    data:dict = DatabaseS3.loadFromS3(bucketName=BUCKET_NAME)
    printYaml(data)
    return S3.saveGz(BUCKET_NAME, 'allData.gz', data)
