# Ejercicio: Ventas mensuales
# Una empresa vendedora de fotocopiadoras necesita calcular cual ha sido el volumen de ventas de cada 
# uno de sus agentes comerciales durante el presente mes y en base a eso determinar distintos indicadores, 
# así como montos a pagar en comisión de ventas.
	
# Se le solicita:
# 1. Obtener el total de unidades vendidas durante el presente mes. Para eso se tiene como dato de entrada 
# un arreglo con la cantidad de unidades vendidas por cada agente comercial.
# 2. Si se sabe que la cuota de venta de cada vendedor es 5 unidades, determinar cuál es el porcentaje de 
# vendedores que superaron la cuota de venta. Para eso se tiene como dato de entrada un arreglo con la 
# cantidad de unidades vendidas por cada agente comercial.
# 3. Se desea saber quién(es) fueron los agentes de ventas que superaron la cuota de venta.
# 4. Si se sabe que por cada unidad vendida se tiene que pagar una comisión de ventas de 300 soles, determinar 
# cuánto es lo que se tiene que pagar como comisión este mes.

import random

def ejercicio1():
    cantidad_vendedores = int(input("Ingrese la cantidad de vendedores: "))
    ventas = [0] * cantidad_vendedores
    for i in range(cantidad_vendedores):
        unidades = random.randint(1, 10)  # Generar un número aleatorio entre 1 y 10
        ventas[i] = unidades

    total_unidades = sum(ventas)
    print("1. Total de unidades vendidas:", total_unidades)
    print("2. Porcentaje de vendedores que superaron la cuota:", cantidad_superaron_cuota(ventas), "%")
    print("4. Monto total a pagar en comisión:", total_unidades * 300, "soles")

def cantidad_superaron_cuota(ventas):
    cuota = 5
    indice = 0
    superaron_cuota = sum(1 for venta in ventas if venta > cuota)
    for venta in range(len(ventas)):
        if ventas[venta] > cuota:
            print("3.",indice + 1," Vendedor con", ventas[venta], "unidades vendidas superó la cuota.")
        indice += 1
    porcentaje = (superaron_cuota / len(ventas)) * 100
    return porcentaje

# ejercicio1()


# ---------------------------------------------------------
# RETO 1 - Sistema de Evaluación Académica Completa
# ---------------------------------------------------------

# Una universidad desea analizar el rendimiento de un grupo de estudiantes.
# El programa debe:
# Solicitar al usuario cuántos estudiantes tiene el curso.
# Crear un arreglo con las notas de cada estudiante (entre 0 y 20).

# Calcular:
# La nota promedio del curso.
# La nota máxima y el índice del estudiante que la obtuvo.
# La nota mínima y el índice del estudiante que la obtuvo.
# Crear un segundo arreglo con las notas aprobadas (≥ 11).

# Determinar:
# El porcentaje de aprobados.
# El porcentaje de desaprobados.

# Mostrar:
# Lista completa de notas
# Lista de aprobados
# Estadísticas finales

def reto1():
    num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

    notas = [0] * num_estudiantes

    # Registro de notas
    for i in range(num_estudiantes):
        # nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
        nota = random.uniform(0, 20)  # Generar una nota aleatoria entre 0 y 20
        nota = round(nota, 2)  # Redondear a 2 decimales
        notas[i] = nota

    # Cálculo del promedio
    suma_notas = 0
    for nota in notas:
        suma_notas += nota

    promedio = suma_notas / len(notas)

    # Nota máxima y mínima
    nota_max = notas[0]
    indice_max = 0

    nota_min = notas[0]
    indice_min = 0

    for i in range(len(notas)):
        if notas[i] > nota_max:
            nota_max = notas[i]
            indice_max = i
        if notas[i] < nota_min:
            nota_min = notas[i]
            indice_min = i

    # Arreglo de aprobados
    aprobados = [0] * len(notas)
    count = 0
    for nota in notas:
        if nota >= 11:
            aprobados[count] = nota
            count += 1
    aprobados = aprobados[:count]  # Recortar el arreglo para eliminar ceros

    porcentaje_aprobados = (len(aprobados) / len(notas)) * 100
    porcentaje_desaprobados = 100 - porcentaje_aprobados

    # Resultados
    print("\n--- RESULTADOS ---")
    print("Notas registradas:", notas)
    print("Promedio del curso:", promedio)
    print("Nota máxima:", nota_max, " (Estudiante índice:", indice_max, ")")
    print("Nota mínima:", nota_min, " (Estudiante índice:", indice_min, ")")
    print("Aprobados:", aprobados)
    print("Porcentaje de aprobados:", porcentaje_aprobados, "%")
    print("Porcentaje de desaprobados:", porcentaje_desaprobados, "%")

reto1()