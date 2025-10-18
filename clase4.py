# Operadores de comparación y lógicos.

booleano = 10 == 10
print("El valor de la comparación es:", booleano)
booleano = 10 == 11
print("El valor de la comparación es:", booleano)
booleano = 10 != 11
print("El valor de la comparación es:", booleano)

# Operadores lógicos
booleano_and = (10 == 10) and (11 > 10)
print("El valor de la comparación AND es:", booleano_and)

# Tabla de verdad del operador AND
# print("Tabla de verdad del operador AND:")
# print("True and True =", True and True)
# print("True and False =", True and False)
# print("False and True =", False and True)
# print("False and False =", False and False)

booleano_or = (10 == 10) or (11 < 10)
print("El valor de la comparación OR es:", booleano_or)
# Tabla de verdad del operador OR
# print("Tabla de verdad del operador OR:")
# print("True or True =", True or True)
# print("True or False =", True or False)
# print("False or True =", False or True)
# print("False or False =", False or False)

# negación
booleano_not = not (10 == 10)
print("El valor de la comparación NOT es:", booleano_not)


# Control de flujo
edad = int(input("Por favor ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

edad = int(input("Por favor ingresa tu edad: "))
dinero = float(input("Por favor ingresa la cantidad de dinero que tienes: "))
if edad >= 18:
    if dinero >= 10000:
        print("Puede entrar a la fiesta.")
    else:
        print("No tiene suficiente dinero.")
else:
    print("No puede entrar a la fiesta, es menor de edad.")


edad = int(input("Por favor ingresa tu edad: "))
dinero = float(input("Por favor ingresa la cantidad de dinero que tienes: "))
if edad >= 18 and dinero >= 10000:
    print("Puede entrar a la fiesta.")
else:
    print("No puede entrar a la fiesta.")

Ciclo for

for i in range(5):
    print("Iteración número:", i)

tabla_de_multiplicar = int(input("Por favor ingresa un número para ver su tabla de multiplicar: "))
for i in range(0, 11):
    resultado = tabla_de_multiplicar * i
    print(f"{tabla_de_multiplicar} x {i} = {resultado}")

lista_uno = [2, 4, 6, 8, 10]
for numero in lista_uno:
    print("Número de la lista:", numero)

diccionario = { 1: "uno", 2: "dos", 3: "tres" }
for clave in diccionario:
    print(f"Clave: {clave}, Valor: {diccionario[clave]}")

for clave in diccionario.keys():
    print(f"Clave: {clave}")

for dato in diccionario.items():
    print(dato)

for dato in diccionario.values():
    print(dato)

# Ciclo while

monedas = 5
while monedas > 0:
    print("Tienes", monedas, "monedas.")
    monedas -= 1 # Equivalente a monedas = monedas - 1

peticion = input("Escribe 's' para terminar el ciclo: ")
while peticion != 's':
    peticion = input("Escribe 's' para terminar el ciclo: ")

# range
for numero in range(10):
    print("Número:", numero)

for numero in range(3, 10):
    print("Número:", numero)

for numero in range(1, 10, 2):
    print("Número impar:", numero)


for numero in range(2, 10, 2):
    print("Número par:", numero)

# Crear una lista con números del 1 al 99 usando range

lista = list(range(1, 100))
print("Lista de números del 1 al 99:", lista)

# Usar enumerate para obtener índice e ítem de una lista

lista = ["a", "b", "c", "d", "e"]
for indice, item in enumerate(lista):
    print(f"Índice: {indice}, Ítem: {item}")

# zip para combinar varias listas

nombres = ["Ana", "Luis", "Carlos", "Marta"]
edades = [23, 30, 18, 25]
ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla"]

cobinacion_uno = zip(nombres, edades)
print(f"Combinación de nombres y edades: {cobinacion_uno}")
combinacion_dos = list(zip(nombres, edades, ciudades))
print(f"Combinación de nombres, edades y ciudades: {combinacion_dos}")

for nombre, edad, ciudad in combinacion_dos:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

# Máximos y mínimos

menor = min(5, 10, -3, 0, 8)
print("El valor mínimo es:", menor)
mayor = max(5, 10, -3, 0, 8)
print("El valor máximo es:", mayor)


dicionario = {  "Juan": 25, "Ana": 30, "Luis": 20 }
edad_menor = min(dicionario.values())
print("La edad mínima en el diccionario es:", edad_menor)
edad_mayor = max(dicionario.values())
print("La edad máxima en el diccionario es:", edad_mayor)

# Random
from random import randint, choice
numero_aleatorio = randint(1, 100000000000000000)
print("Número aleatorio generado:", numero_aleatorio)

# choice
elementos = ["rojo", "azul", "verde", "amarillo"]
for r in range(3):
    elemento_aleatorio = choice(elementos)
    print("Elemento aleatorio seleccionado:", elemento_aleatorio)
    for elemento in elementos:
        if elemento == elemento_aleatorio:
            elemento_aleatorio = choice(elementos)
            print("Elemento aleatorio seleccionado:", elemento_aleatorio)
            # posición = elementos.index(elemento)
            sacar = elementos.index(elemento)
            elementos.pop(sacar)

# Compresión de listas
palabra = "comprensión"
lista = []
for letra in palabra:
    lista.append(letra) 
print("Lista creada con bucle for:", lista)

lista_dos = [letra for letra in palabra]
print("Lista creada con bucle for:", lista_dos)
