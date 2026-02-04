lenguajes=["Python","Ruby","JavaScrip","C#","PhP","Java"]

lenguajes.insert(3,"Go")#para insertar elementos a una lista primero colocamos la pocisión o indice y posteriormente el elemento.
lenguajes.insert(0,"C")

lenguajes.remove("Ruby")#Para eliminar elementos de una lista.

print("PhP" in lenguajes)#Pregunta si el elemento PHP existe dentro de la lista lenguajes.

#lenguajes.clear() Limpia todos los elementos de la lista.

print(len(lenguajes))#Usando el método "len" nos muestra cuantos elementos contine la lista.
