"""
Juego del Ahorcado (versión por consola)

El objetivo de este programa es crear una versión simple del clásico juego del ahorcado, pero sin utilizar elementos gráficos.

El sistema elegirá una palabra secreta de forma aleatoria y mostrará al jugador una serie de guiones (_), donde cada guion representa una letra de la palabra oculta.

En cada turno, el jugador deberá ingresar una letra:

Si la letra está en la palabra secreta, el programa mostrará en qué posiciones aparece.

Si la letra no se encuentra en la palabra, el jugador pierde una vida.

En el juego tradicional, cada error dibuja una parte del ahorcado, pero en esta versión de consola simplemente se mostrará un contador de vidas restantes.
El jugador comenzará con seis vidas, y perderá una en cada intento incorrecto.

El juego terminará cuando:

- El jugador adivine toda la palabra (gana).

- El jugador pierda todas las vidas antes de descubrirla (pierde).

Guía para desarrollar el programa

Importar módulos necesarios

Utiliza el método choice del módulo random para que el programa pueda seleccionar una palabra al azar desde una lista que crearás al inicio.

Definir funciones auxiliares
Crea las funciones que consideres necesarias para organizar el código, por ejemplo:

Una función para pedir una letra al usuario.

Una función que valide que el usuario ingresó una letra válida (solo una y del alfabeto).

Una función que verifique si la letra está en la palabra secreta.

Una función para mostrar el progreso del jugador (letras descubiertas y vidas restantes).

Una función para comprobar si el jugador ganó o perdió.

Estructura del programa

Primero define todas las funciones.

Luego escribe el bloque principal del programa, que controle la secuencia del juego: inicializar variables, mostrar el estado actual, solicitar letras y verificar las condiciones de victoria o derrota.

Consejo

Organiza el código de forma clara y modular. Piensa en las funciones como pequeñas piezas que, al unirse, hacen que el juego funcione correctamente.
"""
from random import choice

palabras = ['python', 'desarrollo', 'programacion', 'ahorcado', 'consola']
letras_correctas = []
letras_incorrectas = []
vidas = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(palabras):
    '''Función que elige una palabra al azar de la lista.'''
    palabra_elegida = choice(palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

def pedir_letra():
    '''Función que pide una letra al usuario y la valida.'''
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while not es_valida:
        letra_elegida = input("Escriba una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No es una letra válida.")
    return letra_elegida

def mostrar_consola(palabra_elegida):
    '''Función que muestra el progreso del jugador.'''
    lista_oculta = []
    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))

def verificar_letra(letra_elegida, palabra_elegida, vidas, aciertos):
    fin = False
    if letra_elegida in palabra_elegida and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        aciertos += 1
    elif letra_elegida in palabra_elegida and letra_elegida in letras_correctas:
        print("Ya has elegido esa letra. Intenta con otra.")
        vidas -= 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    if vidas == 0:
        fin = perder()
    elif aciertos == letras_unicas:
        fin = ganar(palabra_elegida)
    return vidas, fin, aciertos

def perder():
    print("¡Te has quedado sin vidas!  ¡Has perdido!")
    print("la palabra era: ", palabra_elegida)
    return True

def ganar(palabra_elegida):
    mostrar_consola(palabra_elegida)
    print("¡Felicidades! ¡Has adivinado la palabra: ", palabra_elegida)
    return True

palabra_elegida, letras_unicas = elegir_palabra(palabras)


while not juego_terminado:
    print("\n" + "*" * 50 + "\n")
    mostrar_consola(palabra_elegida)
    print("\n")
    print("Letras incorrectas: ", ' -  '.join(letras_incorrectas))
    print(f"Vidas restantes: {vidas}")
    letra_elegida = pedir_letra()
    vidas, juego_terminado, aciertos = verificar_letra(letra_elegida, palabra_elegida, vidas, aciertos)
    juego_terminado = juego_terminado