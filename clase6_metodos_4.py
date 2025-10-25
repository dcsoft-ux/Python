
# Persona

class Persona:
    corazon = 1
    pulmones = 2
    def __init__(self, nombre, color_ojos, color_pelo, password):
        self.nombre = nombre
        self.color_ojos = color_ojos
        self.color_pelo = color_pelo
        self.__password = password  # Atributo privado

    def saltar(self, metros):
        if(metros<0):
            print("No se puede saltar una distancia negativa")
        elif metros>1 and metros<=2:
            print(f"{self.nombre} ha saltado {metros} metros.")
        else:
            print("No puedo saltar esa distancia.")

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")

    def cambiar_color_ojo(self, nuevo_color):
        self.color_ojos = nuevo_color
        print(f"{self.nombre} ha cambiado el color de ojos a {nuevo_color}.")

    def tomar_agua(self, litros):
        print(f"{self.nombre} ha tomado {litros} litros de agua.")
    # Metodo para acceder al atributo privado
    def get_password(self):
        return self.__password
    # Metodo para modificar el atributo privado
    def set_password(self, nuevo_password):
        print("Aqui va el tamaño de la contraseña: ",len(nuevo_password))
        while(len(nuevo_password) <= 12):
            print("La contraseña no es válida.")
            nuevo_password = input("Escribe una nueva contraseña: ")

        self.__password = nuevo_password

nombre = "Andres"
color_ojos = "Verde"
color_pelo = "Negro"
persona1 = Persona(nombre, color_ojos, color_pelo, "123456")
# atributo
print("Color de ojor original : ", persona1.color_ojos)
# Metodo
persona1.cambiar_color_ojo("Azul")
# atributo privado
print(persona1.get_password())
password1 = input("Escribe la nueva contraseña: ")
persona1.set_password(password1)
print(persona1.get_password())