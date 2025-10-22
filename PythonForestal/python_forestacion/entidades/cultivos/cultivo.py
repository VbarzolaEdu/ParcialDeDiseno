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
