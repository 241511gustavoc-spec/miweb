inventario = [] #Lista Principal

#---------PARA AGREGAR UNA HERRAMIENTA------------
nombre = input("Herramienta: ")
precio = float(input("Precio: "))
stock = int(input("Stock: "))

producto = {
    "nombre": nombre,
    "precio": precio,
    "stock": stock
}
inventario.append(producto)


  #-------MOSTRAR INVENTARIO---------------------
for item in inventario:
    print(f"Herramienta: {item['nombre']} | Precio: ${item['precio']} | Stock: {item['stock']}")          



#---------GUARDAR ARCHIVO----------------------
with open("inventario.txt", "w") as archivo:
    for item in inventario:
        archivo.write(f"{item['nombre']} - ${item['precio']} - Stock: {item['stock']}\n")




#----------ACTUALIZAR--------------------------
#elif opc == "4":  # Actualizar producto
    buscar = input("¿Qué herramienta quieres actualizar?: ").lower()
    encontrado = False

    for item in inventario:
        if item["nombre"].lower() == buscar:
            encontrado = True

            print("1. Cambiar precio")
            print("2. Cambiar stock")
            opcion = input("Opción: ")

            if opcion == "1":
                item["precio"] = float(input("Nuevo precio: "))
                print("Precio actualizado")

            elif opcion == "2":
                item["stock"] = int(input("Nuevo stock: "))
                print("Stock actualizado")

    if not encontrado:
        print("Herramienta no encontrada")
