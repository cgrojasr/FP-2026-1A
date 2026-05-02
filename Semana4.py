# El supermercado UNO está premiando a sus clientes que compran por un monto mayor a 800 soles, 
# el premio consiste en un juego, donde el cliente, extrae de una urna un papel que tiene un numero de varias 
# cifras (el número de cifras es variado), como máximo tiene 9 dígitos. 
#  
# El cliente va a recibir un premio de acuerdo a la cantidad de unos que aparece en el papel.
#  
# Si no hay ningún digito uno, no recibe ningún premio. 
# Si hay un digito uno va a recibir el 1% de descuento de la compra realizada.
# Si hay dos dígitos uno va a recibir el 2% de descuento de la compra realizada.
# Si hay tres dígitos uno va a recibir el 3% de descuento de la compra realizada.
# Si hay cuatro dígitos uno va a recibir el 4% de descuento de la compra realizada.
# Y así sucesivamente hasta llegar a los 9 dígitos uno.
# Si la cantidad de  dígitos uno es 2 o múltiplo de 2 recibe un descuento adicional de 50 soles.
#  
# Calcular el descuento total que recibe un cliente
# Calcular el importe a pagar.

class Enunciado_1:
    def __init__(self):
        monto_compra = float(input("Ingrese el monto de la compra realizada: "))
        if(monto_compra > 800):
            numero_papel = input("Ingrese el número del papel extraído: ")
            if len(numero_papel) > 9:
                print("El número del papel no puede tener más de 9 dígitos.")
                return
            descuento_total = calcular_descuento(monto_compra, numero_papel)
            importe_a_pagar = monto_compra - descuento_total
            print(f"El descuento total que recibe el cliente es: {descuento_total} soles")
            print(f"El importe a pagar por el cliente es: {importe_a_pagar} soles")
        else:
            print("El monto de la compra no es mayor a 800 soles, no recibe ningún premio.")

def calcular_descuento(monto_compra, numero_papel):
    # cantidad_unos = numero_papel.count('1')
    cantidad_unos = 0
    for digito in numero_papel:
        if digito == '1':
            cantidad_unos += 1
    descuento = (cantidad_unos / 100) * monto_compra
    if cantidad_unos % 2 == 0 and cantidad_unos != 0:
        descuento += 50
    return descuento

Enunciado_1()