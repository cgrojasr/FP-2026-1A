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

Ejercicio3()