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
