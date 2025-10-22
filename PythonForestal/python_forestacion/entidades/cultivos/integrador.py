"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/__init__.py
# ================================================================================

# python_forestacion/entidades/cultivos/__init__.py


# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================

# python_forestacion/entidades/cultivos/arbol.py
from dataclasses import dataclass
from python_forestacion.entidades.cultivos.cultivo import Cultivo


@dataclass
class Arbol(Cultivo):
    """
    Clase base para arboles.
    Los arboles tienen altura y pueden crecer.
    """
    altura: float = 1.0
    
    def get_altura(self) -> float:
        return self.altura
    
    def set_altura(self, altura: float) -> None:
        if altura < 0:
            raise ValueError("Altura no puede ser negativa")
        self.altura = altura
    
    def crecer(self, incremento: float) -> None:
        """Incrementa la altura del arbol"""
        self.altura += incremento


# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================

# python_forestacion/entidades/cultivos/cultivo.py
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Cultivo:
    id: int
    superficie: float
    agua: int = 0

    def get_agua(self) -> int:
        return self.agua

    def set_agua(self, cantidad: int) -> None:
        if cantidad < 0:
            raise ValueError("Agua no puede ser negativa")
        self.agua = cantidad

    def get_superficie(self) -> float:
        return self.superficie


# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================

# python_forestacion/entidades/cultivos/hortaliza.py
from dataclasses import dataclass
from python_forestacion.entidades.cultivos.cultivo import Cultivo


@dataclass
class Hortaliza(Cultivo):
    """
    Clase base para hortalizas.
    Las hortalizas pueden estar en invernadero.
    """
    invernadero: bool = False
    
    def is_invernadero(self) -> bool:
        return self.invernadero
    
    def set_invernadero(self, invernadero: bool) -> None:
        self.invernadero = invernadero


# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================

# python_forestacion/entidades/cultivos/lechuga.py
from dataclasses import dataclass
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA

@dataclass
class Lechuga(Cultivo):
    variedad: str = "Crespa"
    invernadero: bool = True

    def __post_init__(self):
        if not hasattr(self, "agua") or self.agua is None:
            self.agua = AGUA_INICIAL_LECHUGA


# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================

# python_forestacion/entidades/cultivos/olivo.py
from dataclasses import dataclass, field
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.constantes import AGUA_INICIAL_OLIVO, ALTURA_INICIAL_OLIVO

@dataclass
class Olivo(Cultivo):
    tipo_aceituna: str = "Arbequina"
    altura: float = field(default=ALTURA_INICIAL_OLIVO)

    def __post_init__(self):
        if not hasattr(self, "agua") or self.agua is None:
            self.agua = AGUA_INICIAL_OLIVO

    def crecer(self, aumento: float) -> None:
        self.altura += aumento


# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/pino.py
# ================================================================================

# python_forestacion/entidades/cultivos/pino.py
from dataclasses import dataclass, field
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.constantes import AGUA_INICIAL_PINO, ALTURA_INICIAL_PINO, SUPERFICIE_PINO

@dataclass
class Pino(Cultivo):
    variedad: str = "Parana"
    altura: float = field(default=ALTURA_INICIAL_PINO)

    def __post_init__(self):
        if not hasattr(self, "agua") or self.agua is None:
            self.agua = AGUA_INICIAL_PINO

    def crecer(self, aumento: float) -> None:
        self.altura += aumento


# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================

# python_forestacion/entidades/cultivos/tipo_aceituna.py
from enum import Enum


class TipoAceituna(Enum):
    """
    Tipos de aceitunas disponibles para olivos.
    """
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"


# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================

# python_forestacion/entidades/cultivos/zanahoria.py
from dataclasses import dataclass
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA

@dataclass
class Zanahoria(Cultivo):
    is_baby: bool = False

    def __post_init__(self):
        if not hasattr(self, "agua") or self.agua is None:
            self.agua = AGUA_INICIAL_ZANAHORIA


