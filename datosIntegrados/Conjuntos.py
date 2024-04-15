paletaPrimario ={'rojo','verde','azul'}
paletaSecundario = {'naranja','amarillo'}
paletaPrimario.update(paletaSecundario)
print(type(paletaPrimario))
print(len(paletaPrimario))
print(paletaPrimario)

#remover un elemento
conjunt = {'a','b','c','d'}
print(conjunt)
conjunt.remove('a')
print(conjunt)


#Unir varios conjuntos
a = {'a','b','c'}
b ={1,2,3,4,}
c ={'M','F'}
d = {'Linea blanca','Electronica'}

resultado = a.union(b,c,d)
print(resultado)
#El uso que tiene un conjunto es que eliminina un elemnto duplicado