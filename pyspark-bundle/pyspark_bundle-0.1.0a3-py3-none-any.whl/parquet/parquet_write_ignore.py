from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from pysparkbundle.write.PathWriterDecorator import PathWriterDecorator


@DecoratedDecorator
class parquet_write_ignore(PathWriterDecorator):  # noqa: N801
    _mode = "ignore"
    _writer_service = "pysparkbundle.PathWriter.parquet"
