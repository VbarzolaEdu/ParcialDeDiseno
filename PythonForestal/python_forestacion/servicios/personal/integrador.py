"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/personal
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/personal/__init__.py
# ================================================================================

# python_forestacion/servicios/personal/__init__.py


# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/personal/trabajador_service.py
# ================================================================================

# python_forestacion/servicios/personal/trabajador_service.py
from datetime import date
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.tarea import Tarea
from typing import List


class TrabajadorService:
    """
    Servicio para gestion de trabajadores.
    Proporciona metodos para asignar aptos medicos y ejecutar tareas.
    """
    
    def asignar_apto_medico(
        self,
        trabajador: Trabajador,
        apto: bool,
        fecha_emision: date,
        observaciones: str = None
    ) -> None:
        """
        Asigna un apto medico a un trabajador.
        
        Args:
            trabajador: Trabajador al que se le asigna el apto
            apto: Estado de aptitud (True = apto, False = no apto)
            fecha_emision: Fecha de emision del apto
            observaciones: Observaciones medicas opcionales
        """
        apto_medico = AptoMedico(
            apto=apto,
            fecha_emision=fecha_emision,
            observaciones=observaciones
        )
        trabajador.set_apto_medico(apto_medico)
    
    def trabajar(
        self,
        trabajador: Trabajador,
        fecha: date,
        util: Herramienta
    ) -> bool:
        """
        Ejecuta las tareas asignadas a un trabajador para una fecha especifica.
        Las tareas se ejecutan en orden descendente por ID.
        
        Args:
            trabajador: Trabajador que ejecutara las tareas
            fecha: Fecha de las tareas a ejecutar
            util: Herramienta a usar en las tareas
            
        Returns:
            bool: True si el trabajador tiene apto y ejecuto tareas, False sino
        """
        # Verificar apto medico
        if trabajador.get_apto_medico() is None or not trabajador.get_apto_medico().esta_apto():
            print(f"El trabajador {trabajador.get_nombre()} no tiene apto medico valido")
            return False
        
        # Filtrar tareas de la fecha especificada
        tareas_del_dia = [
            tarea for tarea in trabajador.get_tareas()
            if tarea.get_fecha() == fecha and not tarea.is_completada()
        ]
        
        if not tareas_del_dia:
            print(f"No hay tareas pendientes para {trabajador.get_nombre()} en la fecha {fecha}")
            return True
        
        # Ordenar tareas por ID descendente usando metodo estatico
        tareas_ordenadas = sorted(tareas_del_dia, key=self._obtener_id_tarea, reverse=True)
        
        # Ejecutar tareas
        for tarea in tareas_ordenadas:
            print(f"El trabajador {trabajador.get_nombre()} realizo la tarea {tarea.get_id_tarea()} "
                  f"{tarea.get_descripcion()} con herramienta: {util.get_nombre()}")
            tarea.marcar_completada()
        
        return True
    
    @staticmethod
    def _obtener_id_tarea(tarea: Tarea) -> int:
        """
        Metodo estatico para obtener el ID de una tarea.
        Usado para ordenamiento en lugar de lambdas.
        
        Args:
            tarea: Tarea de la que se obtiene el ID
            
        Returns:
            int: ID de la tarea
        """
        return tarea.get_id_tarea()


