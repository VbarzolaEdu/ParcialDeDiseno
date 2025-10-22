"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/terrenos
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================

# python_forestacion/servicios/terrenos/__init__.py


# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ================================================================================

# python_forestacion/servicios/terrenos/registro_forestal_service.py
import os
import pickle
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA
from python_forestacion.excepciones.persistencia_exception import PersistenciaException


class RegistroForestalService:
    """
    Servicio para gestion de registros forestales.
    Proporciona persistencia con Pickle y mostracion de datos.
    """
    
    def mostrar_datos(self, registro: RegistroForestal) -> None:
        """
        Muestra todos los datos del registro forestal de forma detallada.
        
        Args:
            registro: Registro forestal a mostrar
        """
        print("\nREGISTRO FORESTAL")
        print("="*50)
        print(f"Padron:      {registro.id_padron}")
        print(f"Propietario: {registro.propietario}")
        print(f"Avaluo:      ${registro.avaluo:,.2f}")
        print(f"Domicilio:   {registro.tierra.domicilio}")
        print(f"Superficie:  {registro.tierra.superficie:.2f} m²")
        print(f"Cantidad de cultivos plantados: {len(registro.plantacion.cultivos)}")
        
        if registro.plantacion.cultivos:
            print(f"\nListado de Cultivos plantados")
            print("_"*50)
            registry = CultivoServiceRegistry.get_instance()
            for cultivo in registro.plantacion.cultivos:
                print()
                registry.mostrar_datos(cultivo)
    
    def persistir(self, registro: RegistroForestal) -> None:
        """
        Persiste un registro forestal en disco usando Pickle.
        
        Args:
            registro: Registro forestal a persistir
            
        Raises:
            PersistenciaException: Si ocurre error al persistir
        """
        propietario = registro.propietario
        
        if not propietario or propietario.strip() == "":
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")
        
        # Crear directorio si no existe
        os.makedirs(DIRECTORIO_DATA, exist_ok=True)
        
        # Construir nombre de archivo
        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)
        
        file_handle = None
        try:
            file_handle = open(ruta_completa, "wb")
            pickle.dump(registro, file_handle)
            print(f"Registro de {propietario} persistido exitosamente en {ruta_completa}")
        except Exception as e:
            raise PersistenciaException(
                user_message=f"Error al persistir registro de {propietario}",
                technical_message=str(e),
                nombre_archivo=nombre_archivo,
                tipo_operacion="ESCRITURA"
            )
        finally:
            if file_handle:
                file_handle.close()
    
    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """
        Lee un registro forestal desde disco.
        
        Args:
            propietario: Nombre del propietario
            
        Returns:
            RegistroForestal: Registro recuperado
            
        Raises:
            ValueError: Si propietario es nulo o vacio
            PersistenciaException: Si ocurre error al leer
        """
        if not propietario or propietario.strip() == "":
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")
        
        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)
        
        if not os.path.exists(ruta_completa):
            raise PersistenciaException(
                user_message=f"No se encontro registro de {propietario}",
                technical_message=f"Archivo no existe: {ruta_completa}",
                nombre_archivo=nombre_archivo,
                tipo_operacion="LECTURA"
            )
        
        file_handle = None
        try:
            file_handle = open(ruta_completa, "rb")
            registro = pickle.load(file_handle)
            print(f"Registro de {propietario} recuperado exitosamente desde {ruta_completa}")
            return registro
        except Exception as e:
            raise PersistenciaException(
                user_message=f"Error al leer registro de {propietario}",
                technical_message=str(e),
                nombre_archivo=nombre_archivo,
                tipo_operacion="LECTURA"
            )
        finally:
            if file_handle:
                file_handle.close()


# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

# python_forestacion/servicios/terrenos/tierra_service.py
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


class TierraService:
    """
    Servicio para gestion de terrenos.
    Proporciona metodos para crear y gestionar tierras con plantaciones.
    """
    
    def crear_tierra(self, id_padron_catastral: int, superficie: float, domicilio: str) -> Tierra:
        """
        Crea un nuevo terreno.
        
        Args:
            id_padron_catastral: Numero de padron unico
            superficie: Superficie en metros cuadrados
            domicilio: Direccion del terreno
            
        Returns:
            Tierra: Terreno creado
            
        Raises:
            ValueError: Si la superficie es <= 0
        """
        return Tierra(
            id_padron_catastral=id_padron_catastral,
            superficie=superficie,
            domicilio=domicilio
        )
    
    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str,
        agua_disponible: int = 500
    ) -> Tierra:
        """
        Crea un terreno con una plantacion asociada.
        
        Args:
            id_padron_catastral: Numero de padron unico
            superficie: Superficie en metros cuadrados
            domicilio: Direccion del terreno
            nombre_plantacion: Nombre de la plantacion
            agua_disponible: Agua disponible inicial (default: 500L)
            
        Returns:
            Tierra: Terreno con plantacion asociada
        """
        tierra = self.crear_tierra(id_padron_catastral, superficie, domicilio)
        
        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie_max=superficie,
            agua_disponible=agua_disponible
        )
        
        tierra.set_finca(plantacion)
        return tierra


