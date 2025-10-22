# python_forestacion/servicios/cultivos/zanahoria_service.py
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy


class ZanahoriaService(CultivoService):
    """
    Servicio especifico para gestion de zanahorias.
    Usa absorcion constante de 2L (Strategy Pattern).
    """
    
    def __init__(self):
        # Inyectar estrategia constante: zanahorias absorben 2L siempre
        super().__init__(AbsorcionConstanteStrategy(2))
