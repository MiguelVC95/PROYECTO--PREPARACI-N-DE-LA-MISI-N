# ============================================================
# Archivo:      mision_orbita.py
# Curso:        SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes:  Sharon Ávila Matute, Marcela Otárola Montoya,
#               Miguel Ángel Vargas Cedeño
# Fecha:        19/11/2026            Versión: 3.0
# Descripción:  Sistema integrado que administra el ciclo completo
#               de una misión de exploración espacial: preparación,
#               autorización, viaje, llegada, exploración, evaluación
#               del regreso y resultado final. Si el regreso no es
#               posible, estima la supervivencia de la tripulación.
# ============================================================

# ------------------------------------------------------------
# CONSTANTES GLOBALES (no se modifican durante la ejecución)
# ------------------------------------------------------------
# Consumos diarios del viaje
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1

# Reservas exigidas al planificar la misión
RESERVA_COMBUSTIBLE = 10
RESERVA_OXIGENO = 5
RESERVA_ENERGIA = 10
RESERVA_PROVISIONES = 3
MARGEN_MINIMO_ADVERTENCIA = 10

# Actividades de exploración: costo de energía, provisiones,
# combustible (desplazamiento del módulo) y puntos obtenidos
ENERGIA_ANALIZAR = 8
PROVISIONES_ANALIZAR = 0
COMBUSTIBLE_ANALIZAR = 0
PUNTOS_ANALIZAR = 10

ENERGIA_MUESTRA = 12
PROVISIONES_MUESTRA = 2
COMBUSTIBLE_MUESTRA = 6
PUNTOS_MUESTRA = 20

ENERGIA_OBSERVACION = 5
PROVISIONES_OBSERVACION = 0
COMBUSTIBLE_OBSERVACION = 0
PUNTOS_OBSERVACION = 8

MAX_ACTIVIDADES = 5

# Límites del nivel de riesgo según la duración del viaje
DIAS_RIESGO_BAJO = 3
DIAS_RIESGO_MEDIO = 5

# Destinos: la tupla guarda nombres fijos; el diccionario guarda
# la información asociada a cada nombre (ida, regreso, valor científico)
DESTINOS = ("Luna", "Marte", "Europa")
INFO_DESTINOS = {
    "Luna": {"diasIda": 3, "diasRegreso": 3, "valorCientifico": 30},
    "Marte": {"diasIda": 5, "diasRegreso": 5, "valorCientifico": 60},
    "Europa": {"diasIda": 7, "diasRegreso": 7, "valorCientifico": 90},
}

# Estados posibles de la misión
ESTADO_SIN_MISION = "Sin misión"
ESTADO_PREPARADA = "Misión preparada"
ESTADO_AUTORIZADA = "Lanzamiento autorizado"
ESTADO_NO_AUTORIZADA = "Lanzamiento no autorizado"
ESTADO_EN_DESTINO = "En destino"
ESTADO_FALLIDA = "Misión fallida"
ESTADO_REGRESO_POSIBLE = "Regreso verificado"
ESTADO_VARADA = "Tripulación varada"


# ------------------------------------------------------------
# FUNCIONES DE APOYO
# ------------------------------------------------------------
def leerEntero(mensaje, minimo):
    """
    Propósito: lee un número entero desde consola validando que sea
               numérico y mayor o igual al mínimo indicado.
    Parámetros: mensaje (str): texto a mostrar; minimo (int): valor mínimo.
    Retorna: valor (int) válido ingresado por el usuario.
    """
    valorValido = False
    valor = minimo
    # Ciclo de validación: se repite hasta recibir un entero aceptable
    while not valorValido:
        texto = input(mensaje)
        if texto.strip().isdigit() and int(texto) >= minimo:
            valor = int(texto)
            valorValido = True
        else:
            print("Dato inválido. Ingrese un número entero mayor o igual a", minimo)
    return valor


def crearMisionVacia():
    """
    Propósito: crea el diccionario con el estado inicial de la misión.
    Parámetros: ninguno.
    Retorna: mision (dict) con todos los campos inicializados.
    """
    mision = {
        "nombre": "", "tripulantes": 0, "destino": "",
        "diasIda": 0, "diasRegreso": 0,
        "combustible": 0, "combustibleIda": 0, "combustibleRegreso": 0,
        "combustibleTotal": 0, "oxigeno": 0, "oxigenoRequerido": 0,
        "energia": 0, "energiaRequerida": 0,
        "provisiones": 0, "provisionesRequeridas": 0,
        "diasTranscurridos": 0, "puntosCientificos": 0,
        "muestras": 0, "actividades": 0, "nivelRiesgo": "",
        "estado": ESTADO_SIN_MISION, "llegoDestino": False,
        "regresoPosible": False, "diasSupervivencia": 0,
        "recursoCritico": "",
    }
    return mision


# ------------------------------------------------------------
# FUNCIÓN 1: CÁLCULO DE RECURSOS REQUERIDOS
# ------------------------------------------------------------
def calcularRecursosRequeridos(tripulantes, diasIda, diasRegreso):
    """
    Propósito: calcula los recursos que exige la misión.
    Parámetros: tripulantes (int), diasIda (int), diasRegreso (int).
    Retorna: requeridos (dict) con combustible de ida, regreso, total,
             oxígeno, energía y provisiones requeridos.
    """
    # El combustible de regreso se calcula desde el inicio para no
    # autorizar misiones que dejen varada a la tripulación
    combustibleIda = diasIda * CONSUMO_COMBUSTIBLE_DIA
    combustibleRegreso = diasRegreso * CONSUMO_COMBUSTIBLE_DIA
    combustibleTotal = combustibleIda + combustibleRegreso + RESERVA_COMBUSTIBLE
    oxigenoRequerido = diasIda * tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA + RESERVA_OXIGENO
    energiaRequerida = diasIda * CONSUMO_ENERGIA_DIA + RESERVA_ENERGIA
    provisionesRequeridas = diasIda * tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA + RESERVA_PROVISIONES
    requeridos = {
        "combustibleIda": combustibleIda,
        "combustibleRegreso": combustibleRegreso,
        "combustibleTotal": combustibleTotal,
        "oxigenoRequerido": oxigenoRequerido,
        "energiaRequerida": energiaRequerida,
        "provisionesRequeridas": provisionesRequeridas,
    }
    return requeridos


# ------------------------------------------------------------
# FUNCIÓN 2: VERIFICACIÓN DEL COMBUSTIBLE
# ------------------------------------------------------------
def verificarCombustible(combustible, combustibleTotal):
    """
    Propósito: verifica si el combustible cubre ida, regreso y reserva,
               y advierte cuando el margen adicional es bajo.
    Parámetros: combustible (int): disponible; combustibleTotal (int): requerido.
    Retorna: tupla (suficiente: bool, combustibleAdicional: int).
    """
    combustibleAdicional = combustible - combustibleTotal
    suficiente = combustibleAdicional >= 0
    if suficiente and combustibleAdicional < MARGEN_MINIMO_ADVERTENCIA:
        print("Advertencia: el margen adicional de combustible es bajo.")
    return (suficiente, combustibleAdicional)


# ------------------------------------------------------------
# FUNCIÓN 3: VERIFICACIÓN DE RECURSOS PARA LA TRIPULACIÓN
# ------------------------------------------------------------
def verificarRecursosTripulacion(oxigeno, oxigenoRequerido, provisiones, provisionesRequeridas):
    """
    Propósito: verifica si hay oxígeno y provisiones para la tripulación.
    Parámetros: oxigeno (int), oxigenoRequerido (int),
                provisiones (int), provisionesRequeridas (int).
    Retorna: soporteSuficiente (bool).
    """
    soporteSuficiente = oxigeno >= oxigenoRequerido and provisiones >= provisionesRequeridas
    return soporteSuficiente


# ------------------------------------------------------------
# FUNCIÓN 4: AUTORIZACIÓN DEL LANZAMIENTO
# ------------------------------------------------------------
def autorizarLanzamiento(combustibleSuficiente, soporteSuficiente, energia, energiaRequerida):
    """
    Propósito: decide si el lanzamiento se autoriza con base en los
               resultados de las verificaciones de recursos.
    Parámetros: combustibleSuficiente (bool), soporteSuficiente (bool),
                energia (int), energiaRequerida (int).
    Retorna: autorizado (bool).
    """
    autorizado = combustibleSuficiente and soporteSuficiente and energia >= energiaRequerida
    return autorizado


# ------------------------------------------------------------
# FUNCIÓN 5: SELECCIÓN DEL DESTINO
# ------------------------------------------------------------
def seleccionarDestino(opcionDestino):
    """
    Propósito: obtiene el nombre del destino a partir de la opción elegida.
    Parámetros: opcionDestino (int): 1 Luna, 2 Marte, 3 Europa.
    Retorna: destino (str); cadena vacía si la opción no es válida.
    """
    destino = ""
    if opcionDestino >= 1 and opcionDestino <= len(DESTINOS):
        destino = DESTINOS[opcionDestino - 1]
    return destino


def buscarDestino(nombreBuscado):
    """
    Propósito: busca un destino por nombre mediante búsqueda secuencial
               (no distingue mayúsculas de minúsculas).
    Parámetros: nombreBuscado (str): nombre escrito por el usuario.
    Retorna: posicion (int) del destino en DESTINOS, o -1 si no existe.
    """
    posicion = -1
    indice = 0
    # Recorrido secuencial: se detiene al encontrar el destino
    while indice < len(DESTINOS) and posicion == -1:
        if DESTINOS[indice].lower() == nombreBuscado.strip().lower():
            posicion = indice
        indice = indice + 1
    return posicion


def mostrarDestinos():
    """
    Propósito: muestra todos los destinos con su información.
    Parámetros: ninguno.
    Retorna: cantidadDestinos (int) mostrados.
    """
    cantidadDestinos = 0
    print("\n--- Destinos disponibles ---")
    for nombreDestino in DESTINOS:
        datos = INFO_DESTINOS[nombreDestino]
        cantidadDestinos = cantidadDestinos + 1
        print(str(cantidadDestinos) + ". " + nombreDestino +
              " | Ida: " + str(datos["diasIda"]) + " días" +
              " | Regreso: " + str(datos["diasRegreso"]) + " días" +
              " | Valor científico: " + str(datos["valorCientifico"]) + " puntos")
    return cantidadDestinos


# ------------------------------------------------------------
# FUNCIÓN 6: NIVEL DE RIESGO
# ------------------------------------------------------------
def determinarNivelRiesgo(diasIda):
    """
    Propósito: clasifica el riesgo de la misión según la duración del viaje.
    Parámetros: diasIda (int).
    Retorna: nivelRiesgo (str): "Bajo", "Medio" o "Alto".
    """
    if diasIda <= DIAS_RIESGO_BAJO:
        nivelRiesgo = "Bajo"
    elif diasIda <= DIAS_RIESGO_MEDIO:
        nivelRiesgo = "Medio"
    else:
        nivelRiesgo = "Alto"
    return nivelRiesgo


# ------------------------------------------------------------
# FUNCIÓN 7: SIMULACIÓN DEL VIAJE
# ------------------------------------------------------------
def simularViaje(mision, bitacora, perdidaOxigeno):
    """
    Propósito: simula el viaje día por día, verificando recursos antes
               de cada consumo y protegiendo el combustible de regreso.
    Parámetros: mision (dict): estado de la misión; bitacora (list): eventos;
                perdidaOxigeno (int): oxígeno perdido por un incidente el día 1.
    Retorna: llegoDestino (bool).
    """
    consumoOxigenoDia = mision["tripulantes"] * CONSUMO_OXIGENO_TRIPULANTE_DIA
    consumoProvisionesDia = mision["tripulantes"] * CONSUMO_PROVISIONES_TRIPULANTE_DIA
    viajeActivo = True

    # Situación durante el recorrido: incidente de fuga de oxígeno
    if perdidaOxigeno > 0:
        if perdidaOxigeno > mision["oxigeno"]:
            perdidaOxigeno = mision["oxigeno"]
        mision["oxigeno"] = mision["oxigeno"] - perdidaOxigeno
        print("Incidente: fuga de oxígeno de", perdidaOxigeno, "unidades.")
        bitacora.append("Incidente: fuga de oxígeno de " + str(perdidaOxigeno) + " unidades.")

    # Ciclo del viaje: continúa mientras falten días y haya recursos
    while mision["diasTranscurridos"] < mision["diasIda"] and viajeActivo:
        combustibleTrasDia = mision["combustible"] - CONSUMO_COMBUSTIBLE_DIA
        if (combustibleTrasDia >= mision["combustibleRegreso"]
                and mision["oxigeno"] >= consumoOxigenoDia
                and mision["energia"] >= CONSUMO_ENERGIA_DIA
                and mision["provisiones"] >= consumoProvisionesDia):
            mision["combustible"] = combustibleTrasDia
            mision["oxigeno"] = mision["oxigeno"] - consumoOxigenoDia
            mision["energia"] = mision["energia"] - CONSUMO_ENERGIA_DIA
            mision["provisiones"] = mision["provisiones"] - consumoProvisionesDia
            mision["diasTranscurridos"] = mision["diasTranscurridos"] + 1
            print("Día", mision["diasTranscurridos"], "| Combustible:", mision["combustible"],
                  "| Oxígeno:", mision["oxigeno"], "| Energía:", mision["energia"],
                  "| Provisiones:", mision["provisiones"])
            bitacora.append("Día " + str(mision["diasTranscurridos"]) + " completado.")
        else:
            viajeActivo = False

    # Resultado del viaje
    llegoDestino = mision["diasTranscurridos"] == mision["diasIda"]
    if llegoDestino:
        mision["estado"] = ESTADO_EN_DESTINO
        print("La nave llegó a", mision["destino"], "en", mision["diasTranscurridos"], "días.")
        bitacora.append(mision["destino"] + " alcanzado.")
    else:
        mision["estado"] = ESTADO_FALLIDA
        print("Viaje interrumpido en el día", mision["diasTranscurridos"] + 1,
              "por recursos insuficientes.")
        bitacora.append("Viaje interrumpido en el día " + str(mision["diasTranscurridos"] + 1) + ".")
    mision["llegoDestino"] = llegoDestino
    return llegoDestino


# ------------------------------------------------------------
# FUNCIÓN 8: EXPLORACIÓN DEL DESTINO
# ------------------------------------------------------------
def ejecutarExploracion(mision, bitacora, puntuaciones):
    """
    Propósito: ejecuta actividades científicas mediante un menú hasta que
               el usuario finalice, falten recursos o se llegue al máximo.
    Parámetros: mision (dict), bitacora (list), puntuaciones (list).
    Retorna: actividadesSesion (int) realizadas en esta exploración.
    """
    # Tabla de actividades: (nombre, energía, provisiones, combustible, puntos, esMuestra)
    actividadesDisponibles = (
        ("Analizar terreno", ENERGIA_ANALIZAR, PROVISIONES_ANALIZAR, COMBUSTIBLE_ANALIZAR, PUNTOS_ANALIZAR, False),
        ("Recolectar muestra", ENERGIA_MUESTRA, PROVISIONES_MUESTRA, COMBUSTIBLE_MUESTRA, PUNTOS_MUESTRA, True),
        ("Realizar observación", ENERGIA_OBSERVACION, PROVISIONES_OBSERVACION, COMBUSTIBLE_OBSERVACION, PUNTOS_OBSERVACION, False),
    )
    actividadesSesion = 0
    exploracionActiva = True

    # Tres condiciones de permanencia: el usuario no finaliza, hay
    # recursos para la actividad y no se superó el máximo de actividades
    while exploracionActiva and mision["actividades"] < MAX_ACTIVIDADES:
        print("\n--- Menú de exploración ---")
        print("Energía:", mision["energia"], "| Provisiones:", mision["provisiones"],
              "| Combustible:", mision["combustible"])
        print("1. Analizar terreno (8 energía, 10 puntos)")
        print("2. Recolectar muestra (12 energía, 2 provisiones, 6 combustible, 20 puntos)")
        print("3. Realizar observación (5 energía, 8 puntos)")
        print("4. Finalizar exploración")
        opcion = leerEntero("Seleccione una opción: ", 0)

        if opcion >= 1 and opcion <= 3:
            actividad = actividadesDisponibles[opcion - 1]
            # Se verifica antes de descontar para no alterar el estado si se rechaza
            if (mision["energia"] >= actividad[1] and mision["provisiones"] >= actividad[2]
                    and mision["combustible"] >= actividad[3]):
                mision["energia"] = mision["energia"] - actividad[1]
                mision["provisiones"] = mision["provisiones"] - actividad[2]
                mision["combustible"] = mision["combustible"] - actividad[3]
                mision["puntosCientificos"] = mision["puntosCientificos"] + actividad[4]
                mision["actividades"] = mision["actividades"] + 1
                actividadesSesion = actividadesSesion + 1
                puntuaciones.append(actividad[4])
                print("Actividad realizada:", actividad[0] + ". Puntos obtenidos:", actividad[4])
                if actividad[5]:
                    mision["muestras"] = mision["muestras"] + 1
                    bitacora.append("Muestra recolectada.")
                else:
                    bitacora.append("Actividad realizada: " + actividad[0] + ".")
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracionActiva = False
        elif opcion == 4:
            exploracionActiva = False
        else:
            print("Opción no válida.")

    if mision["actividades"] >= MAX_ACTIVIDADES:
        print("Se alcanzó el máximo de", MAX_ACTIVIDADES, "actividades.")

    # Resumen de la exploración
    print("\n--- Resumen de la exploración ---")
    print("Actividades realizadas:", mision["actividades"])
    print("Muestras recolectadas:", mision["muestras"])
    print("Puntos científicos:", mision["puntosCientificos"])
    bitacora.append("Exploración finalizada.")
    return actividadesSesion


# ------------------------------------------------------------
# FUNCIÓN 9: VERIFICACIÓN DEL COMBUSTIBLE DE REGRESO
# ------------------------------------------------------------
def verificarRegreso(mision, bitacora):
    """
    Propósito: compara el combustible restante contra el requerido para
               regresar; si no alcanza, declara la tripulación varada y
               calcula la supervivencia.
    Parámetros: mision (dict), bitacora (list).
    Retorna: regresoPosible (bool).
    """
    regresoPosible = mision["combustible"] >= mision["combustibleRegreso"]
    print("\nCombustible disponible:", mision["combustible"], "unidades")
    print("Combustible requerido para regresar:", mision["combustibleRegreso"], "unidades")
    if regresoPosible:
        combustibleDespuesRegreso = mision["combustible"] - mision["combustibleRegreso"]
        print("Estado de regreso: REGRESO POSIBLE")
        print("Combustible restante después del regreso:", combustibleDespuesRegreso, "unidades")
        mision["estado"] = ESTADO_REGRESO_POSIBLE
        bitacora.append("Combustible de regreso verificado.")
    else:
        diferencia = mision["combustibleRegreso"] - mision["combustible"]
        print("Estado de regreso: REGRESO NO POSIBLE")
        print("Faltan", diferencia, "unidades de combustible.")
        print("La tripulación ha quedado varada.")
        mision["estado"] = ESTADO_VARADA
        bitacora.append("Combustible de regreso insuficiente.")
        bitacora.append("Tripulación varada.")
        resultado = calcularDiasSupervivencia(mision["tripulantes"], mision["oxigeno"],
                                              mision["provisiones"], mision["energia"])
        mision["diasSupervivencia"] = resultado[0]
        mision["recursoCritico"] = resultado[1]
        print("Días estimados de supervivencia:", resultado[0])
        print("Recurso crítico:", resultado[1])
        bitacora.append("Supervivencia estimada: " + str(resultado[0]) + " días.")
    mision["regresoPosible"] = regresoPosible
    return regresoPosible


# ------------------------------------------------------------
# FUNCIÓN 10: CÁLCULO DE SUPERVIVENCIA
# ------------------------------------------------------------
def calcularDiasSupervivencia(tripulantes, oxigeno, provisiones, energia):
    """
    Propósito: estima los días completos que sobrevive una tripulación varada.
    Parámetros: tripulantes (int), oxigeno (int), provisiones (int), energia (int).
    Retorna: tupla (diasSupervivencia: int, recursoCritico: str).
    """
    # División entera: solo cuentan los días completos
    diasOxigeno = oxigeno // (tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA)
    diasProvisiones = provisiones // (tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA)
    diasEnergia = energia // CONSUMO_ENERGIA_DIA
    print("Días por oxígeno:", diasOxigeno)
    print("Días por provisiones:", diasProvisiones)
    print("Días por energía:", diasEnergia)

    # Búsqueda del menor sin usar min()
    diasPorRecurso = (("oxígeno", diasOxigeno), ("provisiones", diasProvisiones), ("energía", diasEnergia))
    diasSupervivencia = diasOxigeno
    for recurso in diasPorRecurso:
        if recurso[1] < diasSupervivencia:
            diasSupervivencia = recurso[1]

    # Identificación de recursos críticos (puede haber empate)
    criticos = []
    for recurso in diasPorRecurso:
        if recurso[1] == diasSupervivencia:
            criticos.append(recurso[0])
    if len(criticos) == 1:
        recursoCritico = criticos[0]
    else:
        recursoCritico = "varios recursos críticos ("
        contador = 0
        for nombreRecurso in criticos:
            if contador > 0:
                recursoCritico = recursoCritico + ", "
            recursoCritico = recursoCritico + nombreRecurso
            contador = contador + 1
        recursoCritico = recursoCritico + ")"
    return (diasSupervivencia, recursoCritico)


# ------------------------------------------------------------
# RESULTADOS CIENTÍFICOS: ESTADÍSTICAS Y ORDENAMIENTO
# ------------------------------------------------------------
def calcularEstadisticas(puntuaciones):
    """
    Propósito: calcula cantidad, total, promedio, mayor y menor puntuación
               mediante recorridos propios (sin sum, min ni max).
    Parámetros: puntuaciones (list) de enteros.
    Retorna: estadisticas (dict); vacío si no hay actividades.
    """
    estadisticas = {}
    if len(puntuaciones) > 0:
        total = 0
        mayor = puntuaciones[0]
        menor = puntuaciones[0]
        for puntaje in puntuaciones:
            total = total + puntaje
            if puntaje > mayor:
                mayor = puntaje
            if puntaje < menor:
                menor = puntaje
        estadisticas = {"cantidad": len(puntuaciones), "total": total,
                        "promedio": total / len(puntuaciones), "mayor": mayor, "menor": menor}
    return estadisticas


def ordenarPuntuaciones(puntuaciones, ascendente):
    """
    Propósito: ordena una copia de las puntuaciones con el método burbuja.
    Parámetros: puntuaciones (list); ascendente (bool): True menor a mayor.
    Retorna: ordenadas (list) nueva lista ordenada.
    """
    ordenadas = list(puntuaciones)
    cantidad = len(ordenadas)
    for pasada in range(cantidad - 1):
        for posicion in range(cantidad - 1 - pasada):
            if ascendente:
                debeIntercambiar = ordenadas[posicion] > ordenadas[posicion + 1]
            else:
                debeIntercambiar = ordenadas[posicion] < ordenadas[posicion + 1]
            if debeIntercambiar:
                temporal = ordenadas[posicion]
                ordenadas[posicion] = ordenadas[posicion + 1]
                ordenadas[posicion + 1] = temporal
    return ordenadas


def mostrarResultadosCientificos(puntuaciones):
    """
    Propósito: muestra estadísticas y permite ordenar las puntuaciones.
    Parámetros: puntuaciones (list).
    Retorna: hayActividades (bool).
    """
    estadisticas = calcularEstadisticas(puntuaciones)
    hayActividades = len(estadisticas) > 0
    if not hayActividades:
        print("No se han realizado actividades científicas.")
    else:
        print("\nPuntuaciones:", puntuaciones)
        print("Cantidad de actividades:", estadisticas["cantidad"])
        print("Total de puntos científicos:", estadisticas["total"], "puntos")
        print("Promedio por actividad: " + format(estadisticas["promedio"], ".2f") + " puntos")
        print("Mayor puntuación:", estadisticas["mayor"], "puntos")
        print("Menor puntuación:", estadisticas["menor"], "puntos")
        print("1. Ordenar de menor a mayor  2. Ordenar de mayor a menor  3. Volver")
        opcionOrden = leerEntero("Seleccione una opción: ", 0)
        if opcionOrden == 1:
            print("Ascendente:", ordenarPuntuaciones(puntuaciones, True))
        elif opcionOrden == 2:
            print("Descendente:", ordenarPuntuaciones(puntuaciones, False))
    return hayActividades


# ------------------------------------------------------------
# RESULTADO FINAL DE LA MISIÓN
# ------------------------------------------------------------
def determinarEstadoFinal(mision):
    """
    Propósito: determina el estado final según llegada, actividades y regreso.
    Parámetros: mision (dict).
    Retorna: estadoFinal (str).
    """
    if not mision["llegoDestino"]:
        estadoFinal = "Misión fallida"
    elif mision["actividades"] > 0 and mision["regresoPosible"]:
        estadoFinal = "Misión exitosa"
    elif mision["actividades"] > 0:
        estadoFinal = "Misión parcialmente exitosa"
    elif mision["regresoPosible"]:
        estadoFinal = "Misión sin exploración"
    else:
        estadoFinal = "Misión sin exploración (tripulación varada)"
    return estadoFinal


def mostrarResumenFinal(mision):
    """
    Propósito: muestra el resumen completo de la misión.
    Parámetros: mision (dict).
    Retorna: estadoFinal (str) mostrado.
    """
    estadoFinal = determinarEstadoFinal(mision)
    print("\n========== RESULTADO FINAL DE LA MISIÓN ==========")
    print("Misión:", mision["nombre"], "| Destino:", mision["destino"],
          "| Tripulantes:", mision["tripulantes"])
    print("Duración prevista:", mision["diasIda"] + mision["diasRegreso"], "días",
          "| Días completados:", mision["diasTranscurridos"])
    print("Recursos -> Combustible:", mision["combustible"], "| Requerido para regresar:",
          mision["combustibleRegreso"], "| Diferencia:", mision["combustible"] - mision["combustibleRegreso"])
    print("Oxígeno:", mision["oxigeno"], "| Energía:", mision["energia"],
          "| Provisiones:", mision["provisiones"])
    print("Exploración -> Actividades:", mision["actividades"], "| Muestras:", mision["muestras"],
          "| Puntos científicos:", mision["puntosCientificos"])
    if mision["estado"] == ESTADO_VARADA:
        print("Regreso: tripulación varada. Supervivencia estimada:", mision["diasSupervivencia"],
              "días. Recurso limitante:", mision["recursoCritico"])
    elif mision["regresoPosible"]:
        print("Regreso: posible. Combustible estimado después del regreso:",
              mision["combustible"] - mision["combustibleRegreso"], "unidades")
    print("Estado final:", estadoFinal)
    return estadoFinal


# ------------------------------------------------------------
# PREPARACIÓN Y EVALUACIÓN (coordinan las funciones 1 a 6)
# ------------------------------------------------------------
def prepararMision(bitacora):
    """
    Propósito: solicita los datos de una nueva misión y calcula sus requerimientos.
    Parámetros: bitacora (list) que se reinicia con la nueva misión.
    Retorna: mision (dict) preparada, o sin misión si el destino es inválido.
    """
    mision = crearMisionVacia()
    nombre = input("Ingrese el nombre de la misión: ")
    tripulantes = leerEntero("Ingrese la cantidad de tripulantes: ", 1)
    mostrarDestinos()
    destino = seleccionarDestino(leerEntero("Seleccione el destino (1-3): ", 0))
    if destino == "":
        print("Opción de destino no válida. La misión no puede planificarse.")
    else:
        mision["nombre"] = nombre
        mision["tripulantes"] = tripulantes
        mision["destino"] = destino
        mision["diasIda"] = INFO_DESTINOS[destino]["diasIda"]
        mision["diasRegreso"] = INFO_DESTINOS[destino]["diasRegreso"]
        mision["combustible"] = leerEntero("Ingrese el combustible disponible: ", 0)
        mision["oxigeno"] = leerEntero("Ingrese el oxígeno disponible: ", 0)
        mision["energia"] = leerEntero("Ingrese la energía disponible: ", 0)
        mision["provisiones"] = leerEntero("Ingrese las provisiones disponibles: ", 0)
        requeridos = calcularRecursosRequeridos(tripulantes, mision["diasIda"], mision["diasRegreso"])
        for clave in requeridos:
            mision[clave] = requeridos[clave]
        mision["estado"] = ESTADO_PREPARADA
        print("\nCombustible para llegar:", mision["combustibleIda"], "unidades")
        print("Combustible para regresar:", mision["combustibleRegreso"], "unidades")
        print("Combustible total requerido:", mision["combustibleTotal"], "unidades")
        print("Oxígeno requerido:", mision["oxigenoRequerido"], "| Energía requerida:",
              mision["energiaRequerida"], "| Provisiones requeridas:", mision["provisionesRequeridas"])
        bitacora.append("Misión creada.")
    return mision


def evaluarCondiciones(mision, bitacora):
    """
    Propósito: evalúa combustible, tripulación, energía y riesgo para
               autorizar o rechazar el lanzamiento.
    Parámetros: mision (dict), bitacora (list).
    Retorna: autorizado (bool).
    """
    resultadoCombustible = verificarCombustible(mision["combustible"], mision["combustibleTotal"])
    soporte = verificarRecursosTripulacion(mision["oxigeno"], mision["oxigenoRequerido"],
                                           mision["provisiones"], mision["provisionesRequeridas"])
    mision["nivelRiesgo"] = determinarNivelRiesgo(mision["diasIda"])
    print("Combustible adicional:", resultadoCombustible[1], "unidades")
    print("Soporte para la tripulación:", "suficiente" if soporte else "insuficiente")
    print("Nivel de riesgo:", mision["nivelRiesgo"])
    # Caso específico: alcanza para llegar pero no para regresar
    if (not resultadoCombustible[0]
            and mision["combustible"] >= mision["combustibleIda"]):
        print("Combustible suficiente solo para llegar al destino, no para regresar.")
    autorizado = autorizarLanzamiento(resultadoCombustible[0], soporte,
                                      mision["energia"], mision["energiaRequerida"])
    if autorizado:
        mision["estado"] = ESTADO_AUTORIZADA
        print("Lanzamiento autorizado.")
        bitacora.append("Lanzamiento autorizado.")
    else:
        mision["estado"] = ESTADO_NO_AUTORIZADA
        print("Lanzamiento no autorizado. La misión debe ser revisada.")
        bitacora.append("Lanzamiento no autorizado.")
    return autorizado


def mostrarEstado(mision):
    """
    Propósito: muestra el estado actual de la misión.
    Parámetros: mision (dict).
    Retorna: estado (str) actual.
    """
    print("\n--- Estado de la misión ---")
    for clave in mision:
        print(clave + ":", mision[clave])
    return mision["estado"]


def mostrarBitacora(bitacora):
    """
    Propósito: muestra los eventos de la bitácora numerados en orden cronológico.
    Parámetros: bitacora (list).
    Retorna: cantidadEventos (int).
    """
    cantidadEventos = 0
    if len(bitacora) == 0:
        print("La bitácora está vacía.")
    for evento in bitacora:
        cantidadEventos = cantidadEventos + 1
        print(str(cantidadEventos) + ". " + evento)
    return cantidadEventos


def consultarDestinos():
    """
    Propósito: submenú para consultar todos los destinos o buscar uno por nombre.
    Parámetros: ninguno.
    Retorna: posicion (int) encontrada, o -1.
    """
    mostrarDestinos()
    posicion = buscarDestino(input("Ingrese el nombre del destino a buscar: "))
    if posicion == -1:
        print("El destino no se encuentra registrado.")
    else:
        nombreDestino = DESTINOS[posicion]
        print("Destino encontrado:", nombreDestino, "| Ida:", INFO_DESTINOS[nombreDestino]["diasIda"],
              "días | Valor científico:", INFO_DESTINOS[nombreDestino]["valorCientifico"], "puntos")
    return posicion


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------
def main():
    """
    Propósito: coordina el sistema mediante un menú que se repite hasta
               que el usuario decide finalizar, aplicando las reglas de operación.
    Parámetros: ninguno.
    Retorna: None.
    """
    mision = crearMisionVacia()
    bitacora = []
    puntuaciones = []
    programaActivo = True

    # Ciclo del menú principal
    while programaActivo:
        print("\n========== MISIÓN ÓRBITA ==========")
        print("1. Preparar una nueva misión")
        print("2. Consultar estado de la misión")
        print("3. Evaluar condiciones de lanzamiento")
        print("4. Iniciar viaje")
        print("5. Realizar exploración")
        print("6. Verificar condiciones para el regreso")
        print("7. Consultar bitácora")
        print("8. Consultar resultados de la misión")
        print("9. Consultar y buscar destinos")
        print("10. Finalizar programa")
        opcion = leerEntero("Seleccione una opción: ", 0)

        # Decisión del menú: cada opción valida el estado antes de actuar
        if opcion == 1:
            bitacora = []
            puntuaciones = []
            mision = prepararMision(bitacora)
        elif opcion == 2:
            mostrarEstado(mision)
        elif opcion == 3:
            if mision["estado"] == ESTADO_PREPARADA or mision["estado"] == ESTADO_NO_AUTORIZADA:
                evaluarCondiciones(mision, bitacora)
            else:
                print("Debe preparar una misión que aún no haya iniciado el viaje.")
        elif opcion == 4:
            if mision["estado"] == ESTADO_SIN_MISION:
                print("No se puede iniciar el viaje: no se ha preparado una misión.")
            elif mision["llegoDestino"] or mision["estado"] == ESTADO_FALLIDA:
                print("No se puede iniciar nuevamente el viaje: la misión ya lo realizó.")
            elif mision["estado"] != ESTADO_AUTORIZADA:
                print("No se puede iniciar el viaje: el lanzamiento no ha sido autorizado.")
            else:
                perdida = leerEntero("Oxígeno perdido por incidente en el recorrido (0 = ninguno): ", 0)
                simularViaje(mision, bitacora, perdida)
        elif opcion == 5:
            if mision["estado"] == ESTADO_EN_DESTINO:
                ejecutarExploracion(mision, bitacora, puntuaciones)
                # Regla: tras explorar se verifica de nuevo el regreso
                verificarRegreso(mision, bitacora)
            else:
                print("No se permite explorar: la nave no se encuentra en el destino.")
        elif opcion == 6:
            if mision["llegoDestino"]:
                verificarRegreso(mision, bitacora)
            else:
                print("La nave aún no ha alcanzado el destino.")
        elif opcion == 7:
            mostrarBitacora(bitacora)
        elif opcion == 8:
            if mision["estado"] != ESTADO_SIN_MISION:
                mostrarResumenFinal(mision)
            mostrarResultadosCientificos(puntuaciones)
        elif opcion == 9:
            consultarDestinos()
        elif opcion == 10:
            programaActivo = False
            print("Programa finalizado.")
        else:
            print("Opción no válida. Intente de nuevo.")


# Punto único de ejecución del sistema
main()
