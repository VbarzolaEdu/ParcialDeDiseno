# python_forestacion/entidades/terrenos/plantacion.py
from dataclasses import dataclass, field
from typing import List
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException

@dataclass
class Plantacion:
    nombre: str
    superficie_max: float
    agua_disponible: int = 500
    cultivos: List[Cultivo] = field(default_factory=list)
    trabajadores: List = field(default_factory=list)

    def add_cultivo(self, cultivo: Cultivo) -> None:
        ocupada = sum(c.get_superficie() for c in self.cultivos)
        superficie_requerida = ocupada + cultivo.get_superficie()
        if superficie_requerida > self.superficie_max:
            raise SuperficieInsuficienteException(
                superficie_requerida=superficie_requerida,
                superficie_disponible=self.superficie_max
            )
        self.cultivos.append(cultivo)

    def consumir_agua(self, cantidad: int) -> None:
        if cantidad < 0:
            raise ValueError("Cantidad negativa no permitida")
        if self.agua_disponible < cantidad:
            raise AguaAgotadaException(
                agua_requerida=cantidad,
                agua_disponible=self.agua_disponible
            )
        self.agua_disponible -= cantidad
