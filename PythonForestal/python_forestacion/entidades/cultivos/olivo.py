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
