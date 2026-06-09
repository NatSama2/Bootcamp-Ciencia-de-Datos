def numeros(num1, num2, num3):
    maximo = max(num1, num2, num3)
    minimo = min(num1, num2, num3)
    promedio = round((num1 + num2 + num3)/3,2)

    print(f'El número maximo es {maximo}')
    print(f'El número minimo es {minimo}')
    print(f'El promedio es {promedio}')

n1 = float(input("Ingrese el 1er número: "))
n2 = float(input("Ingrese el 2do número: "))
n3 = float(input("Ingrese el 3er número: "))

numeros(n1, n2, n3)