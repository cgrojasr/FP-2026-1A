def Enunciado_S6():
    fin_codigo = True
    codigos = []
    while fin_codigo:
        codigo_producto = input("Ingrese el código del producto (PPCCCCVV): ")
        if len(codigo_producto) != 8:
            print("El código debe tener 8 caracteres. Intente nuevamente.")
        else:
            codigos.append(codigo_producto)
            continua_ingresando = input("¿Desea ingresar otro código? (s/n): ")
            if continua_ingresando.lower() != 's':
                fin_codigo = False
    
    cantidad_producto_x_pais(codigos)
    print("---------------------------------------------------------")
    ultimo_correlativo(codigos)
    print("---------------------------------------------------------")
    monto_almacenaje_por_pais(codigos)


def cantidad_producto_x_pais(codigos):
    paises = []
    cantidades = []
    indice_pais = -1
    for i in range(len(codigos)):
        pais = codigos[i][0:2]
        # if pais in paises:
        #     paises[pais] += 1
        if len(paises) == 0:
            paises.append(pais)
            cantidades.append(1)
        else:
            for j in range(len(paises)):
                if paises[j] == pais:
                    indice_pais = j
                    break
            if indice_pais == -1:
                paises.append(pais)
                cantidades.append(1)
            else:
                cantidades[indice_pais] += 1
                indice_pais = -1
    print("Cantidad de productos vendidos por país:")
    for i in range(len(paises)):
        print(f"{paises[i]}: {cantidades[i]} productos")

def ultimo_correlativo(codigos):
    correlativos = []
    paises = []
    indice_pais = -1
    for i in range(len(codigos)):
        codigo_pais = codigos[i][0:2]
        correlativo = codigos[i][2:6]
        for j in range(len(paises)):
            if paises[j] == codigo_pais:
                indice_pais = j
                break
        if indice_pais == -1:
            paises.append(codigo_pais)
            correlativos.append(int(correlativo))
        else:
            if correlativos[indice_pais] < int(correlativo):
                correlativos[indice_pais] = int(correlativo)
                indice_pais = -1
    
    for i in range(len(paises)):
        print(f"El último correlativo registrado para el país {paises[i]} es: {correlativos[i]}")

def monto_almacenaje_por_pais(codigos):
    paises = []
    montos = []
    indice_pais = -1
    for i in range(len(codigos)):
        pais = codigos[i][0:2]
        # if pais in paises:
        #     paises[pais] += 1
        for j in range(len(paises)):
            if paises[j] == pais:
                indice_pais = j
                break

        if indice_pais == -1:
            paises.append(pais)
            montos.append(int(codigos[i][6:8]))
        else:
            montos[indice_pais] += int(codigos[i][6:8])
            indice_pais = -1
            
    print("Monto de almacenaje por país:")
    for i in range(len(paises)):
        print(f"{paises[i]}: {montos[i]} soles de almacenaje")

Enunciado_S6()
