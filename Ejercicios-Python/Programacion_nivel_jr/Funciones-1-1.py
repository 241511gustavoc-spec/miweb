frutas=[]

def agregar():
    print("------------------Agregar Manzanas----------------")
    tipo=input("Ingrese la fruta: ").lower()
    cant=float(input("Kilos agregados: "))
    pre=float(input("Precio por kilo: "))

    producto={
        "tipo":tipo,
        "cantidad":cant,
        "precio":pre

    }

    frutas.append(producto)
    

def ver():
    if not frutas:
        print("NO EXITEN FRUTAS AGREGADAS")
        return
    
    print("###################INVENTARIO############")
    for item in frutas:
        print(f"Fruta: {item['tipo']} | KG en stock: {item['cantidad']} | Precio: ${item['precio']}")
    print("----------------------------------------")

def guardar():
    with open("Inventario.txt","w")as archivo:
        for item in frutas:
            archivo.write(f"Nombre: {item["tipo"]} | kilogramos: {item["cantidad"]} | Precio: ${item["precio"]}\n")
    print("INVENTARIO GUARDADO DE FORMA EXITOSA")

def editar():
    buscar=input("¿Que fruta desea buscar?: ").lower()
    encontrado=False

    for item in frutas:
        if item["tipo"]==buscar:
            encontrado=True

            print("1. Cambiar Tipo de fruta")
            print("2. Cambiar Cantidad")
            print("3. Cambiar precio")

            preg=input("Opción: ")

            if preg=="1":
                item["tipo"]=input("Nuevo tipo de fruta: ")
                print("TIPO DE FRUTA ACTUALIZADA")

            elif preg=="2":
                item["cantidad"]=int(input("Nueva cantidad: "))
                print("CANTIDAD ACTUALIZADA")

            elif preg=="3":
                item["precio"]=float(input("Nuevo Precio: "))
                print("PRECIO ACTUALIZADO")

    if not encontrado:
        print("No se encontro el producto")

def eliminar():
    frutas.clear()
    print("INVENTARIO ELIMINADO CON EXITO")


def menu():
    while True:
        print("\n<<<<<<<<<<<<<<<<<<<<Fruteria La Coliflor>>>>>>>>>>>>>>>>>>>>>")
        print("MENU\n")
        print("1.Agregar")
        print("2.Ver")
        print("3.Editar")
        print("4.Guardar")
        print("5.Eliminar")
        print("6.Salir")

        opc=input("Opción: ")

        if opc=="1":
            agregar()
        elif opc=="2":
            ver()
        elif opc=="3":
            editar()
        elif opc=="4":
            guardar()
        elif opc=="5":
            eliminar()
        elif opc=="6":
            print("Programa Finalizado")
            break
        else:
            print("ELIJA UNA OPCIÓN VALIDA")
menu()






    