"""
Desafío: ¡Crea tu primer juego completamente funcional!

El programa le pedirá al usuario que ingrese su nombre, y luego le dirá algo como:

“Bueno, nombre, he pensado un número entre 1 y 100, y tienes ocho intentos para adivinar cuál crees que es.”

En cada intento, el jugador ingresará un número, y el programa podrá responder de cuatro maneras distintas:

Número fuera de rango:
Si el número ingresado es menor que 1 o mayor que 100, el programa indicará que ese valor no está permitido.

Número demasiado bajo:
Si el número es menor que el número secreto, el programa avisará que la respuesta es incorrecta y que el número elegido es más bajo que el secreto.

Número demasiado alto:
Si el número es mayor que el número secreto, el programa lo informará de la misma forma.

¡Adivinaste!

Si el usuario acierta el número secreto, el programa anunciará su victoria e indicará en cuántos intentos lo logró.

Si el jugador no acierta en el primer intento, el programa volverá a pedir otro número, y así sucesivamente, hasta que gane o se le agoten los ocho intentos.

"""
from random import randint

numero_secreto = randint(1, 100)
nombre = input("Por favor ingresa tu nombre: ")
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes ocho intentos para adivinar cuál crees que es.")
numero = int(input("Ingresa tu primer intento: "))
contador = 1
while numero != numero_secreto:
    if numero < 1 or numero > 100:
        print("Número fuera de rango. Por favor ingresa un número entre 1 y 100.")
        contador += 1
    elif numero < numero_secreto:
        print("Número demasiado bajo.")
        contador += 1
    elif numero > numero_secreto:
        print("Número demasiado alto.")
        contador += 1
    numero = int(input("Ingresa tu primer intento: "))
    if contador > 8:
        print(f"Lo siento, {nombre}. Se te han agotado los intentos. El número secreto era {numero_secreto}.")
        break
    if numero == numero_secreto:
        print(f"¡Adivinaste, {nombre}! Has ganado en {contador} intentos.")

