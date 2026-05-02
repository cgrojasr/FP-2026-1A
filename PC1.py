def Caso1_1():
    televisor = float(input("Ingrese el precio del televisor en soles: "))
    equipo_sonido = float(input("Ingrese el precio del equipo de sonido en soles: "))
    soporte_pared = float(input("Ingrese el precio del soporte de pared en soles: "))
    total = televisor + equipo_sonido + soporte_pared
    print(f"a) El total a pagar por los tres productos es: {total} soles")
    print(f"b) El precio con descuento del 10% es: {round(total * 0.9, 2)} soles")

# Caso1_1()

def Caso1_2():
    volumen_bobeda = float(input("Ingrese el volumen de la bodega en metros cúbicos: "))
    largo_caja = float(input("Ingrese el largo de la caja en metros: "))
    ancho_caja = float(input("Ingrese el ancho de la caja en metros: "))
    alto_caja = float(input("Ingrese el alto de la caja en metros: "))
    volumen_caja = largo_caja * ancho_caja * alto_caja
    volumen_maximo = volumen_bobeda * 0.75
    cantidad_cajas = int(volumen_maximo // volumen_caja)
    print(f"El número máximo de cajas que se pueden almacenar en la bodega es: {cantidad_cajas} cajas")
    print(f"El volumen total ocupado por las cajas es: {round(cantidad_cajas * volumen_caja, 2)} metros cúbicos")
    print(f"El volumen libre máximo de la bodega es: {round(volumen_maximo, 2)} metros cúbicos")

Caso1_2()