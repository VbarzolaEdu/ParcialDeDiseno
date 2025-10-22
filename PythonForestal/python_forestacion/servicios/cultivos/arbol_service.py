# python_forestacion/servicios/cultivos/arbol_service.py
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO_POR_RIEGO, CRECIMIENTO_OLIVO_POR_RIEGO
from datetime import date


class ArbolService(CultivoService):
    """
    Servicio base para gestion de arboles.
    Los arboles tienen la capacidad adicional de crecer en altura.
    """
    
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        super().__init__(estrategia_absorcion)
    
    def crecer(self, arbol, incremento: float) -> None:
        """
        Hace crecer un arbol en altura.
        
        Args:
            arbol: Arbol que crecera
            incremento: Cantidad de metros a crecer
        """
        if hasattr(arbol, 'crecer'):
            arbol.crecer(incremento)
