herramientas = []


def agregar_producto():
    print("----- Agregar Herramienta -----")
    nombre = input("Nombre: ").lower()
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    herramientas.append(producto)
    print("✅ Producto guardado correctamente")


def ver_inventario():
    if not herramientas:
        print("⚠ No existen herramientas registradas")
        return

    print("----- Inventario -----")
    for item in herramientas:
        print(f"Nombre: {item['nombre']} | Precio: ${item['precio']} | Stock: {item['stock']}")


def editar_producto():
    buscar = input("¿Qué herramienta deseas editar?: ").lower()
    encontrado = False

    for item in herramientas:
        if item["nombre"] == buscar:
            encontrado = True

            print("1. Cambiar Precio")
            print("2. Cambiar Stock")
            opcion = input("Opción: ")

            if opcion == "1":
                item["precio"] = float(input("Nuevo precio: "))
                print("✅ Precio actualizado")

            elif opcion == "2":
                item["stock"] = int(input("Nuevo stock: "))
                print("✅ Stock actualizado")

            break  # 🔥 sale del ciclo cuando ya encontró el producto

    if not encontrado:
        print("❌ Herramienta no encontrada")


def guardar_inventario():
    with open("Inventario.txt", "w") as archivo:
        for item in herramientas:
            archivo.write(
                f"Nombre: {item['nombre']} | Precio: ${item['precio']} | Stock: {item['stock']}\n"
            )
    print("💾 Inventario guardado con éxito")


def eliminar_inventario():
    herramientas.clear()
    print("🗑 Inventario eliminado correctamente")


def menu():
    while True:
        print("\n======= FERRETERIA EL AMIGO GUZ =======")
        print("1. Agregar Herramienta")
        print("2. Ver Inventario")
        print("3. Editar Herramienta")
        print("4. Guardar Inventario")
        print("5. Eliminar Inventario")
        print("6. Salir")

        opc = input("Elija una opción: ")

        if opc == "1":
            agregar_producto()

        elif opc == "2":
            ver_inventario()

        elif opc == "3":
            editar_producto()

        elif opc == "4":
            guardar_inventario()

        elif opc == "5":
            eliminar_inventario()

        elif opc == "6":
            print("👋 Programa finalizado")
            break

        else:
            print("⚠ Opción inválida")


menu()