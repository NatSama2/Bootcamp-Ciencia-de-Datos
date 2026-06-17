import statistics

participantes = {}  
equipos = {}       
historial_partidas = []  

# --- 1. ENTRADA Y VALIDACIÓN DE DATOS ---
def registrar_participante():
    print("\n--- REGISTRAR NUEVO PARTICIPANTE ---")
    
    # Validar nombre
    nombre = input("Ingrese el nombre: ")
    while nombre == "":
        print("Error: El nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre: ")
        
    if nombre in participantes:
        print("Error: Este participante ya está registrado.")
        return

    # Validar edad (entre 12 y 70)
    edad = int(input("Ingrese la edad (12 a 70): "))
    while edad < 12 or edad > 70:
        print("Error: Edad fuera de rango permitido.")
        edad = int(input("Ingrese la edad (12 a 70): "))

    # Validar nivel (entre 1 y 5)
    nivel = int(input("Ingrese el nivel de experiencia (1 a 5): "))
    while nivel < 1 or nivel > 5:
        print("Error: El nivel debe ser entre 1 y 5.")
        nivel = int(input("Ingrese el nivel de experiencia (1 a 5): "))

    # Guardamos los datos en una lista dentro del diccionario
    participantes[nombre] = [edad, nivel]
    print("¡Participante registrado con éxito!")


# --- 2. GESTIÓN DE PARTICIPANTES Y EQUIPOS ---
def formar_equipo():
    print("\n--- CREAR UN EQUIPO ---")
    
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    while nombre_equipo == "":
        print("Error: El nombre del equipo no puede estar vacío.")
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        
    if nombre_equipo in equipos:
        print("Error: Ese nombre de equipo ya existe.")
        return

    j1 = input("Ingrese el nombre del Primer Jugador: ")
    j2 = input("Ingrese el nombre del Segundo Jugador: ")

    # Verificar que los jugadores existan en el sistema
    if j1 not in participantes or j2 not in participantes:
        print("Error: Uno o ambos jugadores no están registrados en el sistema.")
        return

    # Verificar que no sean la misma persona
    if j1 == j2:
        print("Error: No puedes armar un equipo con el mismo jugador dos veces.")
        return

    # ver que ninguno tenga equipo
    ya_tiene_equipo = False
    for eq in equipos:
        integrantes = equipos[eq]
        if j1 == integrantes[0] or j1 == integrantes[1] or j2 == integrantes[0] or j2 == integrantes[1]:
            ya_tiene_equipo = True

    if ya_tiene_equipo == True:
        print("Error: Uno de los jugadores ya forma parte de otro equipo.")
        return


    equipos[nombre_equipo] = [j1, j2, 0]
    print("¡Equipo formado correctamente!")


# --- 3. REGISTRO Y ANÁLISIS DE PARTIDAS ---
def registrar_partida():
    print("\n--- REGISTRAR PARTIDA JUGADA ---")
    
    eq1 = input("Ingrese el nombre del Equipo 1: ")
    eq2 = input("Ingrese el nombre del Equipo 2: ")

    # Validar que los equipos existan
    if eq1 not in equipos or eq2 not in equipos:
        print("Error: Uno o ambos equipos no existen.")
        return
        
    if eq1 == eq2:
        print("Error: Un equipo no puede jugar contra sí mismo.")
        return

    # Validar el ganador
    ganador = input("¿Qué equipo ganó? (Escriba el nombre exacto): ")
    while ganador != eq1 and ganador != eq2:
        print("Error: El ganador debe ser uno de los dos equipos que jugaron.")
        ganador = input("¿Qué equipo ganó?: ")

    # Sumar los 3 puntos al equipo ganador
    datos_ganador = equipos[ganador]
    datos_ganador[2] = datos_ganador[2] + 3

    # Guardar en el historial de texto
    texto_partida = eq1 + " VS " + eq2 + " -> Ganador: " + ganador
    historial_partidas.append(texto_partida)
    print("¡Partida guardada y 3 puntos asignados!")


# --- 4. REPORTES Y CIERRE ---
def mostrar_reportes():
    print("\n========================================")
    print("         REPORTE DEL TORNEO")
    print("========================================")

    # Lista de Participantes
    print("\n--- PARTICIPANTES REGISTRADOS ---")
    for p in participantes:
        datos = participantes[p]
        print("Nombre:", p, "| Edad:", datos[0], "| Nivel:", datos[1])

    # Lista de Equipos
    print("\n--- EQUIPOS FORMADOS ---")
    for eq in equipos:
        datos = equipos[eq]
        print("Equipo:", eq, "| Integrantes:", datos[0], "y", datos[1], "| Puntos:", datos[2])

    # Ranking ordenado 
    print("\n--- RANKING DE EQUIPOS ---")
    lista_ordenar = []
    for eq in equipos:
        datos = equipos[eq]
        puntos = datos[2]
        lista_ordenar.append([puntos, eq]) 

    # ordena listas
    lista_ordenar.sort(reverse=True) 

    posicion = 1
    for elemento in lista_ordenar:
        print(posicion, "-", elemento[1], "con", elemento[0], "puntos.")
        posicion = posicion + 1

    # Uso de la librería statistics para el promedio
    print("\n--- ESTADÍSTICAS GENERALES ---")
    lista_puntos = []
    for eq in equipos:
        datos = equipos[eq]
        lista_puntos.append(datos[2])

    if len(lista_puntos) > 0:
        promedio = statistics.mean(lista_puntos)
        print("Promedio de puntos de los equipos:", promedio)
    else:
        print("No hay equipos con puntos para sacar promedio todavía.")

    # Historial de partidas
    print("\n--- HISTORIAL DE PARTIDAS ---")
    for partida in historial_partidas:
        print("-", partida)
    print("========================================")


# --- MENÚ PRINCIPAL DEL PROGRAMA ---
def menu():
    opcion = "0"
    while opcion != "5":
        print("\n*** MENÚ DE CONTROL - PIXELES RETRO ***")
        print("1. Registrar Participante")
        print("2. Formar Equipo")
        print("3. Registrar Partida")
        print("4. Mostrar Reportes y Estadísticas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            registrar_participante()
        elif opcion == "2":
            formar_equipo()
        elif opcion == "3":
            registrar_partida()
        elif opcion == "4":
            mostrar_reportes()
        elif opcion == "5":
            print("\n¡Saliendo del programa... Gracias por usar el sistema!")
        else:
            print("Opción no válida, intente otra vez.")

# Ejecutar el programa
menu()