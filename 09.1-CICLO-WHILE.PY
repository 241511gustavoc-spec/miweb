while True:

    print("CONVERTIDOR DE GRADOS CELSIUS A FARENHEIT ")

    temp= input("Teclea una temperatura (o 'Salir' si desea cerra el programa):").lower()

    if temp=="salir":
        print("Programa Finalizado 🫡")
        break

    try:
        valor=float(temp)
    except:
        print("Coloque un número válido")
        continue

    conv=input("¿Desea convertir los grados a FARENHEIT o CELSIUS?:").lower()

    if conv in ["f","fahrenheit"]:#El IN busca en la lista si el usuario tecleo alguna de esas opciones.
        result=(valor * 1.8) + 32
        print("El resultado es:",result,"° F")

    elif conv in ["c","celsius"]:
        result2=(valor-32)*(5/9)
        print("El resultado es:",result2,"° C")

    else:
        print("Error en la solicitud")