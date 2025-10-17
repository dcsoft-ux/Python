"""
Laboratorio: Creación de un Analizador de Texto en Python
1. Objetivo del laboratorio

Aplicar los conocimientos sobre strings, listas, tuplas, métodos de cadenas, indexación y tipos de datos, desarrollando un programa completo que analice un texto ingresado por el usuario y muestre distintos resultados.

Al finalizar este laboratorio, serás capaz de:

Manipular y transformar texto usando métodos de str.

Aplicar estructuras de datos adecuadas para el procesamiento de información.

Implementar lógica condicional, conteo, e indexación.

Combinar todo lo aprendido en un programa funcional y legible.

2. Material previo o conocimientos requeridos

Antes de iniciar, asegúrate de dominar:

Operaciones básicas con strings (concatenación, .lower(), .count(), .split(), .join()).

Uso de listas y sus métodos (.append(), .reverse()).

Indexación en strings y listas (texto[0], texto[-1]).

Tipos de datos básicos: str, int, list, bool, dict.

Estructuras condicionales (if, else).

Función input() y función print().

3. Descripción general

Se desarrollará un programa que:

Solicita al usuario un texto cualquiera.

Pide tres letras a elección del usuario.

Realiza cinco análisis sobre el texto.

Muestra los resultados de manera ordenada.

4. Entradas

El programa pedirá:

Dato solicitado	Descripción	Ejemplo de entrada
Texto principal	Cualquier frase, párrafo o poema	"Me gusta aprender Python todos los días"
Letra 1	Primera letra elegida por el usuario	"a"
Letra 2	Segunda letra elegida por el usuario	"t"
Letra 3	Tercera letra elegida por el usuario	"p"
"""

texto = input("Por favor ingresa un texto: ")
texto_lower = texto.lower()
letra1 = input("Por favor ingresa la primera letra que quieres buscar: ")
letra2 = input("Por favor ingresa la segunda letra que quieres buscar: ")
letra3 = input("Por favor ingresa la tercera letra que quieres buscar: ")
letra1_lower = letra1.lower()
letra2_lower = letra2.lower()
letra3_lower = letra3.lower()
# Análisis 1: Contar cuántas veces aparece la letra 1 en el texto
conteo_letra1 = texto_lower.count(letra1_lower)
# Análisis 2: Contar cuántas veces aparece la letra 2 en el texto
conteo_letra2 = texto_lower.count(letra2_lower)
# Análisis 3: Contar cuántas veces aparece la letra 3 en el texto
conteo_letra3 = texto_lower.count(letra3_lower)

# Análisis 4: Encontrar la primera posición de la letra 1 en el texto
posicion_letra1 = texto_lower.find(letra1_lower)
# Análisis 5: Encontrar la primera posición de la letra 2 en el texto
posicion_letra2 = texto_lower.find(letra2_lower)
# Análisis 6: Encontrar la primera posición de la letra 3 en el texto
posicion_letra3 = texto_lower.find(letra3_lower)
# Mostrar resultados
print(f"\nAnálisis del texto ingresado:\n")
print(f"1. La letra '{letra1}' aparece {conteo_letra1} veces en el texto.")
print(f"2. La letra '{letra2}' aparece {conteo_letra2} veces en el texto.")
print(f"3. La letra '{letra3}' aparece {conteo_letra3} veces en el texto.")

# lista_resultados = [conteo_letra1, conteo_letra2, conteo_letra3]
diccionario_resultados = {
    posicion_letra1: letra1,
    posicion_letra2: letra2,
    posicion_letra3: letra3
}
print(diccionario_resultados)
letras_ordenadas = sorted(diccionario_resultados.items())
print(letras_ordenadas)
