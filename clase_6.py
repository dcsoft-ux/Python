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
