"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones/__init__.py
# ================================================================================

# python_forestacion/excepciones/__init__.py


# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================

# python_forestacion/excepciones/agua_agotada_exception.py
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente agua disponible para regar.
    
    Attributes:
        agua_requerida: Cantidad de agua necesaria
        agua_disponible: Cantidad de agua disponible
    """
    
    def __init__(
        self,
        agua_requerida: int,
        agua_disponible: int,
        user_message: str = None,
        technical_message: str = None
    ):
        if user_message is None:
            user_message = f"No hay suficiente agua. Requerida: {agua_requerida}L, Disponible: {agua_disponible}L"
        
        if technical_message is None:
            technical_message = f"AguaAgotadaException: requerida={agua_requerida}, disponible={agua_disponible}"
        
        super().__init__(user_message, technical_message)
        self.agua_requerida = agua_requerida
        self.agua_disponible = agua_disponible
    
    def get_agua_requerida(self) -> int:
        return self.agua_requerida
    
    def get_agua_disponible(self) -> int:
        return self.agua_disponible


# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

# python_forestacion/excepciones/forestacion_exception.py

class ForestacionException(Exception):
    """
    Excepcion base para todas las excepciones del sistema de gestion forestal.
    Proporciona mensajes separados para usuario y tecnico.
    
    Attributes:
        user_message: Mensaje amigable para el usuario
        technical_message: Mensaje tecnico detallado para debugging
    """
    
    def __init__(self, user_message: str, technical_message: str = ""):
        self.user_message = user_message
        self.technical_message = technical_message or user_message
        super().__init__(self.user_message)
    
    def get_user_message(self) -> str:
        """Retorna el mensaje para el usuario"""
        return self.user_message
    
    def get_technical_message(self) -> str:
        """Retorna el mensaje tecnico"""
        return self.technical_message


# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones/mensajes_exception.py
# ================================================================================

# python_forestacion/excepciones/mensajes_exception.py
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class MensajesException(ForestacionException):
    """
    Excepción para errores relacionados con mensajes y comunicaciones del sistema.
    """
    
    def __init__(self, user_message: str, technical_message: str = None):
        super().__init__(user_message, technical_message or user_message)


# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

# python_forestacion/excepciones/persistencia_exception.py
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class PersistenciaException(ForestacionException):
    """
    Excepcion para errores de persistencia de datos.
    Proporciona informacion detallada sobre el error.
    
    Attributes:
        nombre_archivo: Nombre del archivo involucrado
        tipo_operacion: Tipo de operacion (LECTURA o ESCRITURA)
    """
    
    def __init__(
        self,
        user_message: str,
        technical_message: str,
        nombre_archivo: str = "",
        tipo_operacion: str = "DESCONOCIDA"
    ):
        super().__init__(user_message, technical_message)
        self.nombre_archivo = nombre_archivo
        self.tipo_operacion = tipo_operacion
    
    def get_nombre_archivo(self) -> str:
        """Retorna el nombre del archivo involucrado"""
        return self.nombre_archivo
    
    def get_tipo_operacion(self) -> str:
        """Retorna el tipo de operacion"""
        return self.tipo_operacion


# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================

# python_forestacion/excepciones/superficie_insuficiente_exception.py
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class SuperficieInsuficienteException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente superficie disponible para plantar.
    
    Attributes:
        superficie_requerida: Superficie necesaria
        superficie_disponible: Superficie disponible
    """
    
    def __init__(
        self,
        superficie_requerida: float,
        superficie_disponible: float,
        user_message: str = None,
        technical_message: str = None
    ):
        if user_message is None:
            user_message = f"No hay suficiente superficie. Requerida: {superficie_requerida}m², Disponible: {superficie_disponible}m²"
        
        if technical_message is None:
            technical_message = f"SuperficieInsuficienteException: requerida={superficie_requerida}, disponible={superficie_disponible}"
        
        super().__init__(user_message, technical_message)
        self.superficie_requerida = superficie_requerida
        self.superficie_disponible = superficie_disponible
    
    def get_superficie_requerida(self) -> float:
        return self.superficie_requerida
    
    def get_superficie_disponible(self) -> float:
        return self.superficie_disponible


