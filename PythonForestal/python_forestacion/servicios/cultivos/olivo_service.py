# python_forestacion/servicios/cultivos/olivo_service.py
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy


class OlivoService(ArbolService):
    """
    Servicio especifico para gestion de olivos.
    Usa absorcion estacional (Strategy Pattern).
    """
    
    def __init__(self):
        # Inyectar estrategia estacional para arboles
        super().__init__(AbsorcionSeasonalStrategy())
