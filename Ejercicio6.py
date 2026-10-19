# ============================================================
# Archivo:      ejercicio6_viaje.py
# Curso:        SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes:  Sharon Avila M, Miguel Vargas, Marcela Otarola
# Fecha:        19/10/2026            Versión: 1.0
# Descripción:  Simula día a día el viaje hacia el destino,
#               descontando recursos diarios y verificando
#               suficiencia antes de cada consumo. El ciclo
#               termina al completar los días o al detectar
#               recursos insuficientes.
# ============================================================

# --- Constantes de consumo diario ---
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1

# --- Entrada de datos ---
dias_viaje = int(input("Ingrese la cantidad de días del viaje: "))
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# --- Inicialización de variables de control ---
dias_transcurridos = 0
mision_activa = True

# --- Cálculo del consumo diario de oxígeno y provisiones ---
consumo_oxigeno_dia = CONSUMO_OXIGENO_TRIPULANTE_DIA * tripulantes
consumo_provisiones_dia = CONSUMO_PROVISIONES_TRIPULANTE_DIA * tripulantes

# --- Ciclo principal: simulación día a día ---
while dias_transcurridos < dias_viaje and mision_activa:

    # Paso 1: Verificar recursos ANTES del consumo del día siguiente
    if (combustible >= CONSUMO_COMBUSTIBLE_DIA
        and oxigeno >= consumo_oxigeno_dia
        and energia >= CONSUMO_ENERGIA_DIA
        and provisiones >= consumo_provisiones_dia):

        # Paso 2: Descontar consumo diario
        combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
        oxigeno = oxigeno - consumo_oxigeno_dia
        energia = energia - CONSUMO_ENERGIA_DIA
        provisiones = provisiones - consumo_provisiones_dia

        # Paso 3: Incrementar el contador de días
        dias_transcurridos = dias_transcurridos + 1

        # Paso 4: Mostrar estado del día
        print("Día", dias_transcurridos,
              "| Combustible:", combustible,
              "| Oxígeno:", oxigeno,
              "| Energía:", energia,
              "| Provisiones:", provisiones)

    else:
        # Recursos insuficientes: marcar la misión como interrumpida
        mision_activa = False

# --- Resultado final ---
if dias_transcurridos == dias_viaje:
    # Resultado A: Viaje completado exitosamente
    print("\nLa nave llegó al destino en", dias_transcurridos, "días.")
    print("Recursos restantes:")
    print("  Combustible:", combustible, "unidades")
    print("  Oxígeno:", oxigeno, "unidades")
    print("  Energía:", energia, "unidades")
    print("  Provisiones:", provisiones, "unidades")
else:
    # Resultado B: Viaje interrumpido
    dia_fallo = dias_transcurridos + 1
    print("\nViaje interrumpido en el día", dia_fallo)

    # Identificar cada recurso insuficiente
    if combustible < CONSUMO_COMBUSTIBLE_DIA:
        print("  - Combustible insuficiente: disponible", combustible,
              "unidades, se requieren", CONSUMO_COMBUSTIBLE_DIA, "unidades")
    if oxigeno < consumo_oxigeno_dia:
        print("  - Oxígeno insuficiente: disponible", oxigeno,
              "unidades, se requieren", consumo_oxigeno_dia, "unidades")
    if energia < CONSUMO_ENERGIA_DIA:
        print("  - Energía insuficiente: disponible", energia,
              "unidades, se requieren", CONSUMO_ENERGIA_DIA, "unidades")
    if provisiones < consumo_provisiones_dia:
        print("  - Provisiones insuficientes: disponible", provisiones,
              "unidades, se requieren", consumo_provisiones_dia, "unidades")

    print("Días completados:", dias_transcurridos)