temperatura = float(input("Ingresa la temperatura: "))

if temperatura > 37.5:
    print("Tienes fiebre")
elif temperatura >= 37 and temperatura <= 37.5:
    print("Temperatura elevada")
elif temperatura >= 36 and temperatura < 37:
    print("Temperatura normal")
else:
    print("Temperatura baja")