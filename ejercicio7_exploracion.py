# ---------------------------------------------------------------
# Archivo:      ejercicio7_exploracion.py
# Curso:        SOFT-01 Principios de Programación 1, Sección SCP0
# Integrantes:  Sharon Ávila Matute, Marcela Otárola Montoya,
#               Miguel Ángel Vargas Cedeño
# Fecha:        15/11/2026
# Versión:      1.0
# Descripción:  Simula las actividades de exploración científica
#               en el destino mediante un menú repetitivo (while),
#               una condicional múltiple (match-case), contadores
#               y un acumulador de puntos científicos.
# ---------------------------------------------------------------

# ========================
# CONSTANTES
# ========================
# Costo y puntos de cada actividad, según la tabla de la consigna
ENERGIA_ANALIZAR = 8
PROVISIONES_ANALIZAR = 0
PUNTOS_ANALIZAR = 10

ENERGIA_MUESTRA = 12
PROVISIONES_MUESTRA = 2
PUNTOS_MUESTRA = 20

ENERGIA_OBSERVACION = 5
PROVISIONES_OBSERVACION = 0
PUNTOS_OBSERVACION = 8

# ========================
# ENTRADA DE DATOS
# ========================
energia_disponible = int(input("Ingrese la energía disponible: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))

# ========================
# INICIALIZACIÓN
# ========================
# Contadores y acumulador inician en 0 porque aún no se ha realizado
# ninguna actividad
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0

# Variable de control del ciclo. Se usa una variable booleana porque
# el menú termina por DOS motivos: elegir la opción 4 o que una
# actividad se rechace por falta de recursos
exploracion_activa = True

# ========================
# CICLO DEL MENÚ
# ========================
# Se usa while porque no se sabe de antemano cuántas veces se repetirá
while exploracion_activa:
    print()
    print("--- Menú de exploración ---")
    print("Energía: " + str(energia_disponible) + " | Provisiones: " + str(provisiones_disponibles))
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    opcion = int(input("Seleccione una opción: "))

    # ---------- Decisión (condicional múltiple) ----------
    # Cada opción del menú es una alternativa excluyente
    match opcion:
        case 1:
            # Se verifica ANTES de descontar para que una actividad
            # rechazada no modifique recursos, contadores ni puntos
            if (energia_disponible >= ENERGIA_ANALIZAR
                    and provisiones_disponibles >= PROVISIONES_ANALIZAR):
                energia_disponible = energia_disponible - ENERGIA_ANALIZAR
                provisiones_disponibles = provisiones_disponibles - PROVISIONES_ANALIZAR
                actividades_realizadas = actividades_realizadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_ANALIZAR
                print("Actividad realizada: Analizar terreno. Puntos obtenidos: " + str(PUNTOS_ANALIZAR))
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_activa = False

        case 2:
            if (energia_disponible >= ENERGIA_MUESTRA
                    and provisiones_disponibles >= PROVISIONES_MUESTRA):
                energia_disponible = energia_disponible - ENERGIA_MUESTRA
                provisiones_disponibles = provisiones_disponibles - PROVISIONES_MUESTRA
                actividades_realizadas = actividades_realizadas + 1
                # Solo esta actividad aumenta el contador de muestras
                muestras_recolectadas = muestras_recolectadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_MUESTRA
                print("Actividad realizada: Recolectar muestra. Puntos obtenidos: " + str(PUNTOS_MUESTRA))
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_activa = False

        case 3:
            if (energia_disponible >= ENERGIA_OBSERVACION
                    and provisiones_disponibles >= PROVISIONES_OBSERVACION):
                energia_disponible = energia_disponible - ENERGIA_OBSERVACION
                provisiones_disponibles = provisiones_disponibles - PROVISIONES_OBSERVACION
                actividades_realizadas = actividades_realizadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_OBSERVACION
                print("Actividad realizada: Realizar observación. Puntos obtenidos: " + str(PUNTOS_OBSERVACION))
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_activa = False

        case 4:
            # El usuario decide terminar: se apaga la variable de control
            exploracion_activa = False

        case _:
            # Cualquier otro número: no se modifica el estado y el menú se repite
            print("Opción no válida.")

# ========================
# SALIDA DE RESULTADOS
# ========================
print()
print("Actividades realizadas: " + str(actividades_realizadas))
print("Muestras recolectadas: " + str(muestras_recolectadas))
print("Puntos científicos: " + str(puntos_cientificos))
print("Energía restante: " + str(energia_disponible) + " unidades")
print("Provisiones restantes: " + str(provisiones_disponibles) + " unidades")
