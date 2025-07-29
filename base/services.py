from abc import ABC, abstractmethod
from typing import Any


class BaseService(ABC):
    @classmethod
    @abstractmethod
    def execute(cls, *args: tuple, **kwargs: dict[str, Any]) -> Any:  # noqa: ANN401
        raise NotImplementedError()
