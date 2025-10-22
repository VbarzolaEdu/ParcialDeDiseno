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
