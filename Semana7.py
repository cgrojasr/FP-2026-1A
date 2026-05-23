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

Ejercicio1()


