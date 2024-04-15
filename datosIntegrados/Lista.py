lista = ['rojo','verde','azul']
print(type(lista))

#Mostra la lista
print(lista)

#Agregar un elemento
lista.append('morado')
print(lista)

#agregar un elemento de una posicion en especifico
lista.insert(1,'Amarillo')

#eliminar ese elemento
lista.pop()
print(lista)

#eliminar un elemento especifico
lista.remove('rojo')
print(lista)

#reversa de una lista
lista.reverse()
print(lista)

lista.append('rosa')
print(lista)

#recorre nuestra lista
for i in lista:
    print(i,end=" ")

listanueva =['Lunes','Martes','Miercoles','Jueves','Lunes']
print(listanueva,end=" ")
