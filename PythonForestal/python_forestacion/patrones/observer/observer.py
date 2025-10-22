# python_forestacion/patrones/observer/observer.py
from typing import Generic, TypeVar, Protocol

T = TypeVar("T")

class Observer(Protocol[T]):
    def actualizar(self, evento: T) -> None:
        ...
