abarrotes=[]

def agregar():
    ab=input("Agrega el articulo: ").lower()
    precio=float(input("Precio: "))
    stock=int(input("Cantidad: "))

    producto={
        "abarrote":ab,
        "precio":precio,
        "stock":stock
    }

    abarrotes.append(producto)

def ver():
    if not abarrotes:
        print("No se encontraron articulos para mostrar")

    else:
        print("----------ARTICULOS-------------")
        for item in abarrotes:
            print(f"Articulo: {item['abarrote']} | Precio: ${item['precio']} | Stock: {item['stock']}")

def guardar():
    if not abarrotes:
        print("XXXXXXXXX No se encuentran articulos para guardar XXXXXXXXX")
    else:
        with open("Articulos.txt","w")as archivo:
            for item in abarrotes:
                archivo.write(f"Articulo: {item['abarrote']} | Precio: ${item['precio']} | Stock: {item['stock']}\n")
        print("Archivo Guardado con exito")

def eliminar():
    abarrotes.clear()
    print("Articulos Eliminados correctamente")

def menu():

    while True:
        print("----------ABARROTES LA DUFFY------")
        print("1. Agregar Articulo")
        print("2. Ver Articulos")
        print("3. Guardar")
        print("4. Eliminar")
        print("5. Salir\n")

        op=input("Opción: ")

        if op=="1":
            agregar()
        elif op=="2":
            ver()
        elif op=="3":
            guardar()
        elif op=="4":
            eliminar()
        elif op=="5":
            print("Programa Finalizado")
            break
        else:
            print("Elija Una opción Valida")
menu()



