"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/__init__.py
# ================================================================================

# python_forestacion/patrones/observer/__init__.py


# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/observable.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/observer.py
# ================================================================================

# python_forestacion/patrones/observer/observer.py
from typing import Generic, TypeVar, Protocol

T = TypeVar("T")

class Observer(Protocol[T]):
    def actualizar(self, evento: T) -> None:
        ...


