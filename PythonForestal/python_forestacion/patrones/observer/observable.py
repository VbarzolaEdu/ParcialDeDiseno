# python_forestacion/patrones/observer/observable.py
from typing import Generic, TypeVar, List
from threading import Lock
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar("T")

class Observable(Generic[T]):
    def __init__(self):
        self._observadores: List[Observer[T]] = []
        self._lock = Lock()

    def agregar_observador(self, observador: Observer[T]) -> None:
        with self._lock:
            if observador not in self._observadores:
                self._observadores.append(observador)

    def quitar_observador(self, observador: Observer[T]) -> None:
        with self._lock:
            if observador in self._observadores:
                self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        # copia para evitar modificaciones concurrentes
        with self._lock:
            observadores = list(self._observadores)
        for obs in observadores:
            try:
                obs.actualizar(evento)
            except Exception:
                # no romper el ciclo si un observador falla
                pass
