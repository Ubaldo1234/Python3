def Formulario():
    nombre = input("Ingresa tu nombre:")
    apellidoP = input("Ingresa tu apellido paterno:")
    apellidoM = input("Ingresa tu apellido materno:")
    tel = int(input("Ingresa tu numero telefico:"))
    direccion = input("Ingresa tu domicilio:")

    return print(f"{nombre} {apellidoP} {apellidoM} {tel} {direccion}")