diccionario ={
               "modelo": "ford",
               "precio": 70000,
                "color": "rojo"

}
#obtener el valor de un elemento del diccionario
x = diccionario.get("modelo")
print(x)

#Te regresa las claves de tu diccionario
x = diccionario.keys()
print(x)

#Te regresa el valor de tu diccionario
x = diccionario.values()
print(x)

# items() método devolverá cada elemento de un diccionario, como tuplas en una lista.#
x = diccionario.items()
print(x)


#Comprobar si la clave existe
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}

if 'color' in thisdict:
    print("si existe")
else:
    print("No existe \n")

#recorrer el diccionario y imprimir sus valores
print("imprimr valores:")
for x in thisdict.values():
    print(x)


#recorrer el diccionario y imprimir sus valores
print("imprimir claves:")
for x in thisdict.keys():
 print(x)
