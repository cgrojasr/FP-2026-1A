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

Ejercicio1_Reto()
