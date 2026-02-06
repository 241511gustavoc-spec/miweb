while True: 
    print("========CALCULADORA PRO MAX==========")
    print("SELECCIONE UNA OPCIÓN")
    print("(1)SUMA")
    print("(2)RESTA")
    print("(3)MULTIPLICACIÓN")
    print("(4)DIVISIÓN")
    print("(5)SALIR")

    opc=input("Opción: ")

    if opc=="5":
        print("Programa Finalizado ✌️")
        break
    
    if opc not in ["1","2","3","4","5"]:
        print("Seleccione una opción valida")
        continue

    try:
        num1=float(input("Teclea el primer número: "))
        num2=float(input("Teclea el segundo número: "))
    except:
        print("Teclea un número válido")
        continue

    if opc=="1":
        print("El resultado es ",num1+num2)

    elif opc=="2":
        print("El resultado es ",num1-num2)

    elif opc=="3":
        print("El resultdo es ", num1*num2)

    elif opc=="4":
        if num2==0:
            print("No se puede dividir entre 0")
            continue
        print("El resultado es ", num1/num2)
    
