
# ---------------------------------------------------------------
# Archivo:      ejercicio1_recursos.py
# Curso:        SOFT-01 Principios de Programación 1, Sección SCP0
# Integrantes:  Sharon Avila M, Miguel Vargas, Marcela Otarola
# Fecha:        2026-10-11
# Versión:      1.0
# Descripción:  Cálculo de recursos necesarios para una misión
#               espacial utilizando flujo secuencial.
#               Se calculan: combustible (ida, regreso, reserva),
#               oxígeno, energía y provisiones.
# ---------------------------------------------------------------

# ========================
# CONSTANTES
# ========================
CONSUMO_COMBUSTIBLE_POR_DIA = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_POR_DIA = 2
EMERGENCIA_OXIGENO = 5
CONSUMO_ENERGIA_POR_DIA = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_POR_DIA = 1
PROVISIONES_ADICIONALES = 3

# ========================
# ENTRADA DE DATOS
# ========================
nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los días estimados hasta el destino: "))

# ========================
# PROCESAMIENTO (cálculos)
# ========================
# Combustible
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_POR_DIA
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_POR_DIA
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Oxígeno (solo viaje de ida)
oxigeno_requerido = dias_viaje * tripulantes * CONSUMO_OXIGENO_POR_DIA + EMERGENCIA_OXIGENO

# Energía (solo viaje de ida)
energia_requerida = dias_viaje * CONSUMO_ENERGIA_POR_DIA + ENERGIA_EXPLORACION

# Provisiones
provisiones_requeridas = dias_viaje * tripulantes * CONSUMO_PROVISIONES_POR_DIA + PROVISIONES_ADICIONALES

# ========================
# SALIDA DE RESULTADOS
# ========================
print("Misión: " + nombre_mision)
print("Tripulantes: " + str(tripulantes))
print("Duración estimada hasta el destino: " + str(dias_viaje) + " días")
print("Combustible para llegar: " + str(combustible_ida) + " unidades")
print("Combustible para regresar: " + str(combustible_regreso) + " unidades")
print("Reserva de combustible: " + str(RESERVA_COMBUSTIBLE) + " unidades")
print("Combustible total requerido: " + str(combustible_total) + " unidades")
print("Oxígeno requerido: " + str(oxigeno_requerido) + " unidades")
print("Energía requerida: " + str(energia_requerida) + " unidades")
print("Provisiones requeridas: " + str(provisiones_requeridas) + " unidades")

