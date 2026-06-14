# Que solicite la temperatura en grados Celsius y la convierta a grados Fahrenheit.
def ejercicio2():
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")  

# ejercicio2()

# Que lea el valor de un ángulo en radianes y calcule y muestre su valor en grados, minutos y segundos.
def ejercicio7():
    import math
    radianes = float(input("Ingrese el valor del ángulo en radianes: "))
    grados = math.degrees(radianes)
    
    grados_enteros = int(grados)
    minutos = (grados - grados_enteros) * 60
    minutos_enteros = int(minutos)
    segundos = round((minutos - minutos_enteros) * 60, 2)
    
    print(f"{radianes} radianes son {grados_enteros} grados, {minutos_enteros} minutos y {segundos} segundos.")

# ejercicio7()

# Que lea las coordenadas (x1, y1) y (x2, y2) de dos puntos y nos determine e imprima 
# la distancia entre ellos y el ángulo que forma la recta que los une con la horizontal.
def ejercicio8():
    import math
    x1 = float(input("Ingrese la coordenada x del primer punto: "))
    y1 = float(input("Ingrese la coordenada y del primer punto: "))
    x2 = float(input("Ingrese la coordenada x del segundo punto: "))
    y2 = float(input("Ingrese la coordenada y del segundo punto: "))
    
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    angulo_rad = math.atan2(y2 - y1, x2 - x1)
    angulo_deg = math.degrees(angulo_rad)
    
    print(f"La distancia entre los puntos es: {round(distancia,2)}")
    print(f"El ángulo que forma la recta con la horizontal es: {round(angulo_deg,2)} grados")

ejercicio8()