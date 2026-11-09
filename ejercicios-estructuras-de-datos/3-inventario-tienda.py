inventario = []


def mostrar_menu():
    print("\n========== MENÚ ==========",
    "\n1. Agregar producto",
    "\n2. Agregar lote de productos",
    "\n3. Eliminar producto del inventario",
    "\n4. Eliminar el producto más reciente",
    "\n5. Ordenar productos alfabéticamente",
    "\n6. Mostrar número total de productos",
    "\n7. Salir",
    "==========================")


def mostrar_inventario():
    if inventario:
        print("Inventario actual:", ", ".join(inventario))
    else:
        print("El inventario está vacío.")


def buscar_producto(nombre):
    """Busca un producto ignorando mayúsculas/minúsculas.
    Devuelve el nombre tal como está guardado o None."""
    for producto in inventario:
        if producto.lower() == nombre.lower():
            return producto
    return None


def agregar_producto():
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
    elif buscar_producto(nombre):
        print(f"'{nombre}' ya existe en el inventario.")
    else:
        inventario.append(nombre)
        print(f"Producto '{nombre}' agregado.")


def agregar_lote():
    texto = input("Productos separados por comas (ej: leche, pan, arroz): ")
    lote = []
    for nombre in (p.strip() for p in texto.split(",")):
        # Se omiten vacíos y duplicados (en el inventario o en el mismo lote)
        if nombre and not buscar_producto(nombre) and nombre.lower() not in [l.lower() for l in lote]:
            lote.append(nombre)
    if lote:
        inventario.extend(lote)
        print(f"Se agregaron {len(lote)} producto(s): {', '.join(lote)}")
    else:
        print("No se agregó ningún producto nuevo.")


def eliminar_producto():
    if not inventario:
        print("El inventario está vacío.")
        return
    mostrar_inventario()
    nombre = input("Producto a eliminar: ").strip()
    encontrado = buscar_producto(nombre)
    if encontrado:
        inventario.remove(encontrado)
        print(f"Producto '{encontrado}' eliminado.")
    else:
        print(f"'{nombre}' no se encontró en el inventario.")


def eliminar_mas_reciente():
    if inventario:
        eliminado = inventario.pop()
        print(f"Se eliminó el producto más reciente: '{eliminado}'.")
    else:
        print("El inventario está vacío.")


def ordenar_productos():
    if inventario:
        inventario.sort(key=str.lower)
        print("Inventario ordenado alfabéticamente.")
        mostrar_inventario()
    else:
        print("El inventario está vacío.")


def mostrar_total():
    print(f"Total de productos: {len(inventario)}")


def main():
    acciones = {
        "1": agregar_producto,
        "2": agregar_lote,
        "3": eliminar_producto,
        "4": eliminar_mas_reciente,
        "5": ordenar_productos,
        "6": mostrar_total,
    }
    while True:
        mostrar_menu()
        opcion = input("Elija una opción (1-7): ").strip()
        if opcion == "7":
            print("¡Hasta pronto!")
            break
        accion = acciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opción no válida. Intente de nuevo.")



if __name__ == "__main__":
    main()