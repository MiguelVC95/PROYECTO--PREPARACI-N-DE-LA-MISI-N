
# ---------------------------------------------------------
# PROYECTO: MISIÓN ÓRBITA / Principios de programacion
# AVANCE 2
# EJERCICIO 8: EVALUACIÓN DEL REGRESO Y SUPERVIVENCIA
# ---------------------------------------------------------
# Descripción:
# En este ejercicio se evalúa si una tripulación cuenta con los
# recursos necesarios para regresar a la Tierra.
# Si el combustible es suficiente, simula el viaje de
# regreso y verifica el consumo diario de los recursos.
# Si no es suficiente, calcula los días estimados de
# supervivencia e identifica los recursos limitantes.

# Constantes
CONSUMO_COMBUSTIBLE_DIA = 8 #8 unidades por día
CONSUMO_OXIGENO_PERSONA = 2 #2 unidades por persona al día
CONSUMO_ENERGIA_DIA = 5 #5 unidades por día
CONSUMO_PROVISIONES_PERSONA = 1 #1 unidad por persona al día

# Datos de entrada
print("EVALUACIÓN DEL REGRESO Y SUPERVIVENCIA")

tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los días del viaje de regreso: "))
combustible = int(input("Ingrese la cantidad de combustible disponible: "))
oxigeno = int(input("Ingrese la cantidad de oxígeno disponible: "))
energia = int(input("Ingrese la cantidad de energía disponible: "))
provisiones = int(input("Ingrese la cantidad de provisiones disponibles: "))

# EVALUACIÓN DEL COMBUSTIBLE PARA EL REGRESO

combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA

if combustible >= combustible_regreso:
    print("La nave tiene suficiente combustible para el regreso.")

    dias_transcurridos = 0 # lleva el conteo de los días simulados, CONTADOR
    puede_continuar = True # simulación puede continuar mientras haya suficientes recursos, bandera booleana, SE DETIENE O NO?

    # SIMULACIÓN DEL VIAJE DE REGRESO
    while dias_transcurridos < dias_viaje and puede_continuar == True: #== significan comparación, se deben cumpliar ambas condiciones

        # Calcular los recursos que se consumen en un dia
        combustible_dia = CONSUMO_COMBUSTIBLE_DIA
        oxigeno_dia = tripulantes * CONSUMO_OXIGENO_PERSONA
        energia_dia = CONSUMO_ENERGIA_DIA
        provisiones_dia = tripulantes * CONSUMO_PROVISIONES_PERSONA

        # Verificar si todos los recursos son suficientes para completar un día más de viaje.
        if (combustible >= combustible_dia and
            oxigeno >= oxigeno_dia and
            energia >= energia_dia and
            provisiones >= provisiones_dia):

            combustible = combustible - combustible_dia
            oxigeno = oxigeno - oxigeno_dia
            energia = energia - energia_dia
            provisiones = provisiones - provisiones_dia

            dias_transcurridos = dias_transcurridos + 1

            print("Día completado:", dias_transcurridos)

        else:
            puede_continuar = False # Al cambiar la bandera a False, el ciclo while termina en su siguiente evaluación.

# RESULTADO DEL VIAJE DE REGRESO

    if dias_transcurridos == dias_viaje: # Si el contador es igual a la duración del viaje, 
    # significa que la tripulación llegó a la Tierra.
        print("La tripulación regresó exitosamente a la Tierra.")
        print("Recursos restantes:")
        print("Combustible:", combustible)
        print("Oxígeno:", oxigeno)
        print("Energía:", energia)
        print("Provisiones:", provisiones)

    else:
        print("El viaje se interrumpió en el día:", dias_transcurridos + 1) # Sumamos 1 porque dias_transcurridos cuenta únicamente los días completados

        print("Recursos insuficientes:")

        if combustible < combustible_dia:
            print("Combustible insuficiente")

        if oxigeno < oxigeno_dia:
            print("Oxígeno insuficiente")

        if energia < energia_dia:
            print("Energía insuficiente")

        if provisiones < provisiones_dia:
            print("Provisiones insuficientes")

        print("La tripulación no completó el regreso.")

else:
    print("La tripulación quedó varada en el destino por falta de combustible.")

   # CÁLCULO DE SUPERVIVENCIA EN EL DESTINO

    dias_oxigeno = oxigeno // (tripulantes * CONSUMO_OXIGENO_PERSONA) # realiza una división entera, descartando la parte decimal
    dias_energia = energia // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones // (tripulantes * CONSUMO_PROVISIONES_PERSONA)

    # Mostrar días disponibles por recurso
    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:", dias_energia)
    print("Días por provisiones:", dias_provisiones)
    
    # Inicializar la supervivencia estimada
    supervivencia_estimada = dias_oxigeno

    # Comparar los días disponibles de cada recurso
    if dias_energia < supervivencia_estimada:
        supervivencia_estimada = dias_energia

    if dias_provisiones < supervivencia_estimada:
        supervivencia_estimada = dias_provisiones


    # IDENTIFICACIÓN DE RECURSOS LIMITANTES

    recursos_limitantes = ""

    if dias_oxigeno == supervivencia_estimada:
        recursos_limitantes = recursos_limitantes + "Oxígeno "

    if dias_energia == supervivencia_estimada:
        recursos_limitantes = recursos_limitantes + "Energía "

    if dias_provisiones == supervivencia_estimada:
        recursos_limitantes = recursos_limitantes + "Provisiones "

    # Mostrar el resultado de supervivencia
    print("Días estimados de supervivencia:", supervivencia_estimada)
    print("Recursos limitantes:", recursos_limitantes)


 