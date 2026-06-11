print("BIENVENIDO AL JUEGO")
print("----------------------------------")

edad = int(input("ingrese su edad: "))
puntaje = int(input("Ingrese su puntaje (0-100): "))
tiene_equipo = input("Tiene equipo (si/no): ")
horas = int(input("Ingrese sus horas de practica semanales: "))
torneos = int(input("Ingrese el número de torneos previos: "))

es_elegible = (edad >=13) and (puntaje >=20)

# Estructura de categorización
if not es_elegible:
    print("\nNo es elegible para participar en el torneo.")
    if edad < 13:
        print("Debe tener al menos 13 años")
    if puntaje < 20:
        print("Puntaje insuficiente para participar en el torneo")
else:
    if ((puntaje >= 80 and horas >= 10) or (torneos >= 5 and puntaje >= 70)):
        categoria = "Profesional"
        beneficios = "Acceso VIP y premios especiales"

    elif (puntaje >= 60 and (horas >= 5 or torneos >= 2)):
        categoria = "Semi-profesional"
        beneficios = "Acceso a torneos avanzados"

    elif puntaje >= 40:
        categoria = "Amateur Avanzado"
        beneficios = "Entrenamiento adicional"

    else:
        categoria = "Amateur"
        beneficios = "Participación estándar"

    # Determinación del modo de participación
    if tiene_equipo == "si" and not (categoria == "Amateur"):
        modo = "En equipo"
    else:
        modo = "Individual"

    # Mostrar resultados
    print("\n===== RESULTADOS =====")
    print("Categoría asignada:", categoria)
    print("Modo de participación:", modo)
    print("Beneficios:", beneficios)