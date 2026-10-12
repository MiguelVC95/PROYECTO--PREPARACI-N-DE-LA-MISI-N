# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Sharon Ávila Matute, Marcela Otarola Montoya, Miguel Angel Vargas Cedeño
# Fecha: 12/10/2026        Versión: 1.0
# Descripción: Determina si la misión puede ser autorizada
# evaluando combustible, oxígeno, energía y provisiones.
# ============================================================

# ---------- Declaración de constantes ----------
RESERVA_COMBUSTIBLE = 10

# ---------- Entrada de datos ----------
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para llegar: "))
combustible_regreso = int(input("Ingrese el combustible requerido para regresar: "))
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))
energia_disponible = int(input("Ingrese la energía disponible: "))
energia_requerida = int(input("Ingrese la energía requerida: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# ---------- Procesamiento ----------
# Se exige combustible de regreso y reserva desde el inicio,
# para que nunca se autorice una misión que deje varada a la tripulación
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

print()
print("Combustible total requerido:", combustible_total, "unidades")

# ---------- Decisión (condicional doble sin anidación) ----------
# Una sola condición compuesta: los cuatro recursos deben ser suficientes
if (combustible_disponible >= combustible_total
        and oxigeno_disponible >= oxigeno_requerido
        and energia_disponible >= energia_requerida
        and provisiones_disponibles >= provisiones_requeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")
