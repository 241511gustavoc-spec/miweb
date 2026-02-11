animales=[]

while True:
    print("======MENÚ======")
    print("1. Ver lista 🧾")
    print("2. Agregar animales ➕")
    print("3. Borrar Lista 🗑️")
    print("4. Salir 🔚")

    opc=input("Elija Una opción: ")

    if opc=="4":
        q=input("⚠️ ¿Estas seguro de finalizar el programa? S/N: ").lower()

        if q in ["s","si"]:
            print("Programa Finalizado")
            break
        else:
            continue
    
    if opc=="1":
        if len(animales)==0:
            print("****************LISTA VACIA**************")

        else:
            print("****************Lista de Animales***************")
            for ani in animales:
                print(ani)
            print("====================================")
    
    elif opc=="2":
        a=input("Agrega un animal: ")
        print("Agregaste", a)

        animales.append(a)
    
    elif opc=="3":
        preg=input("⚠️ ¿Estas seguro de eliminar la lista? S/N: ").lower()
        if preg=="s":
            animales.clear()
            print("Lista Vaciada 🗑️")
    else:
        print("Opción invalida")
        continue

