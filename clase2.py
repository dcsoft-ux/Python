#
# Tipos de datos en Python
#

# Entero
entero = 10
entero_negativos = -5

# Decimales
decimal = 3.14
decimal_negativo = -2.71

# Booleanos
booleano_verdadero = True
booleano_falso = False

# type() para verificar los tipos de datos
print(type(entero))
print(entero)

#
# Métodos en Python
#

# Quitar espacios en blanco
nombre = "    Carlos Andres     "
# Método para quitar espacios strip()
print(nombre.strip())
# Método para quitar espacios rstrip()
print(nombre.rstrip())
# Método para quitar espacios lstrip()
print(nombre.lstrip())

# Primera letra en mayuscula capitalize()
nombre = "carlos andres"
print(nombre.capitalize())

# Todas las letras en mayuscula upper()
print(nombre.upper())
nombre = nombre.upper()
print(nombre)

# Todas las letras en minuscula lower()
print(nombre.lower())

# Encontrar la posición de una letra o palabra find()
frase = "Hola, mi nombre es Carlos Andres"
print(frase.find("i"))
print(frase.find("nombre"))

# Dentro del texto hay números isalnum()
frase2 = "Andres0"
print(frase2.isalnum())

# Solo letras isalpha()
frase3 = "Andres"
print(frase3.isalpha())

# Solo números isdigit()
frase4 = "12345"
print(frase4.isdigit())

# Código ASCII ord() y chr()
palabra_assii = "50800"
print(palabra_assii.isascii())

# Si todo está en minúsculas
palabra_minusculas = "andres"
print(palabra_minusculas.islower())

# Si todo está en mayúsculas
palabra_mayusculas = "ANDRES"
print(palabra_mayusculas.isupper())

# Reemplazar una palabra por otra replace()
frase5 = "Hola, mi nombre es Carlos Andres"
print(frase5.replace("Carlos", "Andres"))

#
# Cadenas de carácteres (Strings)
#

# Van entre comillas simples o dobles
cadena1 = 'Hola, mi nombre es Carlos Andres'
cadena2 = "Hola, mi nombre es Carlos Andres"
print(type(cadena1))
print(type(cadena2))

# Longitud de una cadena len()
print(len(cadena1))
print(len(cadena2))

# Cadena de carácteres es un arreglo
nombre = "Carlos"
print(nombre[2]) # Imprime la letra 'r'

# Slicing (rebanar)
print(nombre[2:5]) # Imprime 'rlo'

# Slicing con paso [inicio:fin:paso]
frase = "Hola, mi nombre es Carlos Andres"
print(len(frase))
print(frase[8:12:3])
print(frase[4:20:4])


#
# Variables
#

numero1 = 10
numero2 = 5
letra = "A"
palabra = "Hola"
numero3 = "3.14"

print(numero1 + numero2)
print(palabra + letra)
print(palabra + letra + numero3)

numero_entero = 10
numero_decimal = 3.14
numero_entero2 = 2

print(numero_entero + numero_decimal)
print(numero_entero / numero_entero2)


#
# Conversión Variables
#

numero_uno = 340
numero_dos = 34
print(type(numero_uno))
print(type(numero_dos))
resultado = numero_uno / numero_dos
print(type(resultado))

numero_decimal = 3.14
print(type(numero_decimal))
numero_entero = int(numero_decimal)
print(type(numero_entero))

edad = input("Escriba su edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))

edad = int(input("Escriba su edad: "))
print(type(edad))

x = 10
y = 5

print("La suma es: ", x + y)
print("La suma es: 'y'=", y, "'x'=", x, "x+y=", x+y)
print(f"La suma es: 'y'= {y} 'x'= {x} x+y= {x+y}")
print("La suma es: 'y'= {} 'x'= {} x+y= {}".format(y, x, x+y))

#
# Operadores Aritméticos
#

a = 10
b = 2

# Suma
print(a + b)

# Resta
print(a - b)

# Multiplicación
print(a * b)

# División
print(a / b)  # Resultado decimal

# División entera
print(a // b) # Resultado entero

# Módulo (residuo de la división)
print(a % b)

# Potencia
print(a ** b)

# Orden
# PEMDAS
# Paréntesis - Exponentes - Multiplicación - División - Suma - resultado
# Va de izquierda a derecha


#
# Asignación
#

x = 10
print(x)
x += 3 # x = x + 3
print(x)
x -= 2 # x = x - 2
print(x)
x *= 4 # x = x * 4
print(x)
x /= 3 # x = x / 2
print(x)
x //= 2 # x = x // 2
print(x)
x %= 3 # x = x % 3
print(x)
x **= 2 # x = x ** 2
print(x)

#
# Lógicos
#

a = 10
b = 5
c = 2
print(a > b)  # True
print(a < b)  # False
print(a >= b) # True
print(a <= b) # False
print(a == b) # False
print(a != b) # True