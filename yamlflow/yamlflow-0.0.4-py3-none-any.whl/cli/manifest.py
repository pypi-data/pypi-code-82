import os
import sys

import yaml

from dataclasses import dataclass, asdict


@dataclass(frozen=True, order=True)
class _meta:
    name: str
    version: str

    def __repr__(self):
        return f"{self.name}:{self.version}"


@dataclass(frozen=True, order=True)
class _backend:
    runtime: str
    device: str
    
    def __repr__(self):
        return f"{self.runtime}-{self.device}"


@dataclass(frozen=True, order=True)
class _frontend:
    predictor: str
    requirements: str
    


class Manifest:

    def __init__(self, mainfest_path: str):
        super().__init__()
        self._yf = mainfest_path
        if self._yf == ".":
            self._read_from_file()
        else:
            self._read_from_dir()

    
    def _read_from_file(self) -> None:
        with open(self._yf, 'r') as stream:
            try:
                self.data = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                print(err)
                sys.exit(1)


    def _read_from_dir(self) -> None:
        with open(os.path.join(self._yf, "flow.yaml"), 'r') as stream:
            try:
                self.data = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                print(err)
                sys.exit(1)


    @property
    def meta(self):
        return repr(_meta(**self.data["meta"]))


    @property
    def backend(self):
        return repr(_backend(**self.data["backend"]))


    def build_info(self):
        return {
            "buildargs": {"backend": self.backend}, 
            "tag": self.meta,
            "path": os.path.join(
                os.path.abspath(os.path.dirname(__file__)), 
                "dockerfiles", 
                self.backend
            )
        }
