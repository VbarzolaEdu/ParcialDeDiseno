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
