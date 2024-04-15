#Recursividad =  una función se llama a sí misma para resolver un problema
def Factorial(num):
    if num == 0:
        return 1
    else:
        return num * Factorial(num-1)

a = Factorial(5)
print(a)

