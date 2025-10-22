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
