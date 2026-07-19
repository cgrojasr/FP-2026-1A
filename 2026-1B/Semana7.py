# Ingresa una lista de montos en soles (PEN). El programa debe mostrar cada monto convertido a dólares 
# (1 USD = 3.75 PEN), euros (1 EUR = 4.10 PEN) y pesos chilenos (1 CLP = 0.0042 PEN). 
# Además, indica cuántos montos superan los 1000 soles.

def convertir_montos(montos):
    tasa_dolar = 3.75
    tasa_euro = 4.10
    tasa_peso_chileno = 0.0042

    montos_convertidos = []
    montos_superiores_1000 = 0

    for monto in montos:
        monto_dolar = monto / tasa_dolar
        monto_euro = monto / tasa_euro
        monto_peso_chileno = monto / tasa_peso_chileno

        montos_convertidos.append((monto, monto_dolar, monto_euro, monto_peso_chileno))

        if monto > 1000:
            montos_superiores_1000 += 1

    return montos_convertidos, montos_superiores_1000

def main():
    montos = []
    cantidad_montos = int(input("Ingrese la cantidad de montos en soles: "))

    for i in range(cantidad_montos):
        monto = float(input(f"Ingrese el monto {i + 1} en soles: "))
        montos.append(monto)

    montos_convertidos, montos_superiores_1000 = convertir_montos(montos)

    print("\nMontos convertidos:")
    for monto, dolar, euro, peso_chileno in montos_convertidos:
        print(f"{monto:.2f} PEN -> {dolar:.2f} USD, {euro:.2f} EUR, {peso_chileno:.2f} CLP")

    print(f"\nCantidad de montos que superan los 1000 soles: {montos_superiores_1000}")

main()
