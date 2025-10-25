
# Persona

class Persona:
    corazon = 1
    pulmones = 2
    def __init__(self, nombre, color_ojos, color_pelo):
        self.nombre = nombre
        self.color_ojos = color_ojos
        self.color_pelo = color_pelo

    def saltar(self, metros):
        if(metros<0):
            print("No se puede saltar una distancia negativa")
        elif metros>1 and metros<=2:
            print(f"{self.nombre} ha saltado {metros} metros.")
        else:
            print("No puedo saltar esa distancia.")

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")
    
    def tomar_agua(self, litros):
        print(f"{self.nombre} ha tomado {litros} litros de agua.")

nombre = "Andres"
color_ojos = "Verde"
color_pelo = "Negro"
persona1 = Persona(nombre, color_ojos, color_pelo)
# atributo
print("Nombre:", persona1.nombre)
# Metodo
persona1.saltar(-5)
persona1.saltar(1.5)
persona1.saltar(3)