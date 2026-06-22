# Que reciba dos parámetros (nombre y edad), que muestre el mensaje dependiendo de la Edad:
# Edad entre 0 a 2 muestre mensaje: nombre + “ es un infante”
# Edad entre 3 a 10 muestre mensaje: nombre + “ es niño”
# Edad entre 11 a 13 muestre mensaje: nombre + “ es puber”
# Edad entre 14 a 18 muestre mensaje: nombre + “ es adolescente”
# Edad entre 19 a 59 muestre mensaje: nombre + “ es adulto”
# Edad mayor a 59 muestre mensaje:  nombre + “ es anciano”

def Ejercicio4():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))

    if 0 <= edad <= 2:
        print(f"{nombre} es un infante")
    elif 3 <= edad <= 10:
        print(f"{nombre} es niño")
    elif 11 <= edad <= 13:
        print(f"{nombre} es puber")
    elif 14 <= edad <= 18:
        print(f"{nombre} es adolescente")
    elif 19 <= edad <= 59:
        print(f"{nombre} es adulto")
    elif edad > 59:
        print(f"{nombre} es anciano")
    else:
        print("Edad no válida")

# Ejercicio4()

# El presidente de un club de fútbol requiere calcular el sueldo de sus jugadores si se tiene 
# como dato la edad y nacionalidad del jugador.
# 
# Además, se sabe que el sueldo se calcula de la siguiente manera:
# Sueldo fijo 2500 soles
# Si es extranjero recibe un bono de 500 soles
# Si la edad está entre 15 y 20 el sueldo se incrementa en 1400 soles
# Si la edad está entre 21 y 25 el sueldo se incrementa en 1500 soles
# Si la edad está entre 26 y 30 el sueldo se incrementa en 1200 soles
# En otros casos el sueldo se incrementará en 800 soles.

# Se le pide elaborar un programa en Ruby que permita determinar el sueldo de un jugador 
# si se tienen como datos su edad y nacionalidad (E: Extranjero; N: Nacional).

def Ejercicio5_1():
    sueldo_fijo = 2500
    nacionalidad = input("Ingrese la nacionalidad del jugador (E: Extranjero; N: Nacional): ")
    if nacionalidad.upper() not in ["E", "N"]:
        print("Error: Nacionalidad no válida. Debe ser 'E' o 'N'.")
        return
    edad = int(input("Ingrese la edad del jugador: "))
    if edad < 0:
        print("Error: La edad no puede ser negativa.")
        return

    if nacionalidad.upper() == "E":
        sueldo_fijo += 500

    if 15 <= edad <= 20:
        sueldo_fijo += 1400
    elif 21 <= edad <= 25:
        sueldo_fijo += 1500
    elif 26 <= edad <= 30:
        sueldo_fijo += 1200
    else:
        sueldo_fijo += 800

    print(f"El sueldo del jugador es: {sueldo_fijo} soles")

# Ejercicio5_1()

# -----------------------------------------
# RETO 1 - Sistema de Becas (con input)
# -----------------------------------------

def beca_excelencia(promedio, tercio_superior, creditos):
    return promedio >= 17 and tercio_superior == True and creditos >= 18

def beca_socioeconomica(ingreso, promedio):
    return ingreso < 1500 and promedio >= 13

def beca_rendimiento(promedio, creditos):
    return (promedio >= 14 and promedio <= 16) and creditos >= 15

def asignar_beca():
    promedio = float(input("Ingrese el promedio del estudiante: "))
    ingreso = float(input("Ingrese el ingreso familiar: "))
    creditos = int(input("Ingrese la cantidad de créditos matriculados: "))
    tercio = input("¿Pertenece al tercio superior? (S/N): ")

    if tercio.upper() == "S":
        tercio_superior = True
    elif tercio.upper() == "N":
        tercio_superior = False
    else:        
        print("Error: Respuesta no válida para el tercio superior. Debe ser 'S' o 'N'.")
        return

    if beca_excelencia(promedio, tercio_superior, creditos):
        print("Beca asignada: Beca Excelencia")
    elif beca_socioeconomica(ingreso, promedio):
        print("Beca asignada: Beca Socioeconómica")
    elif beca_rendimiento(promedio, creditos):
        print("Beca asignada: Beca Rendimiento")
    else:
        print("No obtiene beca")

# Llamada al método principal
# asignar_beca()

# EJERCICIO 3
# Que reciba dos números A y B y nos indique si A es múltiplo de B. (V o F)
# -----------------------------------------

def es_multiplo():
    A = int(input("Ingrese el número A: "))
    B = int(input("Ingrese el número B: "))
    if B == 0:
        return False
    print(A % B == 0)

# Ejemplo de uso
# print(es_multiplo(10, 2))  # True
# print(es_multiplo(10, 3))  # False

# es_multiplo()

# Una tienda de venta de productos agrícolas al por mayor le ha solicitado que elabore 
# un programa que permita generar la boleta de venta de los clientes que en ella compran.
# Cuando el cliente realiza la compra se le solicita el tipo de producto y la cantidad 
# de sacos que comprará.
# Los productos que vende dicha tienda son:
# Tipo	    Producto	Precio x saco
# P	        Papa	    20.5
# C	        Cebolla	    19.4
# L	        Limón	    32.3
# A	        Ají	        16.5
# M	        Maíz	    19.8

# Se le solicita que elabore un programa en Ruby que reciba como datos el tipo de producto y la cantidad de sacos que el cliente comprará y nos determine e imprima el monto que deberá pagar este.
# Debe validar los datos de entrada para una correcta ejecución de su programa.

def Ejercicio5_2():
    tipo_producto = input("Ingrese el tipo de producto (P: Papa, C: Cebolla, L: Limón, A: Ají, M: Maíz): ")
    cantidad_sacos = int(input("Ingrese la cantidad de sacos que comprará: "))

    if tipo_producto.upper() == "P":
        precio_por_saco = 20.5
    elif tipo_producto.upper() == "C":
        precio_por_saco = 19.4
    elif tipo_producto.upper() == "L":
        precio_por_saco = 32.3
    elif tipo_producto.upper() == "A":
        precio_por_saco = 16.5
    elif tipo_producto.upper() == "M":
        precio_por_saco = 19.8
    else:
        print("Error: Tipo de producto no válido.")
        return
    
    if cantidad_sacos < 0:
        print("Error: La cantidad de sacos no puede ser negativa.")
        return

    monto_total = precio_por_saco * cantidad_sacos
    print(f"El monto total a pagar es: {round(monto_total, 2)} soles")

# Ejercicio5_2()

# ------------------------------------------------
# RETO 2 - Sistema de Control de Acceso (input)
# ------------------------------------------------

def validar_acceso():
    rol = input("Ingrese el rol (admin / empleado / visitante): ").lower()
    hora = int(input("Ingrese la hora de ingreso (0-23): "))
    autorizacion = input("¿Tiene autorización especial? (S/N): ")
    dia = input("¿Es día laboral? (S/N): ")

    if autorizacion.upper() == "S":
        autorizacion_bool = True
    elif autorizacion.upper() == "N":
        autorizacion_bool = False
    else:
        print("Error: Respuesta no válida para autorización especial. Debe ser 'S' o 'N'.")
        return
    
    if dia.upper() == "S":
        dia_laboral = True
    elif dia.upper() == "N":
        dia_laboral = False
    else:
        print("Error: Respuesta no válida para día laboral. Debe ser 'S' o 'N'.")
        return

    if rol == "admin":
        print("Acceso permitido (Administrador)")

    elif rol == "empleado":
        if 6 <= hora <= 22:
            print("Acceso permitido (Empleado en horario)")
        elif autorizacion_bool:
            print("Acceso permitido (Empleado con autorización especial)")
        else:
            print("Acceso denegado (Empleado fuera de horario)")

    elif rol == "visitante":
        if 8 <= hora <= 18 and dia_laboral and autorizacion_bool:
            print("Acceso permitido (Visitante autorizado)")
        else:
            print("Acceso denegado (Visitante sin requisitos)")

    else:
        print("Rol no reconocido")

# Llamada al método
# validar_acceso()


# Dados dos números, nos indique quien es mayor, menor o si son iguales.
def Ejercicio1():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: El valor ingresado no es un número válido.")
        return

    if num1 > num2:
        print(f"{num1} es mayor que {num2}")
    elif num1 < num2:
        print(f"{num1} es menor que {num2}")
    else:
        print("Ambos números son iguales")


# Ejercicio1()

# Que reciba un numero y muestre un mensaje indicando si es par o no.
def Ejercicio2():
    try:
        numero = int(input("Ingrese un número entero: "))
    except ValueError:
        print("Error: El valor ingresado no es un número entero válido.")
        return

    if numero % 2 == 0:
        print(f"{numero} es un número par")
    else:
        print(f"{numero} es un número impar")

# Ejercicio2()

# Una empresa de software vende aplicaciones para celulares (iPhone y Android) y 
# requiere un programa que genere el resumen por cada venta realizada.
# Los productos que vende dicha empresa son:

# Tipo	Producto	Tipo de Celular	Precio x unidad
# O	    Oficina	    iPhone	        50.60
#                   Android	        20.30
# J	    Juegos	    iPhone	        90.80
#                   Android	        40.50
# U	    Utilitarios	iPhone	        60.50
#                   Android	        30.60

# Asimismo, el programa solicita la cantidad de aplicaciones que el cliente va a comprar.
# Se le solicita que elabore un programa en Ruby que reciba como datos el tipo de producto, 
# el tipo de celular (I: iPhone; A: Android) y la cantidad de unidades que el cliente comprará y 
# nos determine e imprima el monto que deberá pagar este.
# Debe validar los datos de entrada para una correcta ejecución de su programa.

def Ejercicio5_III():
    tipo_producto = input("Ingrese el tipo de producto (O: Oficina, J: Juegos, U: Utilitarios): ")

    if tipo_producto.upper() not in ["O", "J", "U"]:
        print("Error: Tipo de producto no válido. Debe ser 'O', 'J' o 'U'.")
        return
    
    tipo_celular = input("Ingrese el tipo de celular (I: iPhone, A: Android): ")

    if tipo_celular.upper() not in ["I", "A"]:
        print("Error: Tipo de celular no válido. Debe ser 'I' o 'A'.")
        return

    cantidad_unidades = input("Ingrese la cantidad de unidades que comprará: ")

    try:
        cantidad_unidades = int(cantidad_unidades)
        if cantidad_unidades < 0:
            print("Error: La cantidad de unidades no puede ser negativa.")
            return
    except ValueError:
        print("Error: La cantidad de unidades debe ser un número entero.")
        return

    if tipo_producto.upper() == "O":
        if tipo_celular.upper() == "I":
            precio_por_unidad = 50.60
        elif tipo_celular.upper() == "A":
            precio_por_unidad = 20.30
        else:
            print("Error: Tipo de celular no válido.")
            return
    elif tipo_producto.upper() == "J":
        if tipo_celular.upper() == "I":
            precio_por_unidad = 90.80
        elif tipo_celular.upper() == "A":
            precio_por_unidad = 40.50
        else:
            print("Error: Tipo de celular no válido.")
            return
    elif tipo_producto.upper() == "U":
        if tipo_celular.upper() == "I":
            precio_por_unidad = 60.50
        elif tipo_celular.upper() == "A":
            precio_por_unidad = 30.60
        else:
            print("Error: Tipo de celular no válido.")
            return
    else:
        print("Error: Tipo de producto no válido.")
        return

    monto_total = precio_por_unidad * cantidad_unidades
    print(f"El monto total a pagar es: {round(monto_total, 2)} soles")

# Ejercicio5_III()

# --------------------------------------------------------
# RETO 3 - Clasificador de Riesgo de Salud (con input)
# --------------------------------------------------------

def clasificar_riesgo():
    edad = input("Ingrese la edad del paciente: ")
    try:
        edad = int(edad)
        if edad < 0:
            print("Error: La edad no puede ser negativa.")
            return
    except ValueError:
        print("Error: La edad debe ser un número entero.")
        return

    imc = input("Ingrese el IMC del paciente: ")
    try:
        imc = float(imc)
        if imc < 0:
            print("Error: El IMC no puede ser negativo.")
            return
    except ValueError:
        print("Error: El IMC debe ser un número.")
        return

    enfermedad = input("¿Tiene enfermedad preexistente? (S/N): ")
    if enfermedad.upper() == "S":
        enfermedad_bool = True
    elif enfermedad.upper() == "N":
        enfermedad_bool = False
    else:
        print("Error: Respuesta no válida para enfermedad preexistente. Debe ser 'S' o 'N'.")
        return
    
    actividad = input("¿Realiza actividad física regular? (S/N): ")
    if actividad.upper() == "S":
        actividad_bool = True
    elif actividad.upper() == "N":
        actividad_bool = False
    else:
        print("Error: Respuesta no válida para actividad física regular. Debe ser 'S' o 'N'.")
        return

    if edad >= 60 or imc >= 30 or (enfermedad_bool and not actividad_bool):
        print("Clasificación: Riesgo Alto")

    elif (40 <= edad <= 59) or (25 <= imc <= 29) or (enfermedad_bool and actividad_bool):
        print("Clasificación: Riesgo Medio")

    elif edad < 40 and imc < 25 and not enfermedad_bool:
        print("Clasificación: Riesgo Bajo")

    else:
        print("Clasificación: Riesgo Indeterminado")

# Llamada al método
clasificar_riesgo()
