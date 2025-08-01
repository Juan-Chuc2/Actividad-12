print("Bienvenido")
estudiantes ={}
while True:
    try:
        cant_estudents = int(input("Ingrese la cantidad de esudiantes que desea ingresar: "))
        for i in range(cant_estudents):
            print(f"Estudiante #{i+1}")
            carnet = input("Ingrese su numero de carnet: ")
            name = str(input("Ingrese Su nombre: "))
            cant_nots = int(input("Ingrese la cantidad de notas que desea ingresar: "))
            nots = []
            for j in range(cant_nots):
                notas = float(input(f"Ingrese la nota {j+1}: "))
                nots.append(notas)
            promedio = sum(nots) / len(nots)
            estudiantes[carnet] = {
                    "Nombre": name,
                    "Notas Igresadas": cant_nots,
                    "Promedio": promedio
                }
    except ValueError:
        print("Error ingrese numeros validos")
    except TypeError:
        print("No se puede sumar un entero con un texto")
    except ZeroDivisionError:
        print("No se puede dividir dentro de 0")
    except Exception as e:
        print("Se ha producido un error no identificado")
    else:
        print("\n --Promedio--")
        for carnet, datos in estudiantes.items():
            print(f"Estudiante: {datos['Nombre']} -- Promedio {datos['Promedio']}")
        break