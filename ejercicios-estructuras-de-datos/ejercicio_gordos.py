def listapeso(a):
    equipo1 = 0
    equipo2 = 0

    for i in range(len(a)):
        if i % 2 == 0:
            equipo1 = equipo1 + a[i]
        else:
            equipo2 = equipo2 + a[i]

    return [equipo1, equipo2]


pesos = []

while True:
    peso = int(input("ingrese el peso de las personas y cuando termine ingrese '999': "))
    if peso == 999:
        break
    pesos.append(peso)  

equipos = listapeso(pesos)

print(equipos)