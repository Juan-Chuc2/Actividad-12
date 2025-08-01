print("Bienvenido")
estudiantes ={}
try:
    cant_estudents = int(input("Ingrese la cantidad de esudiantes que desea ingresar"))
    for i in range(cant_estudents):
        print(f"Estudiante #{i+1}")
        name = input("Ingrese Su nombre")
        cant_nots = int(input("Ingrese la cantidad de notas que desea ingresar"))
        for j in range(cant_nots):
            notas = float(input(f"Ingrese la nota {j+1}"))
