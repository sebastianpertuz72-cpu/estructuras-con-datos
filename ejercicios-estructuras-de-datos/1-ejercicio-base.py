matriz_ventas = []
precios = [1500, 5000, 6500, 2500, 22500]
ingresos_productos = []
for i in range(5):
    fila_temporal = []
    for j in range (7):
        fila_temporal.append(int(input(f"Digite ventas del producto {i+1}, día {j+1}: ")))
    matriz_ventas.append(fila_temporal)
for f in range(5):
    resultado_dinero = sum(matriz_ventas[f]) * precios[f]
    ingresos_productos.append(resultado_dinero)
print(ingresos_productos)
mayor_dinero = max(ingresos_productos)
posicion_mayor_dinero = ingresos_productos.index(mayor_dinero)
num_producto = posicion_mayor_dinero + 1

print(f"El producto que genera mas ingresos es el producto {num_producto} con total de {mayor_dinero}")