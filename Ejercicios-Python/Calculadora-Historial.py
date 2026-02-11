historial=[]

while True:
    print("----->CALCULADORA AVANZADA<-----")
    print("1.SUMAR")
    print("2.RESTAR")
    print("3.MULTIPLICAR")
    print("4.DIVIDIR")
    print("5.VER HISTORIAL")
    print("6.SALIR")

    opc=input("Elija una opción: ")

    if opc=="6":
        duda=input("¿Esta seguro de cerrar el programa? S/N ").lower()
        if duda=="s":
            print("Programa Finalizado 🫢")
            break

        elif duda=="n":
            continue
    
    if opc=="5":
        print("*****HISTORIAL*****")
        if len(historial)==0:
            print("No hay operaciones todavía")
        else:
            for operaciones in historial:
                print(operaciones)
        continue

    if opc in ["1","2","3","4"]:
        try:
            num1=float(input("Escriba el primer número: "))
            num2=float(input("Escriba el segundo número: "))
        except:
            print("⚠️ Escriba un número valido")
            continue

        if opc=="1":
            resultado=num1+num2
            texto=f"{num1}+{num2}={resultado}"

        elif opc=="2":
            resultado=num1-num2
            texto=f"{num1}-{num2}={resultado}"

        elif opc=="3":
            resultado=num1*num2
            texto=f"{num1}*{num2}={resultado}"

        elif opc=="4":
            try:
                resultado=num1/num2
                texto=f"{num1}/{num2}={resultado}"
            except ZeroDivisionError:
                print("❌NO SE PUEDE DIVIDIR ENTRE CEROS❌")
                continue

        print("Resultado: ",resultado)
        historial.append(texto)

    else:
        print("Opción No válida")

        








