import statistics

def ingresar_notas():
    nombre = input("Ingrese el nombre del estudiante: ")
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i} (1.0 a 7.0): "))
                if 1.0 <= nota <= 7.0:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 1.0 y 7.0. Intente nuevamente.")
            except ValueError:
                print("Ingrese un número válido.")
    return nombre, notas

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def determinar_estado(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    else:
        return "Reprobado"

def obtener_estadisticas(notas):
    mediana = statistics.median(notas)
    try:
        moda = statistics.mode(notas)
    except statistics.StatisticsError:
        moda = "No hay una moda única"
    desviacion = statistics.stdev(notas)
    return {
        "mediana": mediana,
        "moda": moda,
        "desviacion": desviacion
    }

def mostrar_resultados(nombre, notas, promedio, estado, estadisticas):
    print("\n===== RESULTADOS =====")
    print(f"Estudiante: {nombre}")
    print(f"Notas: {notas}")
    print(f"Promedio: {promedio:.1f}")
    print(f"Estado: {estado}")
    print("\n--- Estadísticas ---")
    print(f"Mediana: {estadisticas['mediana']:.1f}")
    if isinstance(estadisticas["moda"], str):
        print(f"Moda: {estadisticas['moda']}")
    else:
        print(f"Moda: {estadisticas['moda']:.1f}")
    print(f"Desviación estándar: {estadisticas['desviacion']:.1f}")
    print("======================")

def main():
    nombre, notas = ingresar_notas()
    promedio = calcular_promedio(notas)
    estado = determinar_estado(promedio)
    estadisticas = obtener_estadisticas(notas)
    mostrar_resultados(nombre, notas, promedio, estado, estadisticas)

if __name__ == "__main__":
    main()