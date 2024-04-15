#Calificacion

nombre = input('Ingresa tu nombre:')
matematicas = float(input("Ingresa tu nota de matematicas:"))
fisica = float(input("Ingresa tu nota de fisica:"))
biologia = float(input("Ingresa tu nota de biaologia:"))
historia = float(input("Ingresa tu nota de historia:"))

resultado = float((matematicas+fisica+biologia+historia)/4)

if (resultado >=6):
    print(nombre,"has aprobado tu calificacion es:", resultado)
else:
    print(nombre,"has reprovado tu calificacion es:", resultado)
