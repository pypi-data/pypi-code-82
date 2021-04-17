import json
import logging
from abc import ABCMeta
from os import PathLike
from typing import Any, Dict, Optional

from python_jsonschema_objects import ObjectBuilder
from python_jsonschema_objects.classbuilder import LiteralValue, ProtocolBase
from python_jsonschema_objects.validators import ValidationError
from python_jsonschema_objects.wrapper_types import ArrayWrapper

logger = logging.getLogger(__name__)


class JsonSerializableMeta(ABCMeta):
    """
    A metaclass responsible for resolving a class' JSON schema
    and defining the class at hand based on it
    """

    def __new__(cls, name, bases, attrs):
        if "Json" not in attrs or not hasattr(attrs["Json"], "schema"):
            return super().__new__(cls, name, bases, attrs)

        path = attrs["Json"].schema.absolute()
        with path.open() as file:
            json_schema = json.load(file)

            builder = ObjectBuilder(str(path))

            classes = builder.build_classes(
                strict=True, named_only=True, standardize_names=False
            )

            json_schema = getattr(classes, name)

        return super().__new__(cls, name, (*bases, json_schema), attrs)


class JsonSerializable(ProtocolBase, metaclass=JsonSerializableMeta):
    """
    A class providing JSON serialization and de-serialization
    """

    class Json:
        schema: PathLike
        dependencies: Dict[str, "JsonSerializable"]

    def __setattr__(self, name: str, val: Any) -> None:
        try:
            super().__setattr__(name, val)
        except ValidationError:
            if hasattr(self, "__annotations__") and name in self.__annotations__:
                self.__dict__[name] = val
            else:
                raise

    @classmethod
    def _resolve_dependency(cls, obj: Any) -> Optional["JsonSerializable"]:
        """Given a `python_jsonschema_objects` it returns
        the `JsonSerializable` dependency that has been registered
        with it, given that it's available

        Returns:
            Optional["JsonSerializable"]: the corresponding `JsonSerializable`
            dependency
        """
        if not hasattr(cls.Json, "dependencies"):
            return None

        return cls.Json.dependencies.get(obj.__class__.__name__, None)

    def __getattribute__(self, name: str) -> Any:
        obj = super().__getattribute__(name)

        if isinstance(obj, LiteralValue):
            return obj._value
        if isinstance(obj, ArrayWrapper):
            array = []
            for element in obj.typed_elems:
                dependency = self._resolve_dependency(element)
                if dependency is None:
                    array.append(element)
                else:
                    array.append(dependency(**element.as_dict()))

            return array
        if isinstance(obj, ProtocolBase):
            dependency = self._resolve_dependency(obj)

            if dependency is not None:
                return dependency(**obj.as_dict())

            return obj

        return obj

    def __getattr__(self, name: str):
        if name in self.__prop_names__:
            return self._properties[name]
        if name in self._extended_properties:
            return self._extended_properties[name]

        return object.__getattribute__(self, name)
