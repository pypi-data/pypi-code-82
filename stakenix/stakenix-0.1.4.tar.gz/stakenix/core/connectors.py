from pathlib import Path
from contextlib import contextmanager

from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from sqlalchemy.exc import ProgrammingError
from sshtunnel import SSHTunnelForwarder

from stakenix import Session
from stakenix.config import Config

class Connector:
    def __init__(self) -> None:
        self.config = Config().get_config()
    
    def connection(self):
        raise NotImplementedError


class SQLConnector(Connector):
    def __init__(self) -> None:
        super().__init__()
        self.config: dict = self.config["sql"]
        self.schema: str = None

    def _generate_session(self) -> Session:
        Session.configure(bind=create_engine(self._create_connection_url()))
        return Session()

    @contextmanager
    def connection(self) -> Connection:
        session = self._generate_session()
        try:
            yield session
        except Exception as exc:
            session.rollback()
            raise ProgrammingError(exc, "", "")
        finally:
            session.close()
    
    def _create_connection_url(self) -> str:
        url = "{driver}://{username}:{password}@{host}:{port}/{schema}"
        return url.format(
            driver=self.driver,
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            schema=self.database
        )

    def _get_params(self, alias: str, database: str) -> None:
        self.config = self.config[alias]
        self.driver = self.config["driver"]["name"]
        self.host = self.config["databases"][database]["host"]
        self.port = self.config["databases"][database]["port"]
        self.username = self.config["databases"][database]["username"]
        self.password = self.config["databases"][database]["password"]
        self.database = self.config["databases"][database].get("database_name", self.schema)


class NoSQLConnector(Connector):
    def __init__(self) -> None:
        super().__init__()
        self.config = self.config["nosql"]

    def _get_params(self, alias) -> None:
        self.config = self.config[alias]["databases"][self.schema]
        self.database = self.config["database_name"]
        self.host = self.config["host"]
        self.username = self.config["username"]
        self.password = self.config["password"]
        self.ssh_host = self.config["ssh_host"]
        self.ssh_username = self.config["ssh_username"]
        self.ssh_pkey = Path.home().joinpath('.ssh').joinpath('id_rsa')


class MySQLConnector(SQLConnector):
    def __init__(self, schema: str, database: str = "default") -> None:
        super().__init__()
        self.schema = schema
        self._get_params(alias="mysql", database=database)


class PostgreSQLConnector(SQLConnector):
    def __init__(self, schema: str, database: str = "default") -> None:
        super().__init__()
        self.schema = schema
        self._get_params(alias="postgresql", database=database)


class MsSQLConnector(SQLConnector):
    def __init__(self, schema: str, database: str = "default") -> None:
        super().__init__()
        self.schema = schema
        self._get_params(alias="mssql", database=database)


class ClickHouseConnector(SQLConnector):
    def __init__(self, schema: str, database: str = "default") -> None:
        super().__init__()
        self.schema = schema
        self._get_params(alias="clickhouse", database=database)


class MongoDBConnector(NoSQLConnector):
    def __init__(self, schema: str) -> None:
        super().__init__()
        self.schema = schema
        self._get_params(alias="mongodb")

    @contextmanager
    def connection(self) -> MongoClient:
        ssh_params = dict(
            ssh_address_or_host=self.ssh_host, 
            ssh_username=self.ssh_username,
            ssh_pkey=str(self.ssh_pkey),
            remote_bind_address=(self.host, 27017)
        )
        try:
            ssh = SSHTunnelForwarder(**ssh_params)
            ssh.start()
            mongo_params = dict(
                host=self.host,
                port=ssh.local_bind_port,
                password=self.password,
                username=self.username
            )
            yield MongoClient(**mongo_params)[self.database]
        except Exception as exc:
            raise ProgrammingError(exc, "", "")
        finally:
            ssh.close()