import os
from typing import Mapping, Iterator, NoReturn, Any

import dotenv


class _ExtendedEnviron(Mapping[str, str]):
    def __init__(self) -> None:
        self._dot_env: Mapping[str, str] = dotenv.dotenv_values(".env") or {}

    def __getitem__(self, key: str) -> str:
        if not isinstance(key, str):
            raise ValueError(f"str expected, not {type(key)}")

        try:
            return os.environ.get(key, self._dot_env[key])
        except KeyError:
            raise KeyError(key) from None

    def __setitem__(self, key: Any, value: Any) -> NoReturn:
        raise NotImplementedError("object is readonly. set is not allowed")

    def __len__(self) -> int:
        return len(self.get_dot_env_combined_with_environ())

    def __iter__(self) -> Iterator[str]:
        return iter(self.get_dot_env_combined_with_environ())

    def get_dot_env_combined_with_environ(self) -> Mapping[str, str]:
        return {**self._dot_env, **os.environ}


extended_environ = _ExtendedEnviron()
