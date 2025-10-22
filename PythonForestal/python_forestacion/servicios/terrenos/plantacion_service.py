# python_forestacion/servicios/terrenos/plantacion_service.py
from datetime import date
from typing import List
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import CONSUMO_RIEGO_POR_LLAMADA

class PlantacionService:
    def plantar(self, plantacion: Plantacion, especie: str, cantidad: int, **kwargs) -> List:
        creados = []
        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie, **kwargs)
            plantacion.add_cultivo(cultivo)
            creados.append(cultivo)
        return creados

    def regar(self, plantacion: Plantacion, fecha: date = None, temperatura: float = 20.0, humedad: float = 50.0):
        if fecha is None:
            fecha = date.today()
        # consumir agua fija por riego
        plantacion.consumir_agua(CONSUMO_RIEGO_POR_LLAMADA)
        registry = CultivoServiceRegistry.get_instance()
        resultados = []
        for cultivo in plantacion.cultivos:
            cantidad = registry.absorber_agua(cultivo, fecha, temperatura, humedad)
            # si es árbol, hacerlo crecer
            try:
                if hasattr(cultivo, "crecer"):
                    # crecimiento simple por riego (según tipo)
                    if hasattr(cultivo, "variedad") or cultivo.__class__.__name__ in ("Pino", "Olivo"):
                        # reglas simples - pino sube 0.1, olivo 0.01
                        aumento = 0.10 if cultivo.__class__.__name__ == "Pino" else 0.01
                        cultivo.crecer(aumento)
            except Exception:
                pass
            resultados.append((cultivo, cantidad))
        return resultados
