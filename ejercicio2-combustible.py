
# ---------------------------------------------------------------
# Archivo:      ejercicio2_combustible.py
# Curso:        SOFT-01 Principios de Programación 1, Sección SCP0
# Integrantes:  Sharon Avila M, Miguel Vargas, Marcela Otarola
# Fecha:        2026-10-11
# Versión:      1.0
# Descripción:  Verificación de disponibilidad de combustible
#               para una misión espacial usando condicional simple.
#               Se verifica si el combustible adicional disponible
#               es bajo y se muestra una advertencia si corresponde.
# ---------------------------------------------------------------

# ========================
# CONSTANTES
# ========================
RESERVA_EMERGENCIA = 10
MARGEN_MINIMO_ADVERTENCIA = 10

# ========================
# ENTRADA DE DATOS
# ========================
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para llegar al destino: "))
combustible_regreso = int(input("Ingrese el combustible requerido para regresar: "))

# ========================
# PROCESAMIENTO (cálculos)
# ========================
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_EMERGENCIA
combustible_adicional = combustible_disponible - combustible_total_requerido

# ========================
# SALIDA DE RESULTADOS
# ========================
print("Combustible disponible: " + str(combustible_disponible) + " unidades")
print("Combustible requerido para llegar: " + str(combustible_ida) + " unidades")
print("Combustible requerido para regresar: " + str(combustible_regreso) + " unidades")
print("Reserva de emergencia: " + str(RESERVA_EMERGENCIA) + " unidades")
print("Combustible total requerido: " + str(combustible_total_requerido) + " unidades")
print("Combustible adicional disponible: " + str(combustible_adicional) + " unidades")

# ========================
# DECISIÓN (condicional simple)
# ========================
if combustible_adicional < MARGEN_MINIMO_ADVERTENCIA:
    print("Advertencia: el margen adicional de combustible es bajo.")

