def stringreducido(string: str):
    listap = []
    for i in string:
        if listap and listap[-1] == i:
            listap = listap[:-1]
        else:
            listap.append(i)
    return "".join(listap) if listap else "String vacio"

while True:
    palabra = input("Ingrese su listado de letras pares a eliminar: ").strip()
    print(stringreducido(palabra))
    break