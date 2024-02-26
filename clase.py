nombre =  input("Ingrese el nombre: ")
edad = input("Ingrese su edad: ")
altura = input("Ingrese la altura: ")
informacion = tuple((nombre, edad, altura))

Direccion1 = input(("Ingrese su direccion principal: "))
Direccion2 = input (("Ingrese su direccion secundaria: "))
Direcciones = tuple((Direccion1, Direccion2))

colegio1 = input("Ingrese el nombre el primer colegio al que ingreso: ")
colegio2 = input("Ingrese el nombre del segundo colegio al que ingreso: ")
colegios = tuple((colegio1, colegio2))

trabajo = input("Ingrese el nombre de la empresa  en la que trabaja: ")
experiencia = int(input("Ingrese los años de experiencia laboral que tiene en ese sector: "))
trabajos = tuple((trabajo, experiencia))

print(f"""
Usuario: {informacion}
Direcciones: {Direcciones}
Colegios: {colegios}
Trabajos: {trabajos}
""")