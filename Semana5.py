# Una empresa vendedora de fotocopiadoras necesita calcular cual ha sido el volumen de ventas de cada uno de sus 
# agentes comerciales durante el presente mes y en base a eso determinar distintos indicadores, 
# así como montos a pagar en comisión de ventas.
	
# Se le solicita:
# 1. Obtener el total de unidades vendidas durante el presente mes. Para eso se tiene como dato de entrada un 
# arreglo con la cantidad de unidades vendidas por cada agente comercial.
# 2. Si se sabe que la cuota de venta de cada vendedor es 5 unidades, determinar cuál es el porcentaje de vendedores 
# que superaron la cuota de venta. Para eso se tiene como dato de entrada un arreglo con la cantidad de unidades 
# vendidas por cada agente comercial.
# 3. Se desea saber quién(es) fueron los agentes de ventas que superaron la cuota de venta.
# 4. Si se sabe que por cada unidad vendida se tiene que pagar una comisión de ventas de 300 soles, determinar 
# cuánto es lo que se tiene que pagar como comisión este mes.

def Enunciado_1():
    cantidad_agentes = int(input("Ingrese la cantidad de agentes comerciales: "))
    cantidad_vendidas = [0]*cantidad_agentes
    # cantidad_vendidas = []
    # cantidad_vendida = [int(input(f"Ingrese la cantidad de unidades vendidas por el agente comercial {i+1}: ")) for i in range(cantidad_agentes)]
    for i in range(0, cantidad_agentes, 1):
        cantidad_vendidas[i] = int(input(f"Ingrese la cantidad de unidades vendidas por el agente comercial {i+1}: "))
    # total_unidades_vendidas = sum(cantidad_vendidas)
    total_unidades_vendidas = 0
    for i in range(0, cantidad_agentes, 1):
        total_unidades_vendidas += cantidad_vendidas[i]
    # porcentaje_superaron_cuota = (len([cantidad for cantidad in cantidad_vendidas if cantidad > 5]) / len(cantidad_vendidas)) * 100
    cantidad_superaron_cuota = 0
    for i in range(0, len(cantidad_vendidas), 1):
        if cantidad_vendidas[i] > 5:
            cantidad_superaron_cuota += 1
    porcentaje_agentes_superaron_cuota = round((cantidad_superaron_cuota / cantidad_agentes) * 100, 2) 

    # agentes_superaron_cuota = [i+1 for i, cantidad in enumerate(cantidad_vendida) if cantidad > 5]
    print("Pregunta 1:")
    print(f"El total de unidades vendidas durante el presente mes es: {total_unidades_vendidas} unidades")
    print("Pregunta 2:")
    print(f"El porcentaje de vendedores que superaron la cuota de venta es: {porcentaje_agentes_superaron_cuota}%")
    print("Pregunta 3:")
    # print(f"Los agentes de ventas que superaron la cuota de venta son: {agentes_superaron_cuota}")
    for i in range(0, cantidad_agentes, 1):
        if cantidad_vendidas[i] > 5:
            print(f"El agente comercial {i+1} superó la cuota de venta con {cantidad_vendidas[i]} unidades vendidas.")
    print("Pregunta 4:")
    comision_total = total_unidades_vendidas * 300
    print(f"El monto a pagar como comisión este mes es: {comision_total} soles")

Enunciado_1()