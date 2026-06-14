# Ejercicio de la clase
def comparacion_dos_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    if num1 > num2:
        print(f"{num1} es mayor que {num2}.")
    elif num1 < num2:
        print(f"{num1} es menor que {num2}.")
    else:
        print("Ambos números son iguales.")

# comparacion_dos_numeros()

# Ejercicios de la semana 3
# Ejercicio 3
# Que reciba dos números A y B y nos indique si A es múltiplo de B. (V o F)
def es_multiplo():
    A = float(input("Ingrese el primer número: "))
    B = float(input("Ingrese el segundo número: "))
    
    if B == 0:
        print("El segundo número no puede ser cero.")
    elif A % B == 0:
        print(f"{A} es múltiplo de {B}.")
    else:
        print(f"{A} no es múltiplo de {B}.")

# es_multiplo()

# Ejercicio 5 - Enunciado 1
class Enunciado_1:
    def __init__(self):
        edad = int(input("Ingrese su edad del jugador: "))
        extranjero = input("¿El jugador es extranjero? (s/n): ").upper()
        sueldo_fijo = 2500
        bono_extranjero = calcular_bono_extranjero(extranjero)
        bono_edad = calcular_bono_edad(edad)
        sueldo_total = sueldo_fijo + bono_extranjero + bono_edad
        print(f"El sueldo total del jugador es: {sueldo_total} soles")

def calcular_bono_extranjero(extranjero):
    if extranjero == 'S':
        return 500
    else:
        return 0

def calcular_bono_edad(edad):
    if edad >= 15 and edad <= 20:
        return 1400
    elif edad >= 21 and edad <= 25:
        return 1500
    elif edad >= 26 and edad <= 30:
        return 1200
    else:
        return 800
    
# Enunciado_1()

#Ejercicio 4
# Que reciba dos parámetros (nombre y edad), que muestre el mensaje dependiendo de la Edad:
# Edad entre 0 a 2 muestre mensaje: nombre + “ es un infante”
# Edad entre 3 a 10 muestre mensaje: nombre + “ es niño”
# Edad entre 11 a 13 muestre mensaje: nombre + “ es puber”
# Edad entre 14 a 18 muestre mensaje: nombre + “ es adolescente”
# Edad entre 19 a 59 muestre mensaje: nombre + “ es adulto”
# Edad mayor a 69 muestre mensaje:  nombre + “ es anciano”

class ejercicio_4():
    def __init__(self):
        self.nombre = input("Ingrese el nombre de la persona: ")
        self.edad = int(input("Ingrese la edad de la persona: "))
        clasificar_edad(self.nombre, self.edad)

def clasificar_edad(nombre, edad):
    if edad >= 0 and edad <= 2:
        print(f"{nombre} es un infante.")
    elif edad >= 3 and edad <= 10:
        print(f"{nombre} es niño.")
    elif edad >= 11 and edad <= 13:
        print(f"{nombre} es puber.")
    elif edad >= 14 and edad <= 18:
        print(f"{nombre} es adolescente.")
    elif edad >= 19 and edad <= 59:
        print(f"{nombre} es adulto.")
    elif edad >= 60 and edad <= 69:
        print(f"{nombre} es adulto mayor.")
    elif edad >= 69:
        print(f"{nombre} es anciano.")
    else:
        print("Edad no válida.")

# ejercicio_4()

# Ejercicio 5 - Enunciado 2
class Enunciado_2:
    def __init__(self):
        codigo_producto = input("Ingrese el código del producto (P: Papa, C: Cebolla, L: Limón, A: Ají, M: Maíz): ").upper()
        cantidad = int(input("Ingrese la cantidad del producto: "))

        print(f"El precio total a pagar por el producto es: {calcular_precio_total(codigo_producto, cantidad)} soles")

def calcular_precio_total(codigo_producto, cantidad):
    if codigo_producto == 'P':
        precio_unitario = 20.5
    elif codigo_producto == 'C':
        precio_unitario = 19.4
    elif codigo_producto == 'L':
        precio_unitario = 32.3
    elif codigo_producto == 'A':
        precio_unitario = 16.5
    elif codigo_producto == 'M':
        precio_unitario = 19.8
    else:
        print("Código de producto no válido.")
        return 0
    
    return round(precio_unitario * cantidad, 2)

# Enunciado_2()

# Ejercicio 2
# Que reciba un numero y muestre un mensaje indicando si es par o no.
def es_par():
    numero = int(input("Ingrese un número: "))
    
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} no es un número par.")

# es_par()

# Enunciado 3
def calculo_precio_aplicaciones():
    tipo_producto = input("Ingrese el tipo de producto (O: Oficina, J: Juegos, U: Utilitarios): ").upper()
    tipo_celular = input("Ingrese el tipo de celular (A: Android, I: iPhone): ").upper()
    cantidad = int(input("Ingrese la cantidad de aplicaciones: "))

    precio_unitario = calcular_precio_unitario(tipo_producto, tipo_celular)
    print(f"El precio total a pagar por las aplicaciones es: {round(precio_unitario * cantidad, 2)} soles")
    
def calcular_precio_unitario(tipo_producto, tipo_celular):
    if tipo_producto == 'O' and tipo_celular == 'I':
        return 50.60
    elif tipo_producto == 'O' and tipo_celular == 'A':
        return 20.30
    elif tipo_producto == 'J' and tipo_celular == 'I':
        return 90.80
    elif tipo_producto == 'J' and tipo_celular == 'A':
        return 40.50
    elif tipo_producto == 'U' and tipo_celular == 'I':
        return 60.50
    elif tipo_producto == 'U' and tipo_celular == 'A':
        return 30.60
    else:
        print("Tipo de producto no válido.")
        return 0

calculo_precio_aplicaciones()

    

