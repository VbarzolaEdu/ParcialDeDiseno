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
