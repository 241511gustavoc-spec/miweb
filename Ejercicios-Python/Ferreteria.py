personal=[]

while True:
    print("=========AGREGA A UN NUEVO PERSONAL================")
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Guardar")
    print("4. Salir")
    print("5. Ver lista")

    opc=input("Seleccione una opción: ")

    if opc=="4":
        pregunta=input("¿Estas seguro de cerrar el programa? S/N: ").lower()

        if pregunta in ["s", "si"]:
            print(" BYE  BYE")
            break
        else:
            continue

    if opc=="1":
        a=input("TECLEA EL NOMBRE DEL NUEVO PERSONAL: ")
        personal.append(a)
        print("Guardasta con exito a ",a)

    elif opc=="2":
        pregunta= input("¿Estas seguro de querer eliminar esta información? S/N: ").lower()
        if pregunta in ["s", "si"]:
            personal.clear()
            print("DATOS ELIMINADOS DE MANERA EXITOSA")
        else:
            continue

    elif opc=="3":
        if len(personal)==0:
            print("NO EXISTEN DATOS PARA SER GUARDADOS")
        else:
            with open("PERSONAL.txt","w") as archivo:
                for gente in personal:
                    archivo.write(gente + "\n")
        print("------------------Información Guardada de forma exitosa------------------------")

    elif opc=="5":
        if len(personal)==0:
            print("NO EXISTE INFORMACIÓN PARA MOSTRAR")

        else:
            print("===LISTA DE PERSONAL===")
            for gente in personal:
                print(gente)
            print("----------------------------------------------")

    else:
        print("Opción Invalida")
        
            



