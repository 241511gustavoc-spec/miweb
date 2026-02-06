print("CALCULADORA")


while True:
    salir=input("Si desea finalizar escriba SALIR o presione ENTER para continuar: ").lower()
    if salir =="salir":
        print("Programa Finalizado")
        break

    num1=input("Teclea el primer Número: ")
    num2=input("Teclea el Segundo Número: ")
   
    try:
        valor1=float(num1)
        valor2=float(num2)
    except:
        print("Escriba un número Válido")
        continue

    operacion=input("Escriba que operación desea realizar: + - * / ")

    if operacion=="+":
        r1=valor1 + valor2
        print("El resultado es: ", r1)

    elif operacion=="-":
        r2=valor1-valor2
        print("El resultado es: ",r2)

    elif operacion=="*":
        r3=valor1*valor2
        print("El resultado es: ",r3)

    elif operacion=="/":
        r4=valor1/valor2
        print("El resultado es: ",r4)

    else:
        print("Solicitud Incorrecta")

    



