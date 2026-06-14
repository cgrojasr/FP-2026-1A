# Una empresa desea una aplicación para contabilizar la cantidad de dígitos repetidos dentro de una cadena de números ingresados. 
# Por ejemplo, si tengo el siguiente número 45776574367321367112 y pido que el número a contabilizar sea el 7 entonces debo obtener 5 como valor resultante. 
# La cifra indicada puede tener diferente longitud.

# Desarrollar un subprograma que permita contar la cantidad total de dígitos.
# Desarrollar un subprograma que permita contar la cantidad de números repetidos de acuerdo al digito indicado.
def Ejercicio1():
    numero = input("Ingrese una cadena de números: ")
    digito = input("Ingrese el dígito a contabilizar: ")
    # Validar que la cadena de numeros solo contenga dígitos
    while not numero.isdigit():
        print("La cadena debe contener solo dígitos. Intente nuevamente.")
        numero = input("Ingrese una cadena de números: ")
    # Validar que el dígito a contabilizar sea un dígito y que sea de un solo carácter
    while not digito.isdigit() or len(digito) != 1:
        print("El dígito a contabilizar debe ser un dígito. Intente nuevamente.")
        digito = input("Ingrese el dígito a contabilizar: ")
    cantidad_total_digitos(numero)
    print("---------------------------------------------------------")
    cantidad_digitos_repetidos(numero, digito)

def cantidad_total_digitos(numero):
    print(f"La cantidad total de dígitos en la cadena es: {len(numero)}")

def cantidad_digitos_repetidos(numero, digito):
    cantidad = numero.count(digito)
    print(f"La cantidad de dígitos {digito} en la cadena es: {cantidad}")

# Ejercicio1()

# Una empresa tiene como reglamento dar aumento de sueldo a sus trabajadores todos los años, 
# el porcentaje de aumento está dado de acuerdo con el tipo de trabajador: Gerente (g) o empleado (e). 
# Los gerentes reciben un aumento del 14% anual y los empleados reciben el 8% anual. 
# Cada 4 años en vez de 14% reciben 18% y en vez de 8% reciben 12% (dependiendo del tipo de trabajador). 
# Desarrollar los módulos que determinen el sueldo que tendrá un trabajador después de N años y el porcentaje 
# de aumento de sueldo que ha obtenido comparando su sueldo original y su sueldo después de N años. 
# Tenga en cuenta que los aumentos obtenidos van a su sueldo. 

# Se le solicita lo siguiente:
# a.	Cálculo del sueldo después de N años					
# b.	Calcular el porcentaje de aumento después de N años.

def Ejercicio2():
    sueldo_inicial = float(input("Ingrese el sueldo inicial del trabajador: "))
    tipo_trabajador = input("Ingrese el tipo de trabajador (g para gerente, e para empleado): ")
    while tipo_trabajador.lower() not in ['g', 'e']:
        print("Tipo de trabajador inválido. Intente nuevamente.")
        tipo_trabajador = input("Ingrese el tipo de trabajador (g para gerente, e para empleado): ")
    años = int(input("Ingrese la cantidad de años: "))
    sueldo_final = calcular_sueldo_despues_de_n_años(sueldo_inicial, tipo_trabajador, años)
    print(f"El sueldo después de {años} años es: {sueldo_final:.2f}")
    print("---------------------------------------------------------")
    porcentaje_aumento = calcular_porcentaje_aumento(sueldo_inicial, sueldo_final)
    print(f"El porcentaje de aumento después de {años} años es: {porcentaje_aumento:.2f}%")

def calcular_sueldo_despues_de_n_años(sueldo_inicial, tipo_trabajador, años):
    sueldo = sueldo_inicial
    for i in range(1, años + 1):
        if tipo_trabajador.lower() == 'g':
            if i % 4 == 0:
                sueldo += sueldo * 0.18
            else:
                sueldo += sueldo * 0.14
        else:   
            if i % 4 == 0:
                sueldo += sueldo * 0.12
            else:
                sueldo += sueldo * 0.08
    return sueldo

def calcular_porcentaje_aumento(sueldo_inicial, sueldo_final):
    aumento = sueldo_final - sueldo_inicial
    porcentaje_aumento = (aumento / sueldo_inicial) * 100
    return porcentaje_aumento

# Ejercicio2()

# Un banco establece que la clave secreta para acceso a sus cajeros automáticos debe ser un número de 
# cuatro o más dígitos y que la suma de los dos dígitos que se encuentran en la 3 y 4 posición (posición de centena 
# y millar) sea par. Determinar si una clave cumple con la condición.

def Ejercicio3():
    clave = input("Ingrese la clave secreta (4 o más dígitos): ")
    while not clave.isdigit() or len(clave) < 4:
        print("La clave debe ser un número de cuatro o más dígitos. Intente nuevamente.")
        clave = input("Ingrese la clave secreta (4 o más dígitos): ")
    if (int(clave[2]) + int(clave[3])) % 2 == 0:
        print("La clave cumple con la condición.")
    else:
        print("La clave no cumple con la condición.")

# Ejercicio3()

# Una reconocida empresa de venta de gas natural desea una aplicación que permita calcular el total a pagar por una persona u empresa 
# dependiendo de los metros cúbicos (m3) consumidos y su tipo de contrato. 
# Existen dos tipos de contrato:
# El contrato "residencial" (r) permite que los 28 primeros m3 sean gratis, los siguientes 122 se paguen a tarifa de 2.1 soles y a 
# partir del m3 123 en adelante se paguen a 1.5 soles. 

# Por otro lado, el contrato "comercial" (c) permite que los 400 primeros m3 se paguen a 1.8 soles y a partir del 401 se pague a 2.5 soles. 
# a.	Desarrollar un subprograma que permita a un usuario con contrato residencial calcular el total a pagar
# b.	Desarrollar un subprograma que permita a un usuario con contrato comercial calcular el total a pagar
# c.	Desarrollar un subprograma que, recibiendo la cantidad de m3 y el tipo de contrato pueda retornar el total a pagar. 

def Ejercicio4():
    m3_consumidos = float(input("Ingrese la cantidad de metros cúbicos consumidos: "))
    tipo_contrato = input("Ingrese el tipo de contrato (r para residencial, c para comercial): ")
    while tipo_contrato.lower() not in ['r', 'c']:
        print("Tipo de contrato inválido. Intente nuevamente.")
        tipo_contrato = input("Ingrese el tipo de contrato (r para residencial, c para comercial): ")
    total_a_pagar = calcular_total_a_pagar(m3_consumidos, tipo_contrato)
    print(f"El total a pagar es: {total_a_pagar:.2f} soles")

def calcular_total_a_pagar_residencial(m3_consumidos):
    if m3_consumidos <= 28:
        return 0
    elif m3_consumidos <= 150:
        return (m3_consumidos - 28) * 2.1
    else:
        return (122 * 2.1) + ((m3_consumidos - 150) * 1.5)
    
def calcular_total_a_pagar_comercial(m3_consumidos):
    if m3_consumidos <= 400:
        return m3_consumidos * 1.8
    else:
        return (400 * 1.8) + ((m3_consumidos - 400) * 2.5)

def calcular_total_a_pagar(m3_consumidos, tipo_contrato):
    if tipo_contrato.lower() == 'r':
        return calcular_total_a_pagar_residencial(m3_consumidos)
    else:   
        return calcular_total_a_pagar_comercial(m3_consumidos)

# Ejercicio4()

# El supermercado UNO está premiando a sus clientes que compran por un monto mayor a 800 soles, el premio consiste en un juego, donde el cliente, 
# extrae de una urna un papel que tiene un numero de varias cifras (el número de cifras es variado), como máximo tiene 9 dígitos. 

# El cliente va a recibir un premio de acuerdo a la cantidad de unos que aparece en el papel.
# •	Si no hay ningún digito uno, no recibe ningún premio. 
# •	Si hay un digito uno va a recibir el 1% de descuento de la compra realizada.
# •	Si hay dos dígitos uno va a recibir el 2% de descuento de la compra realizada.
# •	Si hay tres dígitos uno va a recibir el 3% de descuento de la compra realizada.
# •	Si hay cuatro dígitos uno va a recibir el 4% de descuento de la compra realizada.
# •	Y así sucesivamente hasta llegar a los 9 dígitos uno.
# •	Si la cantidad de dígitos uno es 2 o múltiplo de 2 recibe un descuento adicional de 50 soles.

# a.	Calcular el descuento total que recibe un cliente
# b.	Calcular el importe a pagar.

def Ejercicio5():
    monto_compra = float(input("Ingrese el monto de la compra: "))
    while monto_compra <= 800:
        print("El monto de la compra debe ser mayor a 800 soles para recibir un premio. Intente nuevamente.")
        monto_compra = float(input("Ingrese el monto de la compra: "))
    numero_premio = input("Ingrese el número del papel extraído (máximo 9 dígitos): ")
    while not numero_premio.isdigit() or len(numero_premio) > 9:
        print("El número del papel debe ser un número de máximo 9 dígitos. Intente nuevamente.")
        numero_premio = input("Ingrese el número del papel extraído (máximo 9 dígitos): ")
    descuento_total = calcular_descuento_total(monto_compra, numero_premio)
    print(f"El descuento total que recibe el cliente es: {descuento_total:.2f} soles")
    importe_a_pagar = monto_compra - descuento_total
    print(f"El importe a pagar es: {importe_a_pagar:.2f} soles")

def calcular_descuento_total(monto_compra, numero_premio):
    cantidad_unos = numero_premio.count('1')
    descuento = (cantidad_unos / 100) * monto_compra
    if cantidad_unos > 0 and cantidad_unos % 2 == 0:
        descuento += 50
    return descuento

# Ejercicio5()

# El Hospital “Mi Buen Jesús”, lo contrata para que implemente un programa informático, que permita al personal médico calcular en cuantos días un 
# paciente puede eliminar de su cuerpo la medicina ingerida. 
# El caso específico es el siguiente: Un paciente recibe una cantidad de una medicina. Cada día el 20% de la cantidad de medicina presente en su 
# cuerpo es eliminada. El programa debe calcular:		              
# a.	Cuanta medicina queda en el cuerpo después del día D
# b.	Cuantos días tardará el cuerpo en eliminar el X% o más de la cantidad original de la medicina que tenía en el cuerpo.

# Ejemplo para la parte b
# Para 80 unidades de medicina y eliminar el 60% de esta medicina, es decir para eliminar como mínimo 48 unidades de medicina, debe pasar 5 días

def Ejercicio6():
    cantidad_medicina = float(input("Ingrese la cantidad de medicina ingerida: "))
    dia_d = int(input("Ingrese el día D para calcular la cantidad de medicina restante: "))
    porcentaje_eliminar = float(input("Ingrese el porcentaje X para calcular los días necesarios para eliminar esa cantidad: "))
    medicina_restante = calcular_medicina_restante(cantidad_medicina, dia_d)
    print(f"La cantidad de medicina que queda en el cuerpo después del día {dia_d} es: {medicina_restante:.2f} unidades")
    dias_necesarios = calcular_dias_para_eliminar(cantidad_medicina, porcentaje_eliminar)
    print(f"El cuerpo tardará {dias_necesarios} días en eliminar el {porcentaje_eliminar}% o más de la cantidad original de la medicina.")

def calcular_medicina_restante(cantidad_medicina, dia_d):
    for _ in range(dia_d):
        cantidad_medicina *= 0.8
    return cantidad_medicina

def calcular_dias_para_eliminar(cantidad_medicina, porcentaje_eliminar):
    cantidad_a_eliminar = (porcentaje_eliminar / 100) * cantidad_medicina
    cantidad_restante = cantidad_medicina
    dias = 0
    while cantidad_restante > (cantidad_medicina - cantidad_a_eliminar):
        cantidad_restante *= 0.8
        dias += 1
    return dias

Ejercicio6()