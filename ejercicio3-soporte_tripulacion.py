# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: 
# Marcela Otarola Montoya
# Miguel Angel Vargas
# Sharon Avila Matute
# Fecha: 12/10/2026
# Versión: 1.0
# Descripción: Verificar si la nave posee suficiente oxígeno
# y provisiones para brindar soporte a la tripulación.
# ============================================================

# Entrada de datos
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

if (oxigeno_disponible >= oxigeno_requerido) and (provisiones_disponibles >= provisiones_requeridas):
        print ("La nave posee recursos suficientes para la tripulacion")
else:
        print ("La nave NO posee recursos suficientes para la tripualcion")
