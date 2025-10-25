
# Persona

class Persona:
    corazon = 1
    pulmones = 2
    def __init__(self, nombre, color_ojos, color_pelo):
        self.nombre = nombre
        self.color_ojos = color_ojos
        self.color_pelo = color_pelo

    def saltar(self, metros):
        print(f"{self.nombre} ha saltado {metros} metros.")

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")
    
    def tomar_agua(self, litros):
        print(f"{self.nombre} ha tomado {litros} litros de agua.")

nombre = input("Escribe el nombre de la persona: ")
color_ojos = input("Escribe el color de ojos de la persona: ")
color_pelo = input("Escribe el color de pelo de la persona: ")
persona1 = Persona(nombre, color_ojos, color_pelo)
# atributo
print("Nombre:", persona1.nombre)
# Metodo
persona1.saludar()
metros = int(input("¿Cuántos metros quieres que salte? "))
persona1.saltar(metros)
litros = int(input("¿Cuántos litros de agua ha tomado? "))
persona1.tomar_agua(litros)