class Estudiante:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
        self.notas = []

ana = Estudiante("Ana", 15)
jose = Estudiante("Jose", 40)

print(f"Nombre: {ana.nombre}")
print(f"Edad: {ana.edad}")
print(f"Notas: {ana.notas}")

print(f"Nombre: {jose.nombre}")
print(f"Edad: {jose.edad}")
print(f"Notas: {jose.notas}")