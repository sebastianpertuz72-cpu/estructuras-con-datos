def crearMatriz(fils, cols):
    matriz = []
    for f in range(fils):
        lista = []
        for c in range(cols):
            lista.append(1)
        matriz.append(lista)
    return matriz

def matrizOpcion1(fils, cols):
    matriz = []
    aumento = 1
    for f in range(fils):
        lista = []
        for c in range(cols):
            lista.append(aumento)
            aumento += 1
        matriz.append(lista)
    return matriz

def matrizOpcion2(fils, cols):
    matriz = []
    aumento = 1
    disminucion = fils

    for f in range(fils):
        lista = []
        for c in range(cols):
            if f % 2 == 0:
                lista.append(aumento)
                aumento += 1
            else:
                lista.append(disminucion)
                disminucion -= 1
        aumento = 1
        disminucion = fils
        matriz.append(lista)
    return matriz

def matrizOpcion3(fils, cols):
    matriz = []

    for f in range(fils):
        lista = []
        for c in range(cols):
            if f == c:
                lista.append(1)
            else:
                lista.append(0)
        matriz.append(lista)
    return matriz

def matrizOpcion4(fils, cols):
    matriz = []
    disminucion = cols - 1
    aumento = 0
    for f in range(fils):
        lista = []
        for c in range(cols):
            if c == disminucion and f == aumento:
                lista.append(1)
                aumento += 1
                disminucion -= 1
            else:
                lista.append(0)
        matriz.append(lista)
    return matriz

def matrizOpcion5(fils, cols):
    matriz = []
    for f in range(fils):
        lista = []
        for c in range(cols):
            if c > f:
                lista.append(0)
            else:
                lista.append(1)
        matriz.append(lista)
    return matriz

def matrizOpcion6(fils, cols):
    matriz = []
    for f in range(fils):
        lista = []
        for c in range(cols):
            if c < f:
                lista.append(0)
            else:
                lista.append(1)
        matriz.append(lista)
    return matriz

def matrizOpcion7(fils, cols):
    matriz = crearMatriz(fils, cols)
    cont = 1
    f = 0
    for c in range(cols):
        for f in range(fils):
            matriz[f][c] = cont
            cont += 1
    return matriz

def matrizOpcion8(fils, cols):
    matriz = []
    for f in range(fils):
        lista = []
        for c in range(cols):
            if (c < f or c == f) and c % 2 != 0:
                lista.append("B")
            elif (c < f or c == f) and c % 2 == 0:
                lista.append("A")
            else:
                lista.append(" ")
        matriz.append(lista)
    return matriz


def imprimirMatriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            print(matriz[f][c], end= " ")
        print("\t\t")

filas = int(input("Digite la cantidad de filas: "))
columnas = int(input("Digite la cantidad de columnas: "))

if filas != columnas:
    print("La matriz debe ser cuadrada, o sea, filas igual a número de columnas.")
else:
    matriz = matrizOpcion1(filas, columnas)
    print("\n")
    print("MATRIZ OPCION 1".center(24,"="))
    print("\n")
    imprimirMatriz(matriz)

    print("\n")
    print("MATRIZ OPCION 2".center(24,"="))
    print("\n")
    matriz2 = matrizOpcion2(filas, columnas)
    imprimirMatriz(matriz2)

    print("\n")
    print("MATRIZ OPCION 3".center(24,"="))
    print("\n")
    matriz3 = matrizOpcion3(filas, columnas)
    imprimirMatriz(matriz3)

    print("\n")
    print("MATRIZ OPCION 4".center(24,"="))
    print("\n")
    matriz4 = matrizOpcion4(filas, columnas)
    imprimirMatriz(matriz4)

    print("\n")
    print("MATRIZ OPCION 5".center(24,"="))
    print("\n")
    matriz5 = matrizOpcion5(filas, columnas)
    imprimirMatriz(matriz5)

    print("\n")
    print("MATRIZ OPCION 6".center(24,"="))
    print("\n")
    matriz6 = matrizOpcion6(filas, columnas)
    imprimirMatriz(matriz6)

    print("\n")
    print("MATRIZ OPCION 7".center(24,"="))
    print("\n")
    matriz7 = matrizOpcion7(filas, columnas)
    imprimirMatriz(matriz7)

    print("\n")
    print("MATRIZ OPCION 8".center(24,"="))
    print("\n")
    matriz8 = matrizOpcion8(filas, columnas)
    imprimirMatriz(matriz8)