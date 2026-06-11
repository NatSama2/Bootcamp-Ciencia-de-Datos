print("AVENTURA GAMING: ¡EL PORTAL MÁGICO")
print("----------------------------------")
print("¿Tienes lo necesario para cruzar el portal?")
print("Necesitas 100 punos para avanzar al siguiee nivel")
print()

#Pedir los punto al jugaor
puntos = int(input("Aventurero!!! ¿Cuantos puntos has conseguido?: "))

if puntos >= 100:
    print("¡PORTAL ABIERO!")
    print("Has desbloqueado el siguiene nivel")

#Agregamos logros segun puntos
if puntos >= 150:
    print("LEGENDARIO")
    print("Has conseguido el amuleto dorado")

if puntos >= 120 and puntos < 150:
    print("INCREIBLE")
    print("Has conseguido una espada mágica")

if puntos >= 100 and puntos < 120:
    print("BIEN HECHO")
    print("Has conseguido una poción de energía")

print(f'Tus puntos fueron: {puntos}')
print("\U00002B50")