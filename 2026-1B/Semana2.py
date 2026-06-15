# Dados dos números, que determine la suma, resta, multiplicación, división, potencia
def Ejercicio1():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = round(num1 / num2, 2) if num2 != 0 else "No se puede dividir por cero"
    potencia = num1 ** num2
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")
    print(f"Potencia: {potencia}")

# Ejercicio1()

# Que calcule y muestre el menor número de monedas de 5, 2 y 1 para desglosar una cantidad C, de Soles. 
# Por ejemplo, si C fuese 23, entonces la cantidad de monedas de 5 sería 4, de 2 sería 1 y de 1 sería 1.
def Ejercicio5():
    C = int(input("Ingrese la cantidad en Soles: "))
    monedas_5 = C // 5
    C = C % 5
    monedas_2 = C // 2
    monedas_1 = C % 2
    print(f"Monedas de 5: {monedas_5}")
    print(f"Monedas de 2: {monedas_2}")
    print(f"Monedas de 1: {monedas_1}")

# Ejercicio5()

# Que lea el valor de un ángulo en radianes y calcule y muestre su valor en grados, minutos y segundos.
def Ejercicio7():
    import math
    radianes = float(input("Ingrese el ángulo en radianes: "))
    grados = math.degrees(radianes)
    minutos = (grados - int(grados)) * 60
    segundos = (minutos - int(minutos)) * 60
    print(f"Grados: {int(grados)}")
    print(f"Minutos: {int(minutos)}")
    print(f"Segundos: {round(segundos, 2)}")

# Ejercicio7()


# 🧠 Ejercicio 1 — Conversor y Clasificador de Datos Numéricos Enunciado Desarrollar un programa que reciba como 
# entrada tres valores en formato texto (str): Un número entero Un número decimal Un número que representa una
#  potencia (base y exponente separados por un guion, por ejemplo “3-4”) El programa debe: Convertir cada valor al 
# tipo de dato correspondiente (int, float). Calcular: 
# El doble del entero La mitad del decimal La potencia base^exponente 
# Mostrar los resultados usando print.

# Ejercicio 1 - Conversor y Clasificador

# Entradas en formato texto
def Ejercicio1_Reto():
    texto_entero = input("Ingrese un número entero: ")
    # Validar número entero
    try:        
        numero_entero = int(texto_entero)
    except ValueError:
        print("Error: El valor ingresado para el número entero no es válido.")
        return
    texto_decimal = input("Ingrese un número decimal: ")
    # Validar número decimal
    try:
        numero_decimal = float(texto_decimal)
    except ValueError:
        print("Error: El valor ingresado para el número decimal no es válido.")
        return
    
    texto_potencia = input("Ingrese una potencia (base-exponente): ")
    # Validar formato de potencia
    if "-" not in texto_potencia:
        print("Error: El formato de la potencia es incorrecto. Debe ser 'base-exponente'.")
        return
    # Validar que base y exponente sean números
    partes = texto_potencia.split("-")
    if len(partes) != 2:
        print("Error: El formato de la potencia es incorrecto. Debe contener exactamente un guion.")
        return
    
    try:
        base = int(partes[0])
        exponente = int(partes[1])
    except ValueError:
        print("Error: La base y el exponente deben ser números enteros.")
        return

    # Conversión de tipos
    numero_entero = int(texto_entero)
    numero_decimal = float(texto_decimal)

    # Separación de la potencia
    partes = texto_potencia.split("-")
    base = int(partes[0])
    exponente = int(partes[1])

    # Operaciones
    doble_entero = numero_entero * 2
    mitad_decimal = numero_decimal / 2
    resultado_potencia = base ** exponente

    # Impresión de resultados
    print("Doble del entero:", doble_entero)
    print("Mitad del decimal:", mitad_decimal)
    print("Resultado de la potencia:", resultado_potencia)

# Ejercicio1_Reto()

# Que determine el Área de un circulo
def Ejercicio2():
    import math
    radio = float(input("Ingrese el radio del círculo: "))
    area = round(math.pi * (radio ** 2), 2)
    print(f"El área del círculo es: {area}")

# Ejercicio2()

# Que teniendo como dato una hora expresada en segundos (t), 
# nos calcule y muestre la cantidad de horas, minutos y segundos contenidos en dicha hora. Por ejemplo, 
# si t fuese 3879, entonces el número de horas sería 1, los minutos serían 4 y los segundos serían 

def Ejercicio6():
    t = int(input("Ingrese la cantidad de segundos: "))
    horas = t // 3600
    minutos = (t % 3600) // 60
    segundos = t % 60
    print(f"Horas: {horas}, Minutos: {minutos}, Segundos: {segundos}")

# Ejercicio6()

# Que lea las coordenadas (x1, y1) y (x2, y2) de dos puntos y nos determine e imprima la distancia 
# entre ellos y el ángulo que forma la recta que los une con la horizontal.
def Ejercicio8():
    import math
    x1 = int(input("Ingrese la coordenada x1: "))
    y1 = int(input("Ingrese la coordenada y1: "))
    x2 = int(input("Ingrese la coordenada x2: "))
    y2 = int(input("Ingrese la coordenada y2: "))
    
    distancia = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
    angulo = round(math.degrees(math.atan2(y2 - y1, x2 - x1)), 2)

    print(f"Distancia entre los puntos: {distancia}")
    print(f"Ángulo con la horizontal: {angulo} grados")

# Ejercicio8()


def Ejercicio2_Reto():
    # Ejercicio 2 - Desglose de tiempo
    texto_segundos = input("Ingrese la cantidad de segundos: ")

    # Conversión
    segundos_totales = int(texto_segundos)

    if segundos_totales <= 0:
        print("Error: el valor debe ser mayor que cero.")
    else:
        horas = segundos_totales // 3600
        minutos = (segundos_totales % 3600) // 60
        segundos = segundos_totales % 60

        # Conversión a texto para construir el mensaje
        mensaje = "El tiempo es " + str(horas) + " horas, " + str(minutos) + " minutos y " + str(segundos) + " segundos."

        print(mensaje)

# Ejercicio2_Reto()

# Que solicite la temperatura en grados Celsius y la convierta a grados Fahrenheit.
def Ejercicio3():
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = round((celsius * 9/5) + 32, 2)
    print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# Ejercicio3()

# Que teniendo como dato una hora expresada en segundos (t), nos calcule y muestre la cantidad de horas, 
# minutos y segundos contenidos en dicha hora. Por ejemplo, si t fuese 3879, entonces el número de horas sería 1, 
# los minutos serían 4 y los segundos serían 

def Ejercicio6():
    t = int(input("Ingrese la cantidad de segundos: "))
    horas = t // 3600
    minutos = (t % 3600) // 60
    segundos = t % 60
    print(f"Horas: {horas}, Minutos: {minutos}, Segundos: {segundos}")

# Ejercicio6()

# Que lea las coordenadas (x1, y1) y (x2, y2) de dos puntos y nos determine e imprima la distancia 
# entre ellos y el ángulo que forma la recta que los une con la horizontal.

def Ejercicio8():
    import math
    x1 = int(input("Ingrese la coordenada x1: "))
    y1 = int(input("Ingrese la coordenada y1: "))
    x2 = int(input("Ingrese la coordenada x2: "))
    y2 = int(input("Ingrese la coordenada y2: "))
    
    distancia = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
    angulo = round(math.degrees(math.atan2(y2 - y1, x2 - x1)), 2)

    print(f"Distancia entre los puntos: {distancia}")
    print(f"Ángulo con la horizontal: {angulo} grados")

Ejercicio8()

