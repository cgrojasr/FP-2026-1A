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

# Una empresa tiene como reglamento dar aumento de sueldo a sus trabajadores todos los años, 
# el porcentaje de aumento está dado de acuerdo al tipo de trabajador: Gerente (g) o empleado (e). 
# Los gerentes reciben un aumento del 14% anual y los empleados reciben el 8% anual. 
# Cada 4 años en vez de 14% reciben 18% y en vez de 8% reciben 12% (dependiendo del tipo de trabajador). 
# Desarrollar los módulos que determinen el sueldo que tendrá un trabajador después de N años y el porcentaje 
# de aumento de sueldo que ha obtenido comparando su sueldo original y su sueldo después de N años. 
# Tenga en cuenta que los aumentos obtenidos van a su sueldo. 
#  
# Se le solicita lo siguiente:
# Calculo del sueldo después de N años					
# Calcular el porcentaje de aumento después de N años.				
# Calcular la suma del sueldo de un gerente y de un empleado después de N años. 

def Enunciado_2():
    sueldo_inicial_gerente = float(input("Ingrese el sueldo inicial del gerente: "))
    sueldo_inicial_empleado = float(input("Ingrese el sueldo inicial del empleado: "))
    años = int(input("Ingrese la cantidad de años: "))
    sueldo_final_gerente = calcular_sueldo_final(sueldo_inicial_gerente, 'g', años)
    sueldo_final_empleado = calcular_sueldo_final(sueldo_inicial_empleado, 'e', años)
    porcentaje_aumento_gerente = round(((sueldo_final_gerente - sueldo_inicial_gerente) / sueldo_inicial_gerente) * 100,2)
    porcentaje_aumento_empleado = round(((sueldo_final_empleado - sueldo_inicial_empleado) / sueldo_inicial_empleado) * 100,2)
    print(f"El sueldo del gerente después de {años} años es: {sueldo_final_gerente} soles")
    print(f"El porcentaje de aumento del gerente después de {años} años es: {porcentaje_aumento_gerente}%")
    print(f"El sueldo del empleado después de {años} años es: {sueldo_final_empleado} soles")
    print(f"El porcentaje de aumento del empleado después de {años} años es: {porcentaje_aumento_empleado}%")
    print(f"La suma del sueldo de un gerente y de un empleado después de {años} años es: {sueldo_final_gerente + sueldo_final_empleado} soles")

def calcular_sueldo_final(sueldo_inicial, tipo_trabajador, años):
    sueldo_final = sueldo_inicial
    for año in range(1, años + 1, 1):
        if tipo_trabajador == 'g':
            if año % 4 == 0:
                sueldo_final += (18 / 100) * sueldo_final
            else:
                sueldo_final += (14 / 100) * sueldo_final
        elif tipo_trabajador == 'e':
            if año % 4 == 0:
                sueldo_final += (12 / 100) * sueldo_final
            else:
                sueldo_final += (8 / 100) * sueldo_final
    return round(sueldo_final, 2) 

# Enunciado_2()