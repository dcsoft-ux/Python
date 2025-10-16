"""
Vas a crear tu primer programa real aplicando todo lo que has aprendido hasta ahora.

Imagina esta situación: un amigo te pide ayuda porque acaba de abrir su tienda virtual, y quiere que crees un pequeño programa que le permita simular una compra sencilla. Él quiere que el programa tenga una pequeña presentación que muestre el nombre del programa, que pida algunos datos de la compra y que además calcule el valor total con IVA incluido.

Tu misión es ayudarlo creando un programa en Python que haga lo siguiente:

Pida al usuario el nombre del programa (por ejemplo: CompraFácil, TiendaExpress, etc.).

Pida el nombre del objeto que desea comprar (por ejemplo: “computador”, “camisa”, “libro”).

Pida el valor de la compra sin IVA (solo un número).

Pida el porcentaje de IVA que desea aplicar (por ejemplo, 19).

Calcule el valor del IVA y el total a pagar.

Finalmente, muestre un mensaje con formato creativo, en al menos dos líneas, donde se muestren todos los datos combinados, por ejemplo:

Bienvenido a "CompraFácil"
Has adquirido un computador por $200000
IVA (19%): $38000
Total a pagar: $238000
¡Gracias por tu compra!


Pistas y recomendaciones:

Usa la función input() para pedir los datos al usuario.

Convierte los valores numéricos con float() o int() antes de hacer cálculos.

Usa \n para hacer saltos de línea dentro del print().

Intenta que el nombre del programa se muestre entre comillas.

Sé creativo con el mensaje final.
"""

nombre_del_programa = input("Escriba el nombre del programa: ")
nombre_objeto = input("Escriba el nombre del objeto que desea comprar: ")
valor = int(input("Escriba el valor de la compra sin IVA: "))
porcentaje_iva = int(input("Escriba el porcentaje de IVA que desea aplicar: "))
valor_iva = (valor * porcentaje_iva) / 100
total_a_pagar = valor + valor_iva


print("Bienvenido a: " + '"' + nombre_del_programa + '"')
print("Has adquirido un",nombre_objeto,"por $",valor)
print("IVA (",porcentaje_iva,"%) : $",valor_iva)
print("Total a pagar: $",total_a_pagar)
print("¡Gracias por tu compra!")