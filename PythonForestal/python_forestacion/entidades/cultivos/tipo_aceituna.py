# python_forestacion/entidades/cultivos/tipo_aceituna.py
from enum import Enum


class TipoAceituna(Enum):
    """
    Tipos de aceitunas disponibles para olivos.
    """
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"
