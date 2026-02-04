print("CONVERTIDOR DE GRADOS CELSIUS A FARENHEIT")
temp= input("Teclea una temperatura:")
valor=float(temp)

conv=input("¿Desea convertir los grados a FARENHEIT o CELSIUS?:").lower()

if conv in ["f","fahrenheit"]:
    result=(valor * 1.8) + 32
    print("El resultado es:",result,"° F")

elif conv in ["c","celsius"]:
    result2=(valor-32)*(5/9)
    print("El resultado es:",result2,"° C")

else:
    print("Error en la solicitud")



    




