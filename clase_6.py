# class Pajaro:
#     pass
# mi_pajaro = Pajaro()
# print(mi_pajaro)
# print(type(mi_pajaro))

# Atributos
class Pajaro:
    alas = 2
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

color = input("Escribe el color del pájaro: ")
especie = input("Escribe la especie del pájaro: ")
mi_pajaro = Pajaro(color, especie)
print(mi_pajaro)
print(type(mi_pajaro))
print("Color:", mi_pajaro.color)
print("Especie:", mi_pajaro.especie)
print("Alas:", mi_pajaro.alas)

# Persona

class Persona:
    corazon = 1
    pulmones = 2
    def __init__(self, nombre, color_ojos, color_pelo):
        self.nombre = nombre
        self.color_ojos = color_ojos
        self.color_pelo = color_pelo

nombre = input("Escribe el nombre de la persona: ")
color_ojos = input("Escribe el color de ojos de la persona: ")
color_pelo = input("Escribe el color de pelo de la persona: ")
persona1 = Persona(nombre, color_ojos, color_pelo)
print("Nombre:", persona1.nombre)
print("Color de ojos:", persona1.color_ojos)
print("Color de pelo:", persona1.color_pelo)
print("Corazón:", persona1.corazon)
print("Pulmones:", persona1.pulmones)
