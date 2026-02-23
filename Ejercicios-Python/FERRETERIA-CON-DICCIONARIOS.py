herramienta=[]

while True:
    print("=======FERRETERIA EL AMIGO GUZ=========")
    print("1. Agregar Herramienta")
    print("2. Ver Inventario")
    print("3. Editar Herramienta")
    print("4. Guardar Inventario")
    print("5. Eliminar Inventario")
    print("6. Salir")

    opc=input("Elija una opción: ")

    if opc=="6":
        pregunta=input("¿Estas seguro de cerrar el programa? S/N: ").lower()
        if pregunta=="s":
            print("PROGRAMA FINALIZADO")
            break

        elif pregunta=="n":
            continue
        else:
            print("OPCIÓN INVALIDA")
    
    elif opc=="1":
        print("--------------Agrega Una Herramienta--------------")

        nombre=input("Nombre: ").lower()
        precio=float(input("Precio: "))
        stock=int(input("Stock: "))

        producto={
            "nombre":nombre,
            "precio":precio,
            "stock": stock
        }

        herramienta.append(producto)
        print("Producto Guaradado de forma Exitosa")

    elif opc=="2":
        if len(herramienta)==0:
            print("No existen Herramientas Registradas")
        else:
            for item in herramienta:
                print(f" Nombre{item['nombre']} | Precio: ${item['precio']} | Disponible: {item['stock']}")

    elif opc=="4":
        pregunta=input("¿Desea guardar el inventario? S/N: ").lower()
        if pregunta in ["si","s"]:
            with open("Inventario.txt","w")as archivo:
                for item in herramienta:
                    archivo.write(f" Nombre: {item['nombre']} | Precio: ${item['precio']} | Disponible: {item['stock']}\n")
            print("ARCHIVO GUARDADO CON EXITO")

    elif opc=="5":
        pregunta=input("¿Estas seguro de eliminar el resgitro? S/N: ").lower()
        if pregunta in ["s", "si"]:
            herramienta.clear()
            print("DATOS BORRADOS DE MANERA EXITOSA")
        else:
            continue

    elif opc=="3":
        buscar=input("¿Que herramienta desea Buscar?: ").lower()
        encontrado=False
        
        for item in herramienta:
            if item["nombre"].lower() == buscar:
                encontrado=True

                print("1. Cambiar Precio")
                print("2. Cambiar stock")

                opcion=input("Opción: ")

                if opcion=="1":
                    item["precio"]=float(input("Nuevo Precio: "))
                    print("Precio Actualizado")
                
                elif opcion=="2":
                    item["stock"]=int(input("Nuevo Stock: "))
                    print("Stock Actualizado")

        if not encontrado:
            print("Herramienta NO encontrada")

                   
                   
                   






