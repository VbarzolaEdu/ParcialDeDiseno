
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
    # El CultivoServiceRegistry permite dispatch polimorfico
    # para mostrar datos especificos de cada tipo de cultivo.
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
    # Los sensores actuan como Observables que emiten eventos.
    # El controlador se registra como Observer y reacciona
    # automaticamente a los cambios en las lecturas.
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

"""
Script para buscar el paquete python_forestacion desde el directorio raiz del proyecto.
Incluye funcionalidad para integrar archivos Python en cada nivel del arbol de directorios.
"""
import os
import sys
from datetime import datetime


def buscar_paquete(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python en el directorio raiz y subdirectorios.

    Args:
        directorio_raiz: Directorio desde donde iniciar la busqueda
        nombre_paquete: Nombre del paquete a buscar

    Returns:
        Lista de rutas donde se encontro el paquete
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        # Verificar si el directorio actual es el paquete buscado
        nombre_dir = os.path.basename(raiz)

        if nombre_dir == nombre_paquete:
            # Verificar que sea un paquete Python (contiene __init__.py)
            if '__init__.py' in archivos:
                paquetes_encontrados.append(raiz)
                print(f"[+] Paquete encontrado: {raiz}")
            else:
                print(f"[!] Directorio encontrado pero no es un paquete Python: {raiz}")

    return paquetes_encontrados


def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursion).

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de archivos .py
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa) and item.endswith('.py'):
                # Excluir archivos integradores para evitar recursion infinita
                if item not in ['integrador.py', 'integradorFinal.py']:
                    archivos_python.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(archivos_python)


def obtener_subdirectorios(directorio: str) -> list:
    """
    Obtiene todos los subdirectorios inmediatos de un directorio.

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de subdirectorios
    """
    subdirectorios = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isdir(ruta_completa):
                # Excluir directorios especiales
                if not item.startswith('.') and item not in ['__pycache__', 'venv', '.venv']:
                    subdirectorios.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(subdirectorios)


def leer_contenido_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python.

    Args:
        ruta_archivo: Ruta completa del archivo

    Returns:
        Contenido del archivo como string
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as error:
        print(f"[!] Error al leer {ruta_archivo}: {error}")
        return f"# Error al leer este archivo: {error}\n"


def crear_archivo_integrador(directorio: str, archivos_python: list) -> bool:
    """
    Crea un archivo integrador.py con el contenido de todos los archivos Python.

    Args:
        directorio: Directorio donde crear el archivo integrador
        archivos_python: Lista de rutas de archivos Python a integrar

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_python:
        return False

    ruta_integrador = os.path.join(directorio, 'integrador.py')

    try:
        with open(ruta_integrador, 'w', encoding='utf-8') as integrador:
            # Encabezado
            integrador.write('"""\n')
            integrador.write(f"Archivo integrador generado automaticamente\n")
            integrador.write(f"Directorio: {directorio}\n")
            integrador.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador.write(f"Total de archivos integrados: {len(archivos_python)}\n")
            integrador.write('"""\n\n')

            # Integrar cada archivo
            for idx, archivo in enumerate(archivos_python, 1):
                nombre_archivo = os.path.basename(archivo)
                integrador.write(f"# {'=' * 80}\n")
                integrador.write(f"# ARCHIVO {idx}/{len(archivos_python)}: {nombre_archivo}\n")
                integrador.write(f"# Ruta: {archivo}\n")
                integrador.write(f"# {'=' * 80}\n\n")

                contenido = leer_contenido_archivo(archivo)
                integrador.write(contenido)
                integrador.write("\n\n")

        print(f"[OK] Integrador creado: {ruta_integrador}")
        print(f"     Archivos integrados: {len(archivos_python)}")
        return True

    except Exception as error:
        print(f"[!] Error al crear integrador en {directorio}: {error}")
        return False


def procesar_directorio_recursivo(directorio: str, nivel: int = 0, archivos_totales: list = None) -> list:
    """
    Procesa un directorio de forma recursiva, creando integradores en cada nivel.
    Utiliza DFS (Depth-First Search) para llegar primero a los niveles mas profundos.

    Args:
        directorio: Directorio a procesar
        nivel: Nivel de profundidad actual (para logging)
        archivos_totales: Lista acumulativa de todos los archivos procesados

    Returns:
        Lista de todos los archivos Python procesados en el arbol
    """
    if archivos_totales is None:
        archivos_totales = []

    indentacion = "  " * nivel
    print(f"{indentacion}[INFO] Procesando nivel {nivel}: {os.path.basename(directorio)}")

    # Obtener subdirectorios
    subdirectorios = obtener_subdirectorios(directorio)

    # Primero, procesar recursivamente todos los subdirectorios (DFS)
    for subdir in subdirectorios:
        procesar_directorio_recursivo(subdir, nivel + 1, archivos_totales)

    # Despues de procesar subdirectorios, procesar archivos del nivel actual
    archivos_python = obtener_archivos_python(directorio)

    if archivos_python:
        print(f"{indentacion}[+] Encontrados {len(archivos_python)} archivo(s) Python")
        crear_archivo_integrador(directorio, archivos_python)
        # Agregar archivos a la lista total
        archivos_totales.extend(archivos_python)
    else:
        print(f"{indentacion}[INFO] No hay archivos Python en este nivel")

    return archivos_totales


def crear_integrador_final(directorio_raiz: str, archivos_totales: list) -> bool:
    """
    Crea un archivo integradorFinal.py con TODO el codigo fuente de todas las ramas.

    Args:
        directorio_raiz: Directorio donde crear el archivo integrador final
        archivos_totales: Lista completa de todos los archivos Python procesados

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_totales:
        print("[!] No hay archivos para crear el integrador final")
        return False

    ruta_integrador_final = os.path.join(directorio_raiz, 'integradorFinal.py')

    # Organizar archivos por directorio para mejor estructura
    archivos_por_directorio = {}
    for archivo in archivos_totales:
        directorio = os.path.dirname(archivo)
        if directorio not in archivos_por_directorio:
            archivos_por_directorio[directorio] = []
        archivos_por_directorio[directorio].append(archivo)

    try:
        with open(ruta_integrador_final, 'w', encoding='utf-8') as integrador_final:
            # Encabezado principal
            integrador_final.write('"""\n')
            integrador_final.write("INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write(f"Directorio raiz: {directorio_raiz}\n")
            integrador_final.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write(f"Total de archivos integrados: {len(archivos_totales)}\n")
            integrador_final.write(f"Total de directorios procesados: {len(archivos_por_directorio)}\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write('"""\n\n')

            # Tabla de contenidos
            integrador_final.write("# " + "=" * 78 + "\n")
            integrador_final.write("# TABLA DE CONTENIDOS\n")
            integrador_final.write("# " + "=" * 78 + "\n\n")

            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)
                    integrador_final.write(f"#   {contador_global}. {nombre_archivo}\n")
                    contador_global += 1
                integrador_final.write("#\n")

            integrador_final.write("\n\n")

            # Contenido completo organizado por directorio
            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)

                # Separador de directorio
                integrador_final.write("\n" + "#" * 80 + "\n")
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                integrador_final.write("#" * 80 + "\n\n")

                # Procesar cada archivo del directorio
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)

                    integrador_final.write(f"# {'=' * 78}\n")
                    integrador_final.write(f"# ARCHIVO {contador_global}/{len(archivos_totales)}: {nombre_archivo}\n")
                    integrador_final.write(f"# Directorio: {dir_relativo}\n")
                    integrador_final.write(f"# Ruta completa: {archivo}\n")
                    integrador_final.write(f"# {'=' * 78}\n\n")

                    contenido = leer_contenido_archivo(archivo)
                    integrador_final.write(contenido)
                    integrador_final.write("\n\n")

                    contador_global += 1

            # Footer
            integrador_final.write("\n" + "#" * 80 + "\n")
            integrador_final.write("# FIN DEL INTEGRADOR FINAL\n")
            integrador_final.write(f"# Total de archivos: {len(archivos_totales)}\n")
            integrador_final.write(f"# Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write("#" * 80 + "\n")

        print(f"\n[OK] Integrador final creado: {ruta_integrador_final}")
        print(f"     Total de archivos integrados: {len(archivos_totales)}")
        print(f"     Total de directorios procesados: {len(archivos_por_directorio)}")

        # Mostrar tamanio del archivo
        tamanio = os.path.getsize(ruta_integrador_final)
        if tamanio < 1024:
            tamanio_str = f"{tamanio} bytes"
        elif tamanio < 1024 * 1024:
            tamanio_str = f"{tamanio / 1024:.2f} KB"
        else:
            tamanio_str = f"{tamanio / (1024 * 1024):.2f} MB"
        print(f"     Tamanio del archivo: {tamanio_str}")

        return True

    except Exception as error:
        print(f"[!] Error al crear integrador final: {error}")
        return False


def integrar_arbol_directorios(directorio_raiz: str) -> None:
    """
    Inicia el proceso de integracion para todo el arbol de directorios.

    Args:
        directorio_raiz: Directorio raiz desde donde comenzar
    """
    print("\n" + "=" * 80)
    print("INICIANDO INTEGRACION DE ARCHIVOS PYTHON")
    print("=" * 80)
    print(f"Directorio raiz: {directorio_raiz}\n")

    # Procesar directorios y obtener lista de todos los archivos
    archivos_totales = procesar_directorio_recursivo(directorio_raiz)

    print("\n" + "=" * 80)
    print("INTEGRACION POR NIVELES COMPLETADA")
    print("=" * 80)

    # Crear integrador final con todos los archivos
    if archivos_totales:
        print("\n" + "=" * 80)
        print("CREANDO INTEGRADOR FINAL")
        print("=" * 80)
        crear_integrador_final(directorio_raiz, archivos_totales)

    print("\n" + "=" * 80)
    print("PROCESO COMPLETO FINALIZADO")
    print("=" * 80)


def main():
    """Funcion principal del script."""
    # Obtener el directorio raiz del proyecto (donde esta este script)
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))

    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando == "integrar":
            # Modo de integracion de archivos
            if len(sys.argv) > 2:
                directorio_objetivo = sys.argv[2]
                if not os.path.isabs(directorio_objetivo):
                    directorio_objetivo = os.path.join(directorio_raiz, directorio_objetivo)
            else:
                directorio_objetivo = directorio_raiz

            if not os.path.isdir(directorio_objetivo):
                print(f"[!] El directorio no existe: {directorio_objetivo}")
                return 1

            integrar_arbol_directorios(directorio_objetivo)
            return 0

        elif comando == "help" or comando == "--help" or comando == "-h":
            print("Uso: python buscar_paquete.py [COMANDO] [OPCIONES]")
            print("")
            print("Comandos disponibles:")
            print("  (sin argumentos)     Busca el paquete python_forestacion")
            print("  integrar [DIR]       Integra archivos Python en el arbol de directorios")
            print("                       DIR: directorio raiz (por defecto: directorio actual)")
            print("  help                 Muestra esta ayuda")
            print("")
            print("Ejemplos:")
            print("  python buscar_paquete.py")
            print("  python buscar_paquete.py integrar")
            print("  python buscar_paquete.py integrar python_forestacion")
            return 0

        else:
            print(f"[!] Comando desconocido: {comando}")
            print("    Use 'python buscar_paquete.py help' para ver los comandos disponibles")
            return 1

    # Modo por defecto: buscar paquete
    print(f"[INFO] Buscando desde: {directorio_raiz}")
    print(f"[INFO] Buscando paquete: python_forestacion")
    print("")

    # Buscar el paquete
    paquetes = buscar_paquete(directorio_raiz, "python_forestacion")

    print("")
    if paquetes:
        print(f"[OK] Se encontraron {len(paquetes)} paquete(s):")
        for paquete in paquetes:
            print(f"  - {paquete}")

            # Mostrar estructura basica del paquete
            print(f"    Contenido:")
            try:
                contenido = os.listdir(paquete)
                for item in sorted(contenido)[:10]:  # Mostrar primeros 10 items
                    ruta_item = os.path.join(paquete, item)
                    if os.path.isdir(ruta_item):
                        print(f"      [DIR]  {item}")
                    else:
                        print(f"      [FILE] {item}")
                if len(contenido) > 10:
                    print(f"      ... y {len(contenido) - 10} items mas")
            except PermissionError:
                print(f"      [!] Sin permisos para leer el directorio")
    else:
        print("[!] No se encontro el paquete python_forestacion")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())