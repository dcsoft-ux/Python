import re


def saludo(nombre):
    '''Función que recibe un nombre y devuelve un saludo personalizado.'''
    print(f"Hola, {nombre}")

saludo("Andres")

def suma(a, b):
    '''Función que recibe dos números y devuelve su suma.'''
    return a + b

def multiplicacion(a, b):
    '''Función que recibe dos números y devuelve su producto.'''
    return a * b

resultado = suma(3, 5)
print(f"La suma es: {resultado}")
resultado_mult = multiplicacion(4, 6)
print(f"La multiplicación es: {resultado_mult}")

def numeroDeTresCrifras(numero):
    '''Función que verifica si un número tiene tres cifras.'''
    return numero in range(100, 1000)

resultado_tres_cifras = numeroDeTresCrifras(456)
print(f"¿El número tiene tres cifras?:  {resultado_tres_cifras}")

resultado_tres_cifras = numeroDeTresCrifras(55)
print(f"¿El número tiene tres cifras?:  {resultado_tres_cifras}")

def numeroDeTresCrifras(lista_numeros):
    '''Función que verifica si un número de la lista tiene tres cifras.'''
    lista_resultados_positivos = []
    lista_resultados_negativos = []
    for numero in lista_numeros:
        if numero in range(100, 1000):
            print(f"El número {numero} tiene tres cifras.")
            lista_resultados_positivos.append(numero)
        else:
            lista_resultados_negativos.append(numero)
    return (lista_resultados_positivos, lista_resultados_negativos)
lista = [12, 5, 678, 45]
resultado_lista = numeroDeTresCrifras(lista)
print(f"¿Algún número de la lista tiene tres cifras?:  {resultado_lista}")


precios_cafe = [('Expreso', 5000), ('Americano', 3500), ('Latte', 4000), ('Cappuccino', 4500)]
for cafe, precio in precios_cafe:
    print(cafe)
    print(f"El precio del {cafe} es de {precio*0.19+precio} pesos.")

def cafeMasCaro(lista):
    '''Función que encuentra el café más caro en una lista de tuplas (nombre, precio).'''
    precioMayor = 0
    cafeMasCaro = ""
    for cafe, precio in lista:
        if precio > precioMayor:
            precioMayor = precio
            cafeMasCaro = cafe
    return (cafeMasCaro, precioMayor)
print(cafeMasCaro(precios_cafe))

from random import shuffle
import random

palitos = ["-","--","---","----","-----"]

def mezclarPalitos(lista):
    '''Función que mezcla una lista de palitos.'''
    shuffle(lista)
    return lista

def suerte():
    intento=''
    while intento not in ['1','2','3','4','5']:
        intento = input("Elige un número del 1 al 5: ")
    return int(intento)-1

def verificarSuerte(lista, intento):
    '''Función que verifica si el intento del usuario es correcto.'''
    if lista[intento] == "-":
        print("¡Perdiste! Has encontrado el palito más corto.")
    else:
        print("Ganaste, inténtalo de nuevo.")

palitos_mezclados = mezclarPalitos(palitos)
intento_usuario = suerte()
verificarSuerte(palitos_mezclados, intento_usuario)