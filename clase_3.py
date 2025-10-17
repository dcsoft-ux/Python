texto = "Esto es un texto de ejemplo"
print(texto[5])
print(texto[-3])
print(texto.index("e"))
print(texto.index("un"))
print(texto.rindex("e"))
texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
print(texto[5:11])
print(texto[5:20:3])
palabra_uno= "Hola"
palabra_dos= "Mundo"
resultado = " $ ".join([palabra_uno, palabra_dos])
print(resultado)
print(texto.find("Z"))
print(texto.replace("Ñ","AQUI ESTABA UNA LETRA"))
poema = """La programación en mi vida
Es como el agua bendita
Que aparte que da vida
Mi alma codifica
vida
Autor: Miguel Ángel Teherán García"""
print('vida' in poema)

listas = [1, 2, 3, 4, 5, 6, 7]
print(listas)
print(listas[3])
# Sacar el último elemento de la lista
listas.pop()
print(listas)
# Sacar un elemento de una posición específica
listas.pop(2)
print(listas)
# Agregar un elemento al final de la lista
listas.append(9)
print(listas)

# ordenar una lista
listas.sort()
print(listas)

# ordenar una lista de forma inversa
listas.reverse()
print(listas)

# Diccionarios

diccionario = {"casa": "Lugar donde vivo",
              "direccion": "La ubicación de mi casa",
            }
print(diccionario)
print(diccionario["casa"])
print(diccionario["direccion"])

dicionarioEjemplo = {
    'claveUno':['a','b','c'], 
    'claveDos':['d','e','f']
    }
print(dicionarioEjemplo)
print(dicionarioEjemplo['claveUno'][1])
print(dicionarioEjemplo['claveUno'][1].upper())
