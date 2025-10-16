"""
Ejercicio: Cálculo de comisión de ventas
Objetivo:
Crear un programa que pida el nombre de un empleado y el valor total de sus ventas del mes, calcule el 13 % de comisión, y muestre el resultado redondeado.
Instrucciones del ejercicio
    1. Solicita al usuario que ingrese el nombre del empleado.
    2. Solicita el valor total de las ventas del empleado en el mes.
    3. Convierte el valor de las ventas a número entero (ya que input() devuelve texto).
    4. Calcula la comisión aplicando el 13 %.
    5. Redondea el resultado con round().
    6. Muestra el nombre del empleado y la comisión calculada en pantalla.
"""

# Solicitar el nombre del empleado
nombre_empleado = input("Ingrese el nombre del empleado: ")
# Solicitar el valor total de las ventas del empleado en el mes
ventas_mes = int(input("Ingrese el valor total de las ventas del mes: "))
# Calcular la comisión aplicando el 13 %
comision = ventas_mes * 0.13
# Redondear el resultado
comision_redondeada = round(comision,1)
# Mostrar el nombre del empleado y la comisión calculada en pantalla
print(f"El empleado {nombre_empleado} tiene una comisión de: {comision_redondeada}")