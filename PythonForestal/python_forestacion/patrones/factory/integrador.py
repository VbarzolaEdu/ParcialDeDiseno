"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/factory
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/factory/__init__.py
# ================================================================================

# python_forestacion/patrones/factory/__init__.py


# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/factory/cultivo_factory.py
# ================================================================================

# python_forestacion/patrones/factory/cultivo_factory.py
from typing import Callable
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.constantes import SUPERFICIE_PINO, SUPERFICIE_OLIVO, SUPERFICIE_LECHUGA, SUPERFICIE_ZANAHORIA

class CultivoFactory:
    _id_counter = 1

    @staticmethod
    def crear_cultivo(especie: str, **kwargs):
        factories: dict[str, Callable] = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria,
        }
        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")
        return factories[especie](**kwargs)

    @staticmethod
    def _next_id() -> int:
        i = CultivoFactory._id_counter
        CultivoFactory._id_counter += 1
        return i

    @staticmethod
    def _crear_pino(variedad: str = "Parana"):
        return Pino(id=CultivoFactory._next_id(), superficie=SUPERFICIE_PINO, variedad=variedad)

    @staticmethod
    def _crear_olivo(tipo_aceituna: str = "Arbequina"):
        return Olivo(id=CultivoFactory._next_id(), superficie=SUPERFICIE_OLIVO, tipo_aceituna=tipo_aceituna)

    @staticmethod
    def _crear_lechuga(variedad: str = "Crespa", invernadero: bool = True):
        return Lechuga(id=CultivoFactory._next_id(), superficie=SUPERFICIE_LECHUGA, variedad=variedad, invernadero=invernadero)

    @staticmethod
    def _crear_zanahoria(is_baby: bool = False):
        return Zanahoria(id=CultivoFactory._next_id(), superficie=SUPERFICIE_ZANAHORIA, is_baby=is_baby)


