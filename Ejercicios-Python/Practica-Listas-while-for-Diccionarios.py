animales=["perro","gato","jirafa","cochino","jaguar","león","Oveja","Caballo","Tortuga","Ave"]
familia=["Julieta","Janeli","Tadeo","Gustavo"]

for ani in animales:
    print(ani)
    
i=2
while i <=20:
    print(i)
    i=i+1


#**********************************************
for indice, Ani in enumerate(animales) :#para enlistar los elementos junto a su indice o posición.
    print(indice,Ani)

#**************************************************
#in zip: Muestra la información de dos listas diferentes.
for persona, animal in zip(familia,animales):
    print("El animal favorito de",persona,"es",animal)


#************************************************
equipos = {
    "Router": "192.168.1.1",
    "Servidor": "192.168.1.10",
    "Impresora": "192.168.1.50"
}

for dispositivo, ip in equipos.items():
    print(dispositivo, "→", ip)

#Imprime las calves del diccionario
for clave in equipos:
    print(clave)

#Imprime solo los valores del diccionario
for valor in equipos.values():
    print(valor)

#*************************************************************