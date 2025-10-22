"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion
Fecha de generacion: 2025-10-21 22:24:05
Total de archivos integrados: 67
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================


# DIRECTORIO: ..
#   1. main.py
#
# DIRECTORIO: .
#   2. __init__.py
#   3. constantes.py
#
# DIRECTORIO: entidades
#   4. __init__.py
#
# DIRECTORIO: entidades\cultivos
#   5. __init__.py
#   6. arbol.py
#   7. cultivo.py
#   8. hortaliza.py
#   9. lechuga.py
#   10. olivo.py
#   11. pino.py
#   12. tipo_aceituna.py
#   13. zanahoria.py
#
# DIRECTORIO: entidades/personal
#   14. __init__.py
#   15. apto_medico.py
#   16. herramienta.py
#   17. tarea.py
#   18. trabajador.py
#
# DIRECTORIO: entidades/terrenos
#   19. __init__.py
#   20. plantacion.py
#   21. registro_forestal.py
#   22. tierra.py
#
# DIRECTORIO: excepciones
#   23. __init__.py
#   24. agua_agotada_exception.py
#   25. forestacion_exception.py
#   26. mensajes_exception.py
#   27. persistencia_exception.py
#   28. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   29. __init__.py
#
# DIRECTORIO: patrones/factory
#   30. __init__.py
#   31. cultivo_factory.py
#
# DIRECTORIO: patrones/observer
#   32. __init__.py
#   33. observable.py
#   34. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   35. __init__.py
#   36. evento_plantacion.py
#   37. evento_sensor.py
#
# DIRECTORIO: patrones/singleton
#   38. __init__.py
#
# DIRECTORIO: patrones/strategy
#   39. __init__.py
#   40. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   41. __init__.py
#   42. absorcion_constante_strategy.py
#   43. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   44. __init__.py
#
# DIRECTORIO: riego/control
#   45. __init__.py
#   46. control_riego_task.py
#
# DIRECTORIO: riego/sensores
#   47. __init__.py
#   48. humedad_reader_task.py
#   49. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   50. __init__.py
#
# DIRECTORIO: servicios/cultivos
#   51. __init__.py
#   52. arbol_service.py
#   53. cultivo_service.py
#   54. cultivo_service_registry.py
#   55. lechuga_service.py
#   56. olivo_service.py
#   57. pino_service.py
#   58. zanahoria_service.py
#
# DIRECTORIO: servicios/negocio
#   59. __init__.py
#   60. fincas_service.py
#   61. paquete.py
#
# DIRECTORIO: servicios/personal
#   62. __init__.py
#   63. trabajador_service.py
#
# DIRECTORIO: servicios/terrenos
#   64. __init__.py
#   65. plantacion_service.py
#   66. registro_forestal_service.py
#   67. tierra_service.py
#



################################################################################
# DIRECTORIO: ..
################################################################################


# ==============================================================================
# ARCHIVO 1/67: main.py
# Directorio: .
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/main.py
# ==============================================================================


"""
===============================================================================
SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO
===============================================================================

Aplicacion de gestion forestal que demuestra el uso de multiples patrones de
diseno a traves de Historias de Usuario (User Stories).

PATRONES IMPLEMENTADOS:
1. SINGLETON - CultivoServiceRegistry (unica instancia del registro de servicios)
2. FACTORY METHOD - Creacion de cultivos segun tipo
3. OBSERVER - Sistema de monitoreo de sensores y eventos
4. STRATEGY - Algoritmos intercambiables de absorcion de agua
5. REGISTRY - Dispatch polimorfico para servicios de cultivos
"""

import sys
import time
from datetime import date
from typing import Tuple

# Constantes
from python_forestacion.constantes import (
    THREAD_JOIN_TIMEOUT,
    INTERVALO_SENSOR_TEMPERATURA,
    INTERVALO_SENSOR_HUMEDAD,
    COOLDOWN_RIEGO
)

# Entidades
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

# Servicios
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

# Sistema de riego
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

# Excepciones
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException


def imprimir_encabezado():
    """Imprime el encabezado del sistema."""
    print("\n" + "=" * 80)
    print("           SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print("=" * 80)
    print()


def imprimir_epic(numero: int, titulo: str):
    """Imprime el encabezado de un Epic."""
    print("\n" + "=" * 80)
    print(f"EPIC {numero}: {titulo}")
    print("=" * 80)


def imprimir_us(numero: str, descripcion: str):
    """Imprime el encabezado de una User Story."""
    print(f"\n>> {numero}: {descripcion}")


def imprimir_patron(nombre: str, descripcion: str):
    """Imprime informacion sobre un patron aplicado."""
    print(f"\n   [PATRON {nombre}] {descripcion}")


def epic1_gestion_terrenos() -> Tuple[Tierra, Plantacion, RegistroForestal]:
    """
    EPIC 1: GESTION DE TERRENOS Y PLANTACIONES
    
    User Stories:
    - US-001: Registrar Terreno Forestal
    - US-002: Crear Plantacion en Terreno
    - US-003: Crear Registro Forestal Completo
    """
    imprimir_epic(1, "GESTION DE TERRENOS Y PLANTACIONES")
    
    tierra_service = TierraService()
    
    # US-001 y US-002: Crear Tierra con Plantacion
    imprimir_us("US-001/US-002", "Registrar Terreno y Crear Plantacion")
    
    tierra = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Lujan de Cuyo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    
    plantacion = tierra.finca
    
    print(f"   Terreno registrado - Padron: {tierra.id_padron_catastral}")
    print(f"   Superficie: {tierra.superficie} m²")
    print(f"   Plantacion: {plantacion.nombre}")
    print(f"   Agua disponible: {plantacion.agua_disponible} L")
    
    # US-003: Crear Registro Forestal
    imprimir_us("US-003", "Crear Registro Forestal Completo")
    
    registro = RegistroForestal(
        id_padron=tierra.id_padron_catastral,
        tierra=tierra,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )
    
    print(f"   Registro creado para: {registro.propietario}")
    print(f"   Avaluo: ${registro.avaluo:,.2f}")
    
    # Validaciones
    print("\n   [VALIDACIONES]")
    try:
        tierra.set_superficie(-100)
    except ValueError as e:
        print(f"   ✓ Superficie negativa rechazada: {e}")
    
    try:
        tierra.set_superficie(0)
    except ValueError as e:
        print(f"   ✓ Superficie cero rechazada: {e}")
    
    return tierra, plantacion, registro


def epic2_gestion_cultivos(plantacion: Plantacion) -> PlantacionService:
    """
    EPIC 2: GESTION DE CULTIVOS
    
    User Stories:
    - US-004: Plantar Pinos (Factory Method)
    - US-005: Plantar Olivos con Tipo de Aceituna
    - US-006: Plantar Lechugas en Invernadero
    - US-007: Plantar Zanahorias
    - US-008: Regar Cultivos (Strategy Pattern)
    - US-009: Mostrar Datos de Cultivos (Registry Pattern)
    """
    imprimir_epic(2, "GESTION DE CULTIVOS")
    
    # ===================================================================
    # PATRON FACTORY METHOD
    # El metodo plantar() usa un Factory para crear instancias
    # de diferentes tipos de cultivos sin que el codigo cliente
    # necesite conocer los detalles de construccion.
    # ===================================================================
    imprimir_patron("FACTORY METHOD", 
                   "Creacion de cultivos mediante CultivoFactory")
    
    plantacion_service = PlantacionService()
    
    # US-004: Plantar Pinos
    imprimir_us("US-004", "Plantar Pinos")
    pinos = plantacion_service.plantar(plantacion, "Pino", 5, variedad="Parana")
    print(f"   {len(pinos)} Pinos plantados")
    print(f"   Superficie: {sum(p.get_superficie() for p in pinos)} m²")
    
    # US-005: Plantar Olivos
    imprimir_us("US-005", "Plantar Olivos con Tipo de Aceituna")
    olivos = plantacion_service.plantar(plantacion, "Olivo", 5, tipo_aceituna="Arbequina")
    print(f"   {len(olivos)} Olivos plantados")
    print(f"   Superficie: {sum(o.get_superficie() for o in olivos)} m²")
    
    # US-006: Plantar Lechugas
    imprimir_us("US-006", "Plantar Lechugas en Invernadero")
    lechugas = plantacion_service.plantar(plantacion, "Lechuga", 5, variedad="Crespa", invernadero=True)
    print(f"   {len(lechugas)} Lechugas plantadas")
    print(f"   Superficie: {sum(l.get_superficie() for l in lechugas)} m²")
    
    # US-007: Plantar Zanahorias
    imprimir_us("US-007", "Plantar Zanahorias")
    zanahorias = plantacion_service.plantar(plantacion, "Zanahoria", 5, is_baby=False)
    print(f"   {len(zanahorias)} Zanahorias plantadas")
    print(f"   Superficie: {sum(z.get_superficie() for z in zanahorias)} m²")
    
    # Resumen
    total_cultivos = len(plantacion.cultivos)
    superficie_ocupada = sum(c.get_superficie() for c in plantacion.cultivos)
    print(f"\n   Total de cultivos: {total_cultivos}")
    print(f"   Superficie ocupada: {superficie_ocupada:.2f} m²")
    print(f"   Superficie disponible: {plantacion.superficie_max - superficie_ocupada:.2f} m²")
    
    # ===================================================================
    # PATRON STRATEGY
    # Durante el riego, cada cultivo usa diferentes ESTRATEGIAS
    # de absorcion de agua segun su tipo.
    # ===================================================================
    imprimir_patron("STRATEGY", 
                   "Algoritmos intercambiables de absorcion de agua")
    
    # US-008: Regar Cultivos
    imprimir_us("US-008", "Regar Cultivos")
    agua_antes = plantacion.agua_disponible
    print(f"   Agua disponible: {agua_antes} L")
    
    resultados = plantacion_service.regar(
        plantacion,
        fecha=date.today(),
        temperatura=15.0,
        humedad=30.0
    )
    
    agua_despues = plantacion.agua_disponible
    print(f"   Riego completado - Agua consumida: {agua_antes - agua_despues} L")
    print(f"   Agua restante: {agua_despues} L")
    
    # ===================================================================
    # PATRON REGISTRY
    # ===================================================================
    imprimir_patron("REGISTRY", 
                   "Dispatch polimorfico para mostrar datos")
    
    # US-009: Mostrar Datos de Cultivos
    imprimir_us("US-009", "Mostrar Datos de Cultivos")
    registry = CultivoServiceRegistry.get_instance()
    
    print("\n   Mostrando datos de los primeros 2 cultivos:")
    for cultivo in plantacion.cultivos[:2]:
        print("   " + "-" * 40)
        registry.mostrar_datos(cultivo)
    
    # Validaciones de excepciones
    print("\n   [VALIDACIONES]")
    
    # Validar SuperficieInsuficienteException
    try:
        plantacion_service.plantar(plantacion, "Pino", 10000)
    except SuperficieInsuficienteException as e:
        print(f"   ✓ SuperficieInsuficienteException capturada")
        print(f"     Requerida: {e.get_superficie_requerida():.2f} m²")
        print(f"     Disponible: {e.get_superficie_disponible():.2f} m²")
    
    # Validar AguaAgotadaException
    agua_backup = plantacion.agua_disponible
    plantacion.agua_disponible = 0
    try:
        plantacion_service.regar(plantacion)
    except AguaAgotadaException as e:
        print(f"   ✓ AguaAgotadaException capturada")
        print(f"     Requerida: {e.get_agua_requerida()} L")
        print(f"     Disponible: {e.get_agua_disponible()} L")
    finally:
        plantacion.agua_disponible = agua_backup
    
    return plantacion_service


def epic3_sistema_riego(plantacion: Plantacion, plantacion_service: PlantacionService):
    """
    EPIC 3: SISTEMA DE RIEGO AUTOMATIZADO
    
    User Stories:
    - US-010: Monitorear Temperatura (Observer Pattern)
    - US-011: Monitorear Humedad (Observer Pattern)
    - US-012: Control Automatico de Riego
    - US-013: Detener Sistema de Forma Segura
    """
    imprimir_epic(3, "SISTEMA DE RIEGO AUTOMATIZADO")
    
    # ===================================================================
    # PATRON OBSERVER
    # ===================================================================
    imprimir_patron("OBSERVER", 
                   "Sistema de sensores con notificacion de eventos")
    
    # US-010: Crear sensor de temperatura
    imprimir_us("US-010", "Monitorear Temperatura")
    tarea_temp = TemperaturaReaderTask(
        intervalo=INTERVALO_SENSOR_TEMPERATURA,
        min_temp=5.0,
        max_temp=20.0
    )
    print(f"   Sensor creado - Intervalo: {INTERVALO_SENSOR_TEMPERATURA}s")
    
    # US-011: Crear sensor de humedad
    imprimir_us("US-011", "Monitorear Humedad")
    tarea_hum = HumedadReaderTask(
        intervalo=INTERVALO_SENSOR_HUMEDAD,
        min_hum=20.0,
        max_hum=70.0
    )
    print(f"   Sensor creado - Intervalo: {INTERVALO_SENSOR_HUMEDAD}s")
    
    # US-012: Control automatico
    imprimir_us("US-012", "Control Automatico de Riego")
    tarea_control = ControlRiegoTask(
        plantacion=plantacion,
        cooldown_seconds=COOLDOWN_RIEGO
    )
    
    # Registrar observadores
    tarea_temp.agregar_observador(tarea_control)
    tarea_hum.agregar_observador(tarea_control)
    
    print(f"   Controlador creado - Cooldown: {COOLDOWN_RIEGO}s")
    print("   Observadores registrados")
    
    # Iniciar sistema
    agua_inicial = plantacion.agua_disponible
    duracion = 20
    
    print(f"\n   Iniciando sistema automatizado por {duracion} segundos...")
    print(f"   Agua inicial: {agua_inicial} L")
    
    tarea_temp.start()
    tarea_hum.start()
    
    try:
        time.sleep(duracion)
    except KeyboardInterrupt:
        print("\n   Sistema interrumpido por usuario")
    
    agua_final = plantacion.agua_disponible
    
    # US-013: Detener sistema
    imprimir_us("US-013", "Detener Sistema de Forma Segura")
    
    tarea_temp.stop()
    tarea_hum.stop()
    
    # Esperar cierre limpio usando constante de timeout
    tarea_temp.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_hum.join(timeout=THREAD_JOIN_TIMEOUT)
    
    print("   Sistema detenido correctamente")
    print(f"   Agua final: {agua_final} L")
    print(f"   Agua consumida: {agua_inicial - agua_final} L")


def epic4_gestion_personal(plantacion: Plantacion):
    """
    EPIC 4: GESTION DE PERSONAL
    
    User Stories:
    - US-014: Registrar Trabajador con Tareas
    - US-015: Asignar Apto Medico
    - US-016: Ejecutar Tareas
    - US-017: Asignar Trabajadores a Plantacion
    """
    imprimir_epic(4, "GESTION DE PERSONAL")
    
    trabajador_service = TrabajadorService()
    
    # US-014: Crear trabajador con tareas
    imprimir_us("US-014", "Registrar Trabajador con Tareas")
    
    tareas = [
        Tarea(id_tarea=1, fecha=date.today(), descripcion="Desmalezar", completada=False),
        Tarea(id_tarea=2, fecha=date.today(), descripcion="Abonar", completada=False),
        Tarea(id_tarea=3, fecha=date.today(), descripcion="Marcar surcos", completada=False)
    ]
    
    trabajador = Trabajador(
        dni=43888734,
        nombre="Juan Perez",
        tareas=tareas,
        apto_medico=None
    )
    
    print(f"   Trabajador: {trabajador.nombre} (DNI: {trabajador.dni})")
    print(f"   Tareas asignadas: {len(trabajador.tareas)}")
    
    # US-015: Asignar apto medico
    imprimir_us("US-015", "Asignar Apto Medico")
    
    trabajador_service.asignar_apto_medico(
        trabajador=trabajador,
        apto=True,
        fecha_emision=date.today(),
        observaciones="Estado de salud: excelente"
    )
    
    print(f"   Apto medico asignado")
    print(f"   Fecha: {trabajador.apto_medico.fecha_emision}")
    print(f"   Observaciones: {trabajador.apto_medico.observaciones}")
    
    # US-016: Ejecutar tareas
    imprimir_us("US-016", "Ejecutar Tareas")
    
    herramienta = Herramienta(
        id_herramienta=1,
        nombre="Pala",
        certificado_hys=True
    )
    
    resultado = trabajador_service.trabajar(
        trabajador=trabajador,
        fecha=date.today(),
        util=herramienta
    )
    
    if resultado:
        tareas_completadas = sum(1 for t in trabajador.tareas if t.completada)
        print(f"   Tareas completadas: {tareas_completadas}/{len(trabajador.tareas)}")
    
    # US-017: Asignar a plantacion
    imprimir_us("US-017", "Asignar Trabajadores a Plantacion")
    
    plantacion.trabajadores.append(trabajador)
    print(f"   Trabajadores en plantacion: {len(plantacion.trabajadores)}")


def epic5_operaciones_negocio(registro: RegistroForestal) -> FincasService:
    """
    EPIC 5: OPERACIONES DE NEGOCIO
    
    User Stories:
    - US-018: Gestionar Multiples Fincas
    - US-019: Fumigar Plantacion
    - US-020: Cosechar y Empaquetar (Generics)
    """
    imprimir_epic(5, "OPERACIONES DE NEGOCIO")
    
    # US-018: Crear servicio de fincas
    imprimir_us("US-018", "Gestionar Multiples Fincas")
    
    fincas_service = FincasService()
    fincas_service.add_finca(registro)
    
    print(f"   Fincas registradas: {len(fincas_service._registros)}")
    
    # US-019: Fumigar
    imprimir_us("US-019", "Fumigar Plantacion Completa")
    
    plaguicida = "insecto organico"
    fincas_service.fumigar(
        id_padron=registro.id_padron,
        plaguicida=plaguicida
    )
    
    print(f"   Fumigacion completada con: {plaguicida}")
    
    # US-020: Cosechar y empaquetar (Generics)
    imprimir_us("US-020", "Cosechar y Empaquetar (Generics)")
    
    print("\n   Cosechando Lechugas...")
    caja_lechugas = fincas_service.cosechar_yempaquetar(Lechuga)
    print(f"   Cantidad: {caja_lechugas.get_cantidad()}")
    print(f"   ID Paquete: {caja_lechugas.get_id_paquete()}")
    
    print("\n   Cosechando Pinos...")
    caja_pinos = fincas_service.cosechar_yempaquetar(Pino)
    print(f"   Cantidad: {caja_pinos.get_cantidad()}")
    print(f"   ID Paquete: {caja_pinos.get_id_paquete()}")
    
    return fincas_service


def epic6_persistencia_auditoria(registro: RegistroForestal):
    """
    EPIC 6: PERSISTENCIA Y AUDITORIA
    
    User Stories:
    - US-021: Persistir Registro en Disco (Pickle)
    - US-022: Recuperar Registro desde Disco
    - US-023: Mostrar Datos Completos
    """
    imprimir_epic(6, "PERSISTENCIA Y AUDITORIA")
    
    registro_service = RegistroForestalService()
    
    # US-021: Persistir
    imprimir_us("US-021", "Persistir Registro (Pickle)")
    
    try:
        registro_service.persistir(registro)
        print(f"   Registro guardado: {registro.propietario}")
        print(f"   Archivo: data/{registro.propietario}.dat")
    except PersistenciaException as e:
        print(f"   Error al persistir: {e.get_user_message()}", file=sys.stderr)
    
    # US-022: Recuperar
    imprimir_us("US-022", "Recuperar Registro desde Disco")
    
    registro_leido = None
    try:
        registro_leido = RegistroForestalService.leer_registro(registro.propietario)
        print(f"   Registro recuperado: {registro_leido.propietario}")
        print(f"   Cultivos en registro: {len(registro_leido.plantacion.cultivos)}")
    except PersistenciaException as e:
        print(f"   Error al leer: {e.get_user_message()}", file=sys.stderr)
        registro_leido = registro
    
    # US-023: Mostrar datos completos
    imprimir_us("US-023", "Mostrar Datos Completos")
    
    registro_service.mostrar_datos(registro_leido)
    
    # Validaciones
    print("\n   [VALIDACIONES]")
    
    # Validar PersistenciaException
    try:
        RegistroForestalService.leer_registro("NoExiste")
    except PersistenciaException as e:
        print(f"   ✓ PersistenciaException capturada")
        print(f"     Archivo: {e.get_nombre_archivo()}")
        print(f"     Operacion: {e.get_tipo_operacion()}")
    
    # Validar propietario vacio
    try:
        RegistroForestalService.leer_registro("")
    except ValueError as e:
        print(f"   ✓ ValueError capturada: {e}")


def main():
    """
    Funcion principal que ejecuta todo el sistema.
    Demuestra los 6 EPICs y 23 User Stories organizados.
    """
    try:
        imprimir_encabezado()
        
        # ===================================================================
        # PATRON SINGLETON
        # Todos los servicios obtienen automaticamente la UNICA INSTANCIA
        # del CultivoServiceRegistry usando el patron Singleton.
        # ===================================================================
        imprimir_patron("SINGLETON", 
                       "CultivoServiceRegistry - instancia unica compartida")
        print("   Todos los servicios compartiran el mismo registry\n")
        
        # Epic 1: Gestion de Terrenos
        tierra, plantacion, registro = epic1_gestion_terrenos()
        
        # Epic 2: Gestion de Cultivos (Factory, Strategy, Registry)
        plantacion_service = epic2_gestion_cultivos(plantacion)
        
        # Epic 3: Sistema de Riego Automatizado (Observer)
        epic3_sistema_riego(plantacion, plantacion_service)
        
        # Epic 4: Gestion de Personal
        epic4_gestion_personal(plantacion)
        
        # Epic 5: Operaciones de Negocio
        fincas_service = epic5_operaciones_negocio(registro)
        
        # Epic 6: Persistencia y Auditoria
        epic6_persistencia_auditoria(registro)
        
        # Resumen final
        print("\n" + "=" * 80)
        print("              DEMOSTRACION COMPLETADA EXITOSAMENTE")
        print("=" * 80)
        print("  ✓ SINGLETON   - CultivoServiceRegistry (instancia unica)")
        print("  ✓ FACTORY     - Creacion de cultivos")
        print("  ✓ OBSERVER    - Sistema de sensores y eventos")
        print("  ✓ STRATEGY    - Algoritmos de absorcion de agua")
        print("  ✓ REGISTRY    - Dispatch polimorfico")
        print("=" * 80)
        print("\n  Sistema PythonForestal v1.0.0")
        print("  23 User Stories ejecutadas exitosamente\n")
        
    except SuperficieInsuficienteException as e:
        print(f"\n{e.get_full_message()}", file=sys.stderr)
        print(f"Detalles: {e.get_user_message()}", file=sys.stderr)
        if e.get_superficie_requerida() > 0:
            print(f"  - Requerida: {e.get_superficie_requerida():.2f} m²", file=sys.stderr)
            print(f"  - Disponible: {e.get_superficie_disponible():.2f} m²", file=sys.stderr)
        sys.exit(1)
    
    except AguaAgotadaException as e:
        print(f"\n{e.get_full_message()}", file=sys.stderr)
        print(f"Detalles: {e.get_user_message()}", file=sys.stderr)
        if e.get_agua_requerida() > 0:
            print(f"  - Requerida: {e.get_agua_requerida()} L", file=sys.stderr)
            print(f"  - Disponible: {e.get_agua_disponible()} L", file=sys.stderr)
        sys.exit(1)
    
    except PersistenciaException as e:
        print(f"\n{e.get_full_message()}", file=sys.stderr)
        print(f"Detalles: {e.get_user_message()}", file=sys.stderr)
        print(f"Operacion: {e.get_tipo_operacion()}", file=sys.stderr)
        if e.get_cause():
            print(f"Causa: {str(e.get_cause())}", file=sys.stderr)
        sys.exit(1)
    
    except KeyboardInterrupt:
        print("\n\nOperacion interrumpida por el usuario", file=sys.stderr)
        sys.exit(1)
    
    except ValueError as e:
        print(f"\nError de validacion: {str(e)}", file=sys.stderr)
        sys.exit(1)
    
    except Exception as e:
        print("\nError inesperado del sistema", file=sys.stderr)
        print(f"Mensaje: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()


################################################################################
# DIRECTORIO: .
################################################################################


# ==============================================================================
# ARCHIVO 2/67: __init__.py
# Directorio: .
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/__init__.py
# ==============================================================================

# python_forestacion/__init__.py


# ==============================================================================
# ARCHIVO 3/67: constantes.py
# Directorio: .
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/constantes.py
# ==============================================================================

THREAD_JOIN_TIMEOUT = 2.0
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

# Superficies y agua por tipo
SUPERFICIE_PINO = 2.0
AGUA_INICIAL_PINO = 2
ALTURA_INICIAL_PINO = 1.0

SUPERFICIE_OLIVO = 3.0
AGUA_INICIAL_OLIVO = 5
ALTURA_INICIAL_OLIVO = 0.5

SUPERFICIE_LECHUGA = 0.10
AGUA_INICIAL_LECHUGA = 1

SUPERFICIE_ZANAHORIA = 0.15
AGUA_INICIAL_ZANAHORIA = 0

# Riego
CONSUMO_RIEGO_POR_LLAMADA = 10
TEMP_MIN_RIEGO = 8
TEMP_MAX_RIEGO = 15
HUMEDAD_MAX_RIEGO = 50
INTERVALO_CONTROL_RIEGO = 2.5
COOLDOWN_RIEGO = 3

# Sensores
INTERVALO_SENSOR_TEMPERATURA = 2.0
INTERVALO_SENSOR_HUMEDAD = 3.0
SENSOR_TEMP_MIN = -25
SENSOR_TEMP_MAX = 50
SENSOR_HUMEDAD_MIN = 0
SENSOR_HUMEDAD_MAX = 100

# Absorcion de agua (Strategy Pattern)
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2
MES_INICIO_VERANO = 3  # Marzo (hemisferio sur)
MES_FIN_VERANO = 8  # Agosto

# Crecimiento arboles
CRECIMIENTO_PINO_POR_RIEGO = 0.10
CRECIMIENTO_OLIVO_POR_RIEGO = 0.01


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 4/67: __init__.py
# Directorio: entidades
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/__init__.py
# ==============================================================================

# python_forestacion/entidades/__init__.py
# python_forestacion/entidades/__init__.py



################################################################################
# DIRECTORIO: entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 5/67: __init__.py
# Directorio: entidades/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/__init__.py
# ==============================================================================

# python_forestacion/entidades/cultivos/__init__.py


# ==============================================================================
# ARCHIVO 6/67: arbol.py
# Directorio: entidades/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

# python_forestacion/entidades/cultivos/arbol.py
from dataclasses import dataclass
from python_forestacion.entidades.cultivos.cultivo import Cultivo


@dataclass
class Arbol(Cultivo):
    """
    Clase base para arboles.
    Los arboles tienen altura y pueden crecer.
    """
    altura: float = 1.0
    
    def get_altura(self) -> float:
        return self.altura
    
    def set_altura(self, altura: float) -> None:
        if altura < 0:
            raise ValueError("Altura no puede ser negativa")
        self.altura = altura
    
    def crecer(self, incremento: float) -> None:
        """Incrementa la altura del arbol"""
        self.altura += incremento


# ==============================================================================

# ARCHIVO 7/67: cultivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

# python_forestacion/entidades/cultivos/cultivo.py
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Cultivo:
    id: int
    superficie: float
    agua: int = 0

    def get_agua(self) -> int:
        return self.agua

    def set_agua(self, cantidad: int) -> None:
        if cantidad < 0:
            raise ValueError("Agua no puede ser negativa")
        self.agua = cantidad

    def get_superficie(self) -> float:
        return self.superficie


# ==============================================================================
# ARCHIVO 8/67: hortaliza.py
# Directorio: entidades/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

# python_forestacion/entidades/cultivos/hortaliza.py
from dataclasses import dataclass
from python_forestacion.entidades.cultivos.cultivo import Cultivo


@dataclass
class Hortaliza(Cultivo):
    """
    Clase base para hortalizas.
    Las hortalizas pueden estar en invernadero.
    """
    invernadero: bool = False
    
    def is_invernadero(self) -> bool:
        return self.invernadero
    
    def set_invernadero(self, invernadero: bool) -> None:
        self.invernadero = invernadero


# ==============================================================================
# ARCHIVO 9/67: lechuga.py
# Directorio: entidades/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

# python_forestacion/entidades/cultivos/lechuga.py
from dataclasses import dataclass
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA

@dataclass
class Lechuga(Cultivo):
    variedad: str = "Crespa"
    invernadero: bool = True

    def __post_init__(self):
        if not hasattr(self, "agua") or self.agua is None:
            self.agua = AGUA_INICIAL_LECHUGA


# ==============================================================================
# ARCHIVO 10/67: olivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

# python_forestacion/entidades/cultivos/olivo.py
from dataclasses import dataclass, field
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.constantes import AGUA_INICIAL_OLIVO, ALTURA_INICIAL_OLIVO

@dataclass
class Olivo(Cultivo):
    tipo_aceituna: str = "Arbequina"
    altura: float = field(default=ALTURA_INICIAL_OLIVO)

    def __post_init__(self):
        if not hasattr(self, "agua") or self.agua is None:
            self.agua = AGUA_INICIAL_OLIVO

    def crecer(self, aumento: float) -> None:
        self.altura += aumento


# ==============================================================================
# ARCHIVO 11/67: pino.py
# Directorio: entidades/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

# python_forestacion/entidades/cultivos/pino.py
from dataclasses import dataclass, field
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.constantes import AGUA_INICIAL_PINO, ALTURA_INICIAL_PINO, SUPERFICIE_PINO

@dataclass
class Pino(Cultivo):
    variedad: str = "Parana"
    altura: float = field(default=ALTURA_INICIAL_PINO)

    def __post_init__(self):
        if not hasattr(self, "agua") or self.agua is None:
            self.agua = AGUA_INICIAL_PINO

    def crecer(self, aumento: float) -> None:
        self.altura += aumento


# ==============================================================================
# ARCHIVO 12/67: tipo_aceituna.py
# Directorio: entidades/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

# python_forestacion/entidades/cultivos/tipo_aceituna.py
from enum import Enum


class TipoAceituna(Enum):
    """
    Tipos de aceitunas disponibles para olivos.
    """
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"


# ==============================================================================
# ARCHIVO 13/67: zanahoria.py
# Directorio: entidades/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

# python_forestacion/entidades/cultivos/zanahoria.py
from dataclasses import dataclass
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA

@dataclass
class Zanahoria(Cultivo):
    is_baby: bool = False

    def __post_init__(self):
        if not hasattr(self, "agua") or self.agua is None:
            self.agua = AGUA_INICIAL_ZANAHORIA



################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 14/67: __init__.py
# Directorio: entidades/personal
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/personal/__init__.py
# ==============================================================================

# python_forestacion/entidades/personal/__init__.py


# ==============================================================================
# ARCHIVO 15/67: apto_medico.py
# Directorio: entidades/personal
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

# python_forestacion/entidades/personal/apto_medico.py
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class AptoMedico:
    """
    Representa el apto medico de un trabajador.
    
    Attributes:
        apto: Estado de aptitud (True = apto, False = no apto)
        fecha_emision: Fecha de emision del apto
        observaciones: Observaciones medicas opcionales
    """
    apto: bool
    fecha_emision: date
    observaciones: Optional[str] = None
    
    def esta_apto(self) -> bool:
        return self.apto
    
    def get_fecha_emision(self) -> date:
        return self.fecha_emision
    
    def get_observaciones(self) -> Optional[str]:
        return self.observaciones


# ==============================================================================
# ARCHIVO 16/67: herramienta.py
# Directorio: entidades/personal
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

# python_forestacion/entidades/personal/herramienta.py
from dataclasses import dataclass


@dataclass
class Herramienta:
    """
    Representa una herramienta certificada para uso en tareas agricolas.
    
    Attributes:
        id_herramienta: ID unico de la herramienta
        nombre: Nombre de la herramienta
        certificado_hys: Certificacion de higiene y seguridad
    """
    id_herramienta: int
    nombre: str
    certificado_hys: bool
    
    def get_id_herramienta(self) -> int:
        return self.id_herramienta
    
    def get_nombre(self) -> str:
        return self.nombre
    
    def is_certificado_hys(self) -> bool:
        return self.certificado_hys


# ==============================================================================
# ARCHIVO 17/67: tarea.py
# Directorio: entidades/personal
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

# python_forestacion/entidades/personal/tarea.py
from dataclasses import dataclass
from datetime import date


@dataclass
class Tarea:
    """
    Representa una tarea asignada a un trabajador.
    
    Attributes:
        id_tarea: ID unico de la tarea
        fecha: Fecha programada para la tarea
        descripcion: Descripcion de la tarea
        completada: Estado de la tarea (False = pendiente, True = completada)
    """
    id_tarea: int
    fecha: date
    descripcion: str
    completada: bool = False
    
    def get_id_tarea(self) -> int:
        return self.id_tarea
    
    def get_fecha(self) -> date:
        return self.fecha
    
    def get_descripcion(self) -> str:
        return self.descripcion
    
    def is_completada(self) -> bool:
        return self.completada
    
    def marcar_completada(self) -> None:
        self.completada = True


# ==============================================================================
# ARCHIVO 18/67: trabajador.py
# Directorio: entidades/personal
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

# python_forestacion/entidades/personal/trabajador.py
from dataclasses import dataclass, field
from typing import List, Optional
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico


@dataclass
class Trabajador:
    """
    Representa un trabajador agricola con sus tareas y apto medico.
    
    Attributes:
        dni: DNI unico del trabajador
        nombre: Nombre completo del trabajador
        tareas: Lista de tareas asignadas
        apto_medico: Apto medico del trabajador (opcional)
    """
    dni: int
    nombre: str
    tareas: List[Tarea] = field(default_factory=list)
    apto_medico: Optional[AptoMedico] = None
    
    def get_dni(self) -> int:
        return self.dni
    
    def get_nombre(self) -> str:
        return self.nombre
    
    def get_tareas(self) -> List[Tarea]:
        # Defensive copy
        return self.tareas.copy()
    
    def set_tareas(self, tareas: List[Tarea]) -> None:
        # Defensive copy
        self.tareas = tareas.copy()
    
    def agregar_tarea(self, tarea: Tarea) -> None:
        self.tareas.append(tarea)
    
    def get_apto_medico(self) -> Optional[AptoMedico]:
        return self.apto_medico
    
    def set_apto_medico(self, apto_medico: AptoMedico) -> None:
        self.apto_medico = apto_medico



################################################################################
# DIRECTORIO: entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 19/67: __init__.py
# Directorio: entidades/terrenos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================

# python_forestacion/entidades/terrenos/__init__.py


# ==============================================================================
# ARCHIVO 20/67: plantacion.py
# Directorio: entidades/terrenos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 21/67: registro_forestal.py
# Directorio: entidades/terrenos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

# python_forestacion/entidades/terrenos/registro_forestal.py
from dataclasses import dataclass
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


@dataclass
class RegistroForestal:
    """
    Registro forestal que vincula terreno, plantacion, propietario y avaluo.
    
    Attributes:
        id_padron: ID del padron catastral
        tierra: Terreno asociado
        plantacion: Plantacion asociada
        propietario: Nombre del propietario
        avaluo: Avaluo fiscal del terreno
    """
    id_padron: int
    tierra: Tierra
    plantacion: Plantacion
    propietario: str
    avaluo: float
    
    def get_id_padron(self) -> int:
        return self.id_padron
    
    def get_tierra(self) -> Tierra:
        return self.tierra
    
    def get_plantacion(self) -> Plantacion:
        return self.plantacion
    
    def get_propietario(self) -> str:
        return self.propietario
    
    def get_avaluo(self) -> float:
        return self.avaluo


# ==============================================================================
# ARCHIVO 22/67: tierra.py
# Directorio: entidades/terrenos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

# python_forestacion/entidades/terrenos/tierra.py
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


@dataclass
class Tierra:
    """
    Representa un terreno con su padron catastral y superficie.
    
    Attributes:
        id_padron_catastral: Numero de padron unico
        superficie: Superficie en metros cuadrados
        domicilio: Direccion del terreno
        finca: Plantacion asociada al terreno
    """
    id_padron_catastral: int
    superficie: float
    domicilio: str
    finca: Optional['Plantacion'] = None
    
    def __post_init__(self):
        if self.superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
    
    def get_id_padron_catastral(self) -> int:
        return self.id_padron_catastral
    
    def get_superficie(self) -> float:
        return self.superficie
    
    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self.superficie = superficie
    
    def get_domicilio(self) -> str:
        return self.domicilio
    
    def set_domicilio(self, domicilio: str) -> None:
        self.domicilio = domicilio
    
    def get_finca(self) -> Optional['Plantacion']:
        return self.finca
    
    def set_finca(self, finca: 'Plantacion') -> None:
        self.finca = finca



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 23/67: __init__.py
# Directorio: excepciones
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones/__init__.py
# ==============================================================================

# python_forestacion/excepciones/__init__.py


# ==============================================================================
# ARCHIVO 24/67: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 25/67: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 26/67: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones/mensajes_exception.py
# ==============================================================================

# python_forestacion/excepciones/mensajes_exception.py
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class MensajesException(ForestacionException):
    """
    Excepción para errores relacionados con mensajes y comunicaciones del sistema.
    """
    
    def __init__(self, user_message: str, technical_message: str = None):
        super().__init__(user_message, technical_message or user_message)


# ==============================================================================
# ARCHIVO 27/67: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 28/67: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 29/67: __init__.py
# Directorio: patrones
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/__init__.py
# ==============================================================================

# python_forestacion/patrones/__init__.py



################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 30/67: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/factory/__init__.py
# ==============================================================================

# python_forestacion/patrones/factory/__init__.py


# ==============================================================================
# ARCHIVO 31/67: cultivo_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

# python_forestacion/patrones/factory/cultivo_factory.py
from typing import Callable
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.constantes import SUPERFICIE_PINO, SUPERFICIE_OLIVO, SUPERFICIE_LECHUGA, SUPERFICIE_ZANAHORIA

class CultivoFactory:
    _id_counter = 1

    @staticmethod
    def crear_cultivo(especie: str, **kwargs):
        factories: dict[str, Callable] = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria,
        }
        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")
        return factories[especie](**kwargs)

    @staticmethod
    def _next_id() -> int:
        i = CultivoFactory._id_counter
        CultivoFactory._id_counter += 1
        return i

    @staticmethod
    def _crear_pino(variedad: str = "Parana"):
        return Pino(id=CultivoFactory._next_id(), superficie=SUPERFICIE_PINO, variedad=variedad)

    @staticmethod
    def _crear_olivo(tipo_aceituna: str = "Arbequina"):
        return Olivo(id=CultivoFactory._next_id(), superficie=SUPERFICIE_OLIVO, tipo_aceituna=tipo_aceituna)

    @staticmethod
    def _crear_lechuga(variedad: str = "Crespa", invernadero: bool = True):
        return Lechuga(id=CultivoFactory._next_id(), superficie=SUPERFICIE_LECHUGA, variedad=variedad, invernadero=invernadero)

    @staticmethod
    def _crear_zanahoria(is_baby: bool = False):
        return Zanahoria(id=CultivoFactory._next_id(), superficie=SUPERFICIE_ZANAHORIA, is_baby=is_baby)



################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 32/67: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/__init__.py
# ==============================================================================

# python_forestacion/patrones/observer/__init__.py


# ==============================================================================
# ARCHIVO 33/67: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/observable.py
# ==============================================================================

# python_forestacion/patrones/observer/observable.py
from typing import Generic, TypeVar, List
from threading import Lock
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar("T")

class Observable(Generic[T]):
    def __init__(self):
        self._observadores: List[Observer[T]] = []
        self._lock = Lock()

    def agregar_observador(self, observador: Observer[T]) -> None:
        with self._lock:
            if observador not in self._observadores:
                self._observadores.append(observador)

    def quitar_observador(self, observador: Observer[T]) -> None:
        with self._lock:
            if observador in self._observadores:
                self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        # copia para evitar modificaciones concurrentes
        with self._lock:
            observadores = list(self._observadores)
        for obs in observadores:
            try:
                obs.actualizar(evento)
            except Exception:
                # no romper el ciclo si un observador falla
                pass


# ==============================================================================
# ARCHIVO 34/67: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/observer.py
# ==============================================================================

# python_forestacion/patrones/observer/observer.py
from typing import Generic, TypeVar, Protocol

T = TypeVar("T")

class Observer(Protocol[T]):
    def actualizar(self, evento: T) -> None:
        ...



################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 35/67: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/eventos/__init__.py
# ==============================================================================

# python_forestacion/patrones/observer/eventos/__init__.py


# ==============================================================================
# ARCHIVO 36/67: evento_plantacion.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ==============================================================================

# python_forestacion/patrones/observer/eventos/evento_plantacion.py
from dataclasses import dataclass
from typing import Optional


@dataclass
class EventoPlantacion:
    """
    Evento relacionado con operaciones de plantacion.
    Puede ser usado para notificar plantacion, riego, fumigacion, etc.
    """
    tipo: str  # "PLANTACION", "RIEGO", "FUMIGACION", etc.
    descripcion: str
    cantidad: Optional[int] = None
    superficie: Optional[float] = None


# ==============================================================================
# ARCHIVO 37/67: evento_sensor.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ==============================================================================

# python_forestacion/patrones/observer/eventos/evento_sensor.py
from dataclasses import dataclass
from datetime import datetime


@dataclass
class EventoSensor:
    """
    Evento generado por un sensor.
    Contiene el valor leido y metadata adicional.
    """
    tipo_sensor: str  # "TEMPERATURA" o "HUMEDAD"
    valor: float
    timestamp: datetime
    unidad: str  # "°C" o "%"



################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 38/67: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/singleton/__init__.py
# ==============================================================================

# python_forestacion/patrones/singleton/__init__.py



################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 39/67: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/strategy/__init__.py
# ==============================================================================

# python_forestacion/patrones/strategy/__init__.py


# ==============================================================================
# ARCHIVO 40/67: absorcion_agua_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

# python_forestacion/patrones/strategy/absorcion_agua_strategy.py
from abc import ABC, abstractmethod
from datetime import date

class AbsorcionAguaStrategy(ABC):
    @abstractmethod
    def calcular_absorcion(self, fecha: date, temperatura: float, humedad: float, cultivo) -> int:
        ...



################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 41/67: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================

# python_forestacion/patrones/strategy/impl/__init__.py


# ==============================================================================
# ARCHIVO 42/67: absorcion_constante_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================

# python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion constante para hortalizas.
    Absorbe siempre la misma cantidad independiente de la temporada.
    Lechuga: 1L
    Zanahoria: 2L
    """
    
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, fecha: date, temperatura: float, humedad: float, cultivo) -> int:
        return self._cantidad


# ==============================================================================
# ARCHIVO 43/67: absorcion_seasonal_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================

# python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
    MES_INICIO_VERANO,
    MES_FIN_VERANO
)

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion estacional para arboles.
    Verano (marzo-agosto): 5L
    Invierno (septiembre-febrero): 2L
    """
    
    def calcular_absorcion(self, fecha: date, temperatura: float, humedad: float, cultivo) -> int:
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        return ABSORCION_SEASONAL_INVIERNO



################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 44/67: __init__.py
# Directorio: riego
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/__init__.py
# ==============================================================================

# python_forestacion/riego/__init__.py



################################################################################
# DIRECTORIO: riego/control
################################################################################

# ==============================================================================
# ARCHIVO 45/67: __init__.py
# Directorio: riego/control
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/control/__init__.py
# ==============================================================================

# python_forestacion/riego/control/__init__.py


# ==============================================================================
# ARCHIVO 46/67: control_riego_task.py
# Directorio: riego/control
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

# python_forestacion/riego/control/control_riego_task.py
import threading
import time
from datetime import datetime, timedelta
from typing import Any
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.constantes import TEMP_MIN_RIEGO, TEMP_MAX_RIEGO, HUMEDAD_MAX_RIEGO

class ControlRiegoTask(Observer[Any]):
    """
    Observador que recibe lecturas de sensores (temperatura y humedad).
    Cuando las condiciones de riego se cumplen llama a PlantacionService.regar(plantacion).
    Uso:
      control = ControlRiegoTask(plantacion)
      temp_sensor.agregar_observador(control)
      hum_sensor.agregar_observador(control)
    """

    def __init__(self, plantacion, cooldown_seconds: int = 60):
        # plantacion: instancia de Plantacion (donde se realizan los riegos)
        self.plantacion = plantacion
        self._plantation_service = PlantacionService()
        self._lock = threading.Lock()
        self._last_temp: float | None = None
        self._last_hum: float | None = None
        self._last_riego_time: datetime | None = None
        self.cooldown = timedelta(seconds=cooldown_seconds)

    def actualizar(self, evento: Any) -> None:
        """
        Este método es llamado por los sensores.
        El evento puede ser temperatura (float) o humedad (float).
        Distinguir por rango: temperatura típicamente -50..+60, humedad 0..100.
        """
        try:
            val = float(evento)
        except Exception:
            return

      
        if 0.0 <= val <= 100.0:
            # posible humedad o temperatura; preferimos tratar como humedad si ya tenemos temperatura reciente
            # política simple:
            if self._last_temp is None:
                # asumimos que es temperatura (si no hay temp previa)
                self._last_temp = val
            else:
                self._last_hum = val
        else:
            # temperatura fuera de 0..100 -> temperatura
            self._last_temp = val

        # mejor enfoque: ejecutar evaluación cuando tengamos ambos valores
        if self._last_temp is not None and self._last_hum is not None:
            self._evaluar_y_regar(self._last_temp, self._last_hum)
            # reset simple para siguiente ciclo
            self._last_temp = None
            self._last_hum = None

    def _puede_regar(self) -> bool:
        if self._last_riego_time is None:
            return True
        return datetime.now() - self._last_riego_time >= self.cooldown

    def _evaluar_y_regar(self, temperatura: float, humedad: float):
        """
        Lógica de decisión:
         - temperatura dentro de [TEMP_MIN_RIEGO, TEMP_MAX_RIEGO]
         - humedad <= HUMEDAD_MAX_RIEGO
         - y cooldown respetado
        """
        with self._lock:
            if not self._puede_regar():
                return

            condiciones_temp = TEMP_MIN_RIEGO <= temperatura <= TEMP_MAX_RIEGO
            condiciones_hum = humedad <= HUMEDAD_MAX_RIEGO

            if condiciones_temp and condiciones_hum:
                try:
                    # llamar al servicio de plantacion
                    resultados = self._plantation_service.regar(self.plantacion, temperatura=temperatura, humedad=humedad)
                    self._last_riego_time = datetime.now()
                    # opcional: imprimir resumen
                    print(f"[{datetime.now().isoformat()}] Riego ejecutado. Temperatura={temperatura}, Humedad={humedad}")
                    for cultivo, amt in resultados:
                        print(f"  - ID {cultivo.id} absorbió {amt} L")
                    print(f"  Agua restante en plantacion: {self.plantacion.agua_disponible} L")
                except Exception as e:
                    print(f"[{datetime.now().isoformat()}] Error al regar: {e}")
            else:
                # condiciones no cumplidas; solo log para debug
                print(f"[{datetime.now().isoformat()}] No riega: Temp={temperatura} (req {TEMP_MIN_RIEGO}-{TEMP_MAX_RIEGO}), Hum={humedad} (req <={HUMEDAD_MAX_RIEGO})")



################################################################################
# DIRECTORIO: riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 47/67: __init__.py
# Directorio: riego/sensores
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/sensores/__init__.py
# ==============================================================================

# python_forestacion/riego/sensores/__init__.py
# python_forestacion/riego/sensores/__init__.py

from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask

__all__ = ['TemperaturaReaderTask', 'HumedadReaderTask']


# ==============================================================================
# ARCHIVO 48/67: humedad_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

# python_forestacion/riego/sensores/humedad_reader_task.py
import threading
import time
import random
from typing import Optional
from python_forestacion.patrones.observer.observable import Observable

class HumedadReaderTask(Observable[float], threading.Thread):
    """
    Sensor simulado de humedad (%).
    Notifica valores 0..100 cada intervalo (segundos).
    """
    def __init__(self, intervalo: float = 5.0, min_hum: float = 0.0, max_hum: float = 100.0):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self.intervalo = intervalo
        self._stop_event = threading.Event()
        self.min_hum = min_hum
        self.max_hum = max_hum

    def run(self):
        while not self._stop_event.is_set():
            hum = round(random.uniform(self.min_hum, self.max_hum), 2)
            self.notificar_observadores(hum)
            time.sleep(self.intervalo)

    def stop(self):
        self._stop_event.set()


# ==============================================================================
# ARCHIVO 49/67: temperatura_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

# python_forestacion/riego/sensores/temperatura_reader_task.py
import threading
import time
import random
from typing import Optional
from python_forestacion.patrones.observer.observable import Observable

class TemperaturaReaderTask(Observable[float], threading.Thread):
    """
    Sensor simulado de temperatura.
    Hereda de Observable[float] y de Thread.
    Notifica la temperatura como float a sus observadores cada intervalo (segundos).
    """
    def __init__(self, intervalo: float = 5.0, min_temp: float = 0.0, max_temp: float = 40.0):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self.intervalo = intervalo
        self._stop_event = threading.Event()
        self.min_temp = min_temp
        self.max_temp = max_temp

    def run(self):
        while not self._stop_event.is_set():
            # Aquí se simula la lectura; en integración real reemplazar por lectura del sensor
            temp = round(random.uniform(self.min_temp, self.max_temp), 2)
            # notificar a observadores
            self.notificar_observadores(temp)
            time.sleep(self.intervalo)

    def stop(self):
        self._stop_event.set()



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 50/67: __init__.py
# Directorio: servicios
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/__init__.py
# ==============================================================================

# python_forestacion/servicios/__init__.py



################################################################################
# DIRECTORIO: servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 51/67: __init__.py
# Directorio: servicios/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================

# python_forestacion/servicios/cultivos/__init__.py


# ==============================================================================
# ARCHIVO 52/67: arbol_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 53/67: cultivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

# python_forestacion/servicios/cultivos/cultivo_service.py
from datetime import date
from typing import Optional
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class CultivoService:
    def __init__(self, estrategia: AbsorcionAguaStrategy):
        self._estrategia = estrategia

    def absorver_agua(self, cultivo, fecha: date, temperatura: float, humedad: float) -> int:
        cantidad = self._estrategia.calcular_absorcion(fecha, temperatura, humedad, cultivo)
        cultivo.set_agua(cultivo.get_agua() + cantidad)
        # comportamiento por tipo (ej.: crecimiento) será delegado por servicios concretos si corresponde
        return cantidad


# ==============================================================================
# ARCHIVO 54/67: cultivo_service_registry.py
# Directorio: servicios/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

# python_forestacion/servicios/cultivos/cultivo_service_registry.py
from threading import Lock
from typing import Dict, Type, Callable
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class CultivoServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_internal()
        return cls._instance

    def _init_internal(self):
        # diccionarios de dispatch por tipo
        self._absorber_agua_handlers: Dict[Type, Callable] = {}
        self._mostrar_datos_handlers: Dict[Type, Callable] = {}
        # registrar handlers por defecto
        self._pino_service = CultivoService(AbsorcionSeasonalStrategy())
        self._olivo_service = CultivoService(AbsorcionSeasonalStrategy())
        self._lechuga_service = CultivoService(AbsorcionConstanteStrategy(1))
        self._zanahoria_service = CultivoService(AbsorcionConstanteStrategy(2))

        self.register_handler(Pino, self._pino_service)
        self.register_handler(Olivo, self._olivo_service)
        self.register_handler(Lechuga, self._lechuga_service)
        self.register_handler(Zanahoria, self._zanahoria_service)

    @classmethod
    def get_instance(cls):
        return cls()

    def register_handler(self, tipo: Type, service: CultivoService):
        self._absorber_agua_handlers[tipo] = service

    def absorber_agua(self, cultivo, fecha, temperatura, humedad) -> int:
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo no registrado: {tipo}")
        service: CultivoService = self._absorber_agua_handlers[tipo]
        return service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def mostrar_datos(self, cultivo):
        # Implementación simple de muestra por tipo (puedes ampliar)
        tipo = type(cultivo)
        if tipo == Pino:
            print(f"Cultivo: Pino\nSuperficie: {cultivo.superficie} m²\nAgua: {cultivo.agua} L\nID: {cultivo.id}\nAltura: {cultivo.altura} m\nVariedad: {cultivo.variedad}")
        elif tipo == Olivo:
            print(f"Cultivo: Olivo\nSuperficie: {cultivo.superficie} m²\nAgua: {cultivo.agua} L\nID: {cultivo.id}\nAltura: {cultivo.altura} m\nTipo aceituna: {cultivo.tipo_aceituna}")
        elif tipo == Lechuga:
            print(f"Cultivo: Lechuga\nSuperficie: {cultivo.superficie} m²\nAgua: {cultivo.agua} L\nID: {cultivo.id}\nVariedad: {cultivo.variedad}\nInvernadero: {cultivo.invernadero}")
        elif tipo == Zanahoria:
            print(f"Cultivo: Zanahoria\nSuperficie: {cultivo.superficie} m²\nAgua: {cultivo.agua} L\nID: {cultivo.id}\nIs baby: {cultivo.is_baby}")
        else:
            raise ValueError("Tipo desconocido para mostrar_datos")


# ==============================================================================
# ARCHIVO 55/67: lechuga_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 56/67: olivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 57/67: pino_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================

# python_forestacion/servicios/cultivos/pino_service.py
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy


class PinoService(ArbolService):
    """
    Servicio especifico para gestion de pinos.
    Usa absorcion estacional (Strategy Pattern).
    """
    
    def __init__(self):
        # Inyectar estrategia estacional para arboles
        super().__init__(AbsorcionSeasonalStrategy())


# ==============================================================================
# ARCHIVO 58/67: zanahoria_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 59/67: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/negocio/__init__.py
# ==============================================================================

# python_forestacion/servicios/negocio/__init__.py


# ==============================================================================
# ARCHIVO 60/67: fincas_service.py
# Directorio: servicios/negocio
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/negocio/fincas_service.py
# ==============================================================================

# python_forestacion/servicios/negocio/fincas_service.py
from typing import Dict, Type, TypeVar
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.negocio.paquete import Paquete

T = TypeVar('T', bound=Cultivo)


class FincasService:
    """
    Servicio para gestion de multiples fincas.
    Proporciona operaciones de alto nivel como fumigacion y cosecha.
    """
    
    def __init__(self):
        self._registros: Dict[int, RegistroForestal] = {}
    
    def add_finca(self, registro: RegistroForestal) -> None:
        """
        Agrega una finca al servicio.
        
        Args:
            registro: Registro forestal de la finca
        """
        self._registros[registro.get_id_padron()] = registro
    
    def buscar_finca(self, id_padron: int) -> RegistroForestal:
        """
        Busca una finca por su ID de padron.
        
        Args:
            id_padron: ID del padron catastral
            
        Returns:
            RegistroForestal: Registro de la finca
            
        Raises:
            KeyError: Si no existe finca con ese padron
        """
        if id_padron not in self._registros:
            raise KeyError(f"No existe finca con padron {id_padron}")
        return self._registros[id_padron]
    
    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """
        Fumiga todos los cultivos de una finca.
        
        Args:
            id_padron: ID del padron de la finca a fumigar
            plaguicida: Tipo de plaguicida a aplicar
        """
        registro = self.buscar_finca(id_padron)
        print(f"Fumigando plantacion con: {plaguicida}")
        # En una implementacion real, aqui se aplicaria el plaguicida a cada cultivo
    
    def cosechar_yempaquetar(self, tipo_cultivo: Type[T]) -> Paquete[T]:
        """
        Cosecha todos los cultivos de un tipo especifico de todas las fincas
        y los empaqueta en un Paquete generico tipo-seguro.
        
        Args:
            tipo_cultivo: Clase del tipo de cultivo a cosechar
            
        Returns:
            Paquete[T]: Paquete con los cultivos cosechados
        """
        paquete: Paquete[T] = Paquete()
        
        for registro in self._registros.values():
            plantacion = registro.get_plantacion()
            cultivos_a_cosechar = [
                c for c in plantacion.cultivos
                if isinstance(c, tipo_cultivo)
            ]
            
            # Remover de la plantacion y agregar al paquete
            for cultivo in cultivos_a_cosechar:
                plantacion.cultivos.remove(cultivo)
                paquete.agregar_item(cultivo)
        
        cantidad = paquete.get_cantidad()
        print(f"\nCOSECHANDO {cantidad} unidades de {tipo_cultivo}")
        
        return paquete


# ==============================================================================
# ARCHIVO 61/67: paquete.py
# Directorio: servicios/negocio
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/negocio/paquete.py
# ==============================================================================

# python_forestacion/servicios/negocio/paquete.py
from typing import Generic, TypeVar, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """
    Paquete generico tipo-seguro para empaquetar cultivos cosechados.
    Usa Generics para garantizar type-safety.
    
    Type Parameters:
        T: Tipo de cultivo en el paquete
    
    Attributes:
        items: Lista de cultivos del mismo tipo
        id_paquete: ID unico del paquete
    """
    
    _counter = 0
    
    def __init__(self):
        Paquete._counter += 1
        self.id_paquete = Paquete._counter
        self.items: List[T] = []
    
    def agregar_item(self, item: T) -> None:
        """Agrega un cultivo al paquete"""
        self.items.append(item)
    
    def get_items(self) -> List[T]:
        """Retorna lista de cultivos en el paquete"""
        return self.items.copy()
    
    def get_cantidad(self) -> int:
        """Retorna cantidad de cultivos en el paquete"""
        return len(self.items)
    
    def get_id_paquete(self) -> int:
        """Retorna ID del paquete"""
        return self.id_paquete
    
    def mostrar_contenido_caja(self) -> None:
        """Muestra el contenido del paquete de forma detallada"""
        if not self.items:
            print("\nContenido de la caja:")
            print("  Caja vacia")
            return
        
        tipo_nombre = self.items[0].__class__.__name__
        print(f"\nContenido de la caja:")
        print(f"  Tipo: {tipo_nombre}")
        print(f"  Cantidad: {self.get_cantidad()}")
        print(f"  ID Paquete: {self.id_paquete}")



################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 62/67: __init__.py
# Directorio: servicios/personal
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/personal/__init__.py
# ==============================================================================

# python_forestacion/servicios/personal/__init__.py


# ==============================================================================
# ARCHIVO 63/67: trabajador_service.py
# Directorio: servicios/personal
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 64/67: __init__.py
# Directorio: servicios/terrenos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================

# python_forestacion/servicios/terrenos/__init__.py


# ==============================================================================
# ARCHIVO 65/67: plantacion_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 66/67: registro_forestal_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 67/67: tierra_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

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



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 67
# Generado: 2025-10-21 22:24:05
################################################################################
