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
