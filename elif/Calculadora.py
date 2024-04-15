resul = 0
op = int(input('''Elige una de las siguientes operaciones aritmetica
1)Suma
2)Resta
3)Multiplicacion
4)Division
'''))
num1 = float(input("Ingresa tu primer numero:"))
num2 = float(input("Ingresa tu segundo numero:"))

if op == 1:
    resul = num1+num2
    print("El resultado de tu suma es:",resul)

elif op == 2:
    resul = num1 - num2
    print("El resultado de tu resta es:", resul)

elif op ==3:
    resul = num1 * num2
    print("El resultado de tu multiplicacion es:",resul)

elif op == 4:
    resul = num1 / num2
    print("El resultado de tu division es:",resul)


else:
    print("Opcion no valida")