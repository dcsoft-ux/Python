
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


