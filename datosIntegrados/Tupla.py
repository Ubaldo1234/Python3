#tupla
tuplas = ('a','b','c')
print(type(tuplas))
print(tuplas)

#agregar un elemento a una tupla lo convertimos en una lista
convertir = list(tuplas)
print(type(convertir))

convertir.insert(1,'h')
print(convertir)

#desempaquetar
tupla  = ('red','green','blue')
(rojo,verde,azul) = tupla
print(rojo)
print(verde)

#Devuelve el número de veces que aparece un valor especificado en una tupla
tupla = ('rojo','verde','rojo','azul','rojo')
x=tupla.count('rojo')
print(x)

