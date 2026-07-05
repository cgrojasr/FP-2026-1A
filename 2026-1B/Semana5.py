# Una reconocida empresa que se dedica al rubro logístico de almacén acaba de implementar un proceso 
# automático de etiquetado de todos los productos que almacenará. Las etiquetas poseen el siguiente 
# formato:

# Posición	Significado
# Posición 1 a la 2	País de procedencia del producto PE: Perú AR: Argentina CH: Chile BR: Brasil
# Posición 3 a la 6	Correlativo de productos ingresado
# Posición 7 a la 8	Costo de almacenamiento diario del producto

# Ejemplo:  
# PE219002
# PE = País de procedencia Perú
# 2190 = existen 2190 productos similares en el almacén
# 02 = 2 soles cuestan almacenar el producto en el almacén

# Se solicita lo siguiente:
# 1. Subprograma que obtenga la cantidad de productos de una determinada nacionalidad.
# 2. Subprograma que obtenga el último correlativo generado para un producto de una determinada nacionalidad.
# 3. Subprograma que obtenga el monto de almacenar la totalidad de productos de una determinada nacionalidad en el almacén.

def cantidad_productos_nacionalidad(etiquetas, nacionalidad):
    cantidad = 0
    for etiqueta in etiquetas:
        if etiqueta[0:2] == nacionalidad:
            cantidad += 1
    return cantidad

def ultimo_correlativo_nacionalidad(etiquetas, nacionalidad):
    ultimo_correlativo = 0
    for etiqueta in etiquetas:
        if etiqueta[0:2] == nacionalidad:
            correlativo = int(etiqueta[2:6])
            if correlativo > ultimo_correlativo:
                ultimo_correlativo = correlativo
    return ultimo_correlativo

def monto_almacenamiento_nacionalidad(etiquetas, nacionalidad):
    monto_total = 0
    for etiqueta in etiquetas:
        if etiqueta[0:2] == nacionalidad:
            costo = int(etiqueta[6:8])
            monto_total += costo
    return monto_total

def main():
    # Listar 50 etiquetas de ejemplo para probar los subprogramas
    etiquetas = [
        "PE219002",
        "AR150003",
        "CH300001",
        "BR100005",
        "PE220004",
        "AR151002",
        "CH301003",
        "BR101001",
        "PE221001",
        "AR152004",
        "CH302002",
        "BR102003",
        "PE222003",
        "AR153001",
        "CH303004",
        "BR103002",
        "PE223002",
        "AR154003",
        "CH304001",
        "BR104004",
        "PE224001",
        "AR155002",
        "CH305003",
        "BR105001",
        "PE225004",
        "AR156001",
        "CH306002",
        "BR106003",
        "PE226003",
        "AR157004",
        "CH307001",
        "BR107002",
        "PE227002",
        "AR158003",
        "CH308004",
        "BR108001",
        "PE228001",
        "AR159002",
        "CH309003",
        "BR109004",
        "PE229004",
        "AR160001",
        "CH310002",
        "BR110003",
        "PE230003",
        "AR161004",
        "CH311001",
        "BR111002",
        "PE231002",
        "AR162003",
        "CH312004",
        "BR112001",
        "PE232001",
        "AR163002",
        "CH313003",
        "BR113004",
        "PE233004",
        "AR164001",
        "CH314002",
        "BR114003",
        "PE234003",
        "AR165004",
        "CH315001",
        "BR115002",
        "PE235002",
        "AR166003",
        "CH316004",
        "BR116001",
        "PE236001",
        "AR167002",
        "CH317003",
        "BR117004",
        "PE237004",
        "AR168001",
        "CH318002",
        "BR118003",
        "PE238003",
        "AR169004",
        "CH319001",
        "BR119002",
        "PE239002",
        "AR170003",
        "CH320004",
        "BR120001",
        "PE240001",
        "AR171002",
        "CH321003",
        "BR121004",
        "PE241004",
        "AR172001",
        "CH322002",
        "BR122003",
        "PE242003",
        "AR173004",
        "CH323001",
        "BR123002",
        "PE243002",
        "AR174003",
    ]

    nacionalidad = input("Ingrese la nacionalidad (PE, AR, CH, BR): ").upper()

    cantidad = cantidad_productos_nacionalidad(etiquetas, nacionalidad)
    ultimo_correlativo = ultimo_correlativo_nacionalidad(etiquetas, nacionalidad)
    monto_total = monto_almacenamiento_nacionalidad(etiquetas, nacionalidad)

    print(f"Cantidad de productos de {nacionalidad}: {cantidad}")
    print(f"Último correlativo de productos de {nacionalidad}: {ultimo_correlativo}")
    print(f"Monto total de almacenamiento de productos de {nacionalidad}: {monto_total} soles")


# main()

# RETO - 1
# Una empresa utiliza códigos de producto con el siguiente formato: LLNNNLLL
# Donde:
# LL = dos letras que indican la categoría
# NNN = tres dígitos que indican el lote
# LLL = tres letras que indican el almacén de destino (por ejemplo, SUR, NTE, CTR)

# Ejemplos válidos:
# EL120SUR
# AL450NTE
# RO999CTR

# El programa debe:
# Validar que el código tenga exactamente 8 caracteres.
# Validar que los primeros 2 sean letras y los siguientes 3 sean números.

# Extraer:
# Categoría → código[0:2]
# Lote → código[2:5]
# Almacén → código[5:8]

# Clasificar la categoría según estas reglas:
# EL → Electrónica
# AL → Alimentos
# RO → Ropa
# Otro → Categoría desconocida

# Mostrar un mensaje final con toda la información extraída.

# ---------------------------------------------------------
# EJERCICIO 1 - Validación y Clasificación de Código
# ---------------------------------------------------------

def reto1():
    codigo = input("Ingrese el código del producto (8 caracteres): ")

    # Validación de longitud
    if len(codigo) != 8:
        print("Código inválido: debe tener exactamente 8 caracteres.")
    else:
        categoria = codigo[0:2]
        lote = codigo[2:5]
        almacen = codigo[5:8]

        # Validación de letras y números
        if not categoria.isalpha() or not lote.isdigit() or not almacen.isalpha():
            print("Código inválido: formato incorrecto.")
        else:
            # Clasificación
            if categoria == "EL":
                tipo = "Electrónica"
            elif categoria == "AL":
                tipo = "Alimentos"
            elif categoria == "RO":
                tipo = "Ropa"
            else:
                tipo = "Categoría desconocida"

            print("\n--- Información del Producto ---")
            print("Categoría:", tipo)
            print("Lote:", lote)
            print("Almacén:", almacen)

# reto1()

#RETOS - 2
# Dado un arreglo de nombres:
# nombres = ["Carlos", "Ana", "Felipe", "María", "Jonathan", "Sol", "Pedro"]
# El programa debe:

# Recorrer el arreglo usando un ciclo.

# Para cada nombre:
# 1. Obtener la primera letra
# 2. Obtener la última letra
# 3. Obtener la subcadena formada por los primeros 3 caracteres (si el nombre tiene menos de 3 
#    caracteres, mostrar el nombre completo)
# 4. Contar cuántos nombres empiezan con vocal.
# 5. Contar cuántos nombres tienen más de 5 caracteres.
# 6. Construir un nuevo arreglo con los nombres que contienen la letra “a” o “A”.
# Mostrar todos los resultados.

# ---------------------------------------------------------
# EJERCICIO 2 - Análisis de nombres en un arreglo
# ---------------------------------------------------------

def reto2():
    nombres = ["Carlos", "Ana", "Felipe", "María", "Jonathan", "Sol", "Pedro"]

    vocales = "AEIOUaeiou"
    contador_vocal = 0
    contador_mayores_5 = 0
    nombres_con_a = []

    for nombre in nombres:
        primera = nombre[0]
        ultima = nombre[-1]

        if len(nombre) >= 3:
            subcadena = nombre[0:3]
        else:
            subcadena = nombre

        print("\nNombre:", nombre)
        print("Primera letra:", primera)
        print("Última letra:", ultima)
        print("Subcadena (primeros 3 caracteres):", subcadena)

        if primera in vocales:
            contador_vocal += 1

        if len(nombre) > 5:
            contador_mayores_5 += 1

        if "a" in nombre.lower():
            nombres_con_a.append(nombre)

    print("\n--- Resultados Finales ---")
    print("Nombres que empiezan con vocal:", contador_vocal)
    print("Nombres con más de 5 caracteres:", contador_mayores_5)
    print("Nombres que contienen la letra 'a':", nombres_con_a)

reto2()