# python_forestacion/servicios/cultivos/lechuga_service.py
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy


class LechugaService(CultivoService):
    """
    Servicio especifico para gestion de lechugas.
    Usa absorcion constante de 1L (Strategy Pattern).
    """
    
    def __init__(self):
        # Inyectar estrategia constante: lechugas absorben 1L siempre
        super().__init__(AbsorcionConstanteStrategy(1))
