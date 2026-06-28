# El supermercado UNO está premiando a sus clientes que compran por un monto mayor a 800 soles, el premio 
# consiste en un juego, donde el cliente, extrae de una urna un papel que tiene un numero de varias cifras 
# (el número de cifras es variado), como máximo tiene 9 dígitos. 
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

def supermercadoUNO():
    # Solicitar al usuario el monto de la compra
    monto_compra = float(input("Ingrese el monto de la compra (mayor a 800 soles): "))
    
    # Verificar que el monto sea mayor a 800
    if monto_compra <= 800:
        print("El monto de la compra debe ser mayor a 800 soles.")
        return
    
    # Solicitar al usuario el número extraído del papel
    # numero = input("Ingrese el número extraído del papel (máximo 9 dígitos): ")

    # Generar un numero de hasta 9 dígitos de manera aleatoria
    import random
    numero = str(random.randint(100000000, 999999999))
    
    # Verificar que el número tenga como máximo 9 dígitos
    if len(numero) > 9 or not numero.isdigit():
        print("El número debe tener como máximo 9 dígitos y ser un número válido.")
        return
    
    # Contar la cantidad de dígitos '1' en el número
    cantidad_unos = numero.count('1')
    
    # Calcular el descuento basado en la cantidad de unos
    descuento_por_unos = cantidad_unos * (monto_compra * 0.01)
    
    # Calcular descuento adicional si la cantidad de unos es múltiplo de 2
    descuento_adicional = 50 if cantidad_unos > 0 and cantidad_unos % 2 == 0 else 0
    
    # Calcular el descuento total
    descuento_total = descuento_por_unos + descuento_adicional
    
    # Calcular el importe a pagar
    importe_a_pagar = monto_compra - descuento_total
    
    # Mostrar los resultados
    print(f"Número extraído del papel: {numero}")
    print(f"Cantidad de dígitos '1': {cantidad_unos}")
    print(f"Descuento por unos: {descuento_por_unos:.2f} soles")
    print(f"Descuento adicional: {descuento_adicional:.2f} soles")
    print(f"Descuento total: {descuento_total:.2f} soles")
    print(f"Importe a pagar: {importe_a_pagar:.2f} soles")

# Llamar a la función para ejecutar el programa
# supermercadoUNO()

# ----------------------------------------------------
# RETO 1 - Análisis de Ventas con ciclos FOR/WHILE
# ----------------------------------------------------

def reto1():
    num_vendedores = int(input("Ingrese la cantidad de vendedores: "))

    mayor_venta_total = -1
    vendedor_mayor_venta = ""
    mayor_dias_superados = -1
    vendedor_mayor_dias = ""

    for v in range(num_vendedores):
        print("\n--- Vendedor", v + 1, "---")
        nombre = input("Ingrese el nombre del vendedor: ")
        dias = int(input("¿Cuántos días trabajó este mes?: "))

        total_vendido = 0
        dias_superados = 0

        for d in range(dias):
            venta = int(input("Ventas del día " + str(d + 1) + ": "))
            total_vendido += venta

            if venta > 10:
                dias_superados += 1

        promedio = total_vendido / dias

        print("\nResultados del vendedor:", nombre)
        print("Total vendido:", total_vendido)
        print("Promedio diario:", promedio)
        print("Días con más de 10 ventas:", dias_superados)

        # Actualizar máximos
        if total_vendido > mayor_venta_total:
            mayor_venta_total = total_vendido
            vendedor_mayor_venta = nombre

        if dias_superados > mayor_dias_superados:
            mayor_dias_superados = dias_superados
            vendedor_mayor_dias = nombre

    print("\n==============================")
    print("Vendedor con mayor venta total:", vendedor_mayor_venta)
    print("Monto:", mayor_venta_total)
    print("Vendedor con más días superando 10 ventas:", vendedor_mayor_dias)
    print("Días:", mayor_dias_superados)

reto1()


