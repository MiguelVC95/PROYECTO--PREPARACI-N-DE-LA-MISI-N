# ============================================================
# Archivo:      ejercicio5_destino.py
# Curso:        SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes:  Sharon Avila M, Miguel Vargas, Marcela Otarola# Fecha:        19/10/2026            Versión: 1.0
# Descripción:  Selecciona el destino de la misión mediante una
#               condicional múltiple y autoriza el lanzamiento
#               con una condicional anidada comparando los cuatro
#               recursos disponibles contra los requeridos.
# ============================================================

# --- Constantes de consumo diario ---
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1

# --- Constantes de reserva ---
RESERVA_COMBUSTIBLE = 10
RESERVA_OXIGENO = 5
RESERVA_ENERGIA = 10
RESERVA_PROVISIONES = 3

# --- Entrada de datos ---
nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
opcion_destino = int(input("Seleccione el destino (1: Luna, 2: Marte, 3: Europa): "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# --- Determinación del destino mediante condicional múltiple (match-case) ---
match opcion_destino:
    case 1:
        destino = "Luna"
        dias_viaje = 3
    case 2:
        destino = "Marte"
        dias_viaje = 5
    case 3:
        destino = "Europa"
        dias_viaje = 7
    case _:
        destino = ""
        dias_viaje = 0

# --- Procesamiento y salida ---
if dias_viaje == 0:
    # Opción no válida: terminar sin calcular
    print("Opción de destino no válida. La misión no puede planificarse.")
else:
    # --- Cálculo de recursos requeridos (fórmulas del Avance 1) ---
    combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
    combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
    combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
    oxigeno_requerido = dias_viaje * tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA + RESERVA_OXIGENO
    energia_requerida = dias_viaje * CONSUMO_ENERGIA_DIA + RESERVA_ENERGIA
    provisiones_requeridas = dias_viaje * tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA + RESERVA_PROVISIONES

    # --- Condicional anidada: autorización del lanzamiento ---
    if (combustible >= combustible_total
        and oxigeno >= oxigeno_requerido
        and energia >= energia_requerida
        and provisiones >= provisiones_requeridas):
        estado_lanzamiento = "Lanzamiento autorizado."
    else:
        estado_lanzamiento = "Lanzamiento no autorizado. La misión debe ser revisada."

    # --- Resumen de la misión ---
    print("\n========== RESUMEN DE LA MISIÓN ==========")
    print("Misión:", nombre_mision)
    print("Destino:", destino)
    print("Tripulantes:", tripulantes)
    print("Duración del viaje de ida:", dias_viaje, "días")
    print("Combustible para llegar:", combustible_ida, "unidades")
    print("Combustible para regresar:", combustible_regreso, "unidades")
    print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
    print("Combustible total requerido:", combustible_total, "unidades")
    print("Oxígeno requerido:", oxigeno_requerido, "unidades")
    print("Energía requerida:", energia_requerida, "unidades")
    print("Provisiones requeridas:", provisiones_requeridas, "unidades")
    print(estado_lanzamiento)