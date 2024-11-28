# Lista para almacenar los alumnos
alumnos = []

# Función para mostrar la lista de alumnos con su formato
def mostrar_alumnos(lista):
    if len(lista) == 0:
        print("No hay alumnos registrados.")
    else:
        for i in range(len(lista)):
            alumno = lista[i]
            print(f"{i}. {alumno['apelidos']}, {alumno['nome']}: {alumno['nota']}")

# Función para ingresar un nuevo alumno
def ingresar_alumno():
    nome = input("Introduce el nombre del alumno: ")
    apelidos = input("Introduce los apellidos del alumno: ")
    nota = float(input("Introduce la nota del alumno: "))
    alumnos.append({"nome": nome, "apelidos": apelidos, "nota": nota})

# Función para eliminar un alumno
def eliminar_alumno(indice):
    return alumnos.pop(indice)

# Función para modificar la nota de un alumno
def modificar_nota(indice, nueva_nota):
    alumnos[indice]["nota"] = nueva_nota

# Función para calcular la nota media
def calcular_nota_media():
    total = 0
    for alumno in alumnos:
        total += alumno["nota"]
    return total / len(alumnos) if len(alumnos) > 0 else None

# Función para ordenar alumnos alfabéticamente sin usar sorted
def ordenar_alumnos():
    for i in range(len(alumnos)):
        for e in range(len(alumnos) - i - 1):
            if alumnos[e]["apelidos"] > alumnos[e + 1]["apelidos"] or \
               (alumnos[e]["apelidos"] == alumnos[e + 1]["apelidos"] and alumnos[e]["nome"] > alumnos[e + 1]["nome"]):
                alumnos[e], alumnos[e + 1] = alumnos[e + 1], alumnos[e]

while True:
    print("\nMenú de aplicación:")
    print("a) Ingresar datos alumno")
    print("b) Eliminar datos alumno")
    print("c) Modificar nota alumno")
    print("d) Ver nombres y apellidos de alumnos aprobados")
    print("e) Mostrar alumnos alfabéticamente")
    print("f) Ver la nota media")
    print("g) Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "a":
        try:
            ingresar_alumno()
            print("Alumno añadido correctamente.")
        except Exception as e:
            print("Error al ingresar los datos del alumno:", e)
    
    elif opcion == "b":
        try:
            if len(alumnos) == 0:
                print("No hay alumnos para eliminar.")
            else:
                mostrar_alumnos(alumnos)
                indice = int(input("Introduce el índice del alumno a eliminar: "))
                if 0 <= indice < len(alumnos):
                    eliminado = eliminar_alumno(indice)
                    print("Alumno eliminado:", eliminado["apelidos"], eliminado["nome"])
                else:
                    print("Índice no válido.")
        except Exception as e:
            print("Error al eliminar el alumno:", e)
    
    elif opcion == "c":
        try:
            if len(alumnos) == 0:
                print("No hay alumnos para modificar.")
            else:
                mostrar_alumnos(alumnos)
                indice = int(input("Introduce el índice del alumno a modificar: "))
                if 0 <= indice < len(alumnos):
                    nueva_nota = float(input("Introduce la nueva nota: "))
                    modificar_nota(indice, nueva_nota)
                    print("Nota modificada correctamente para", alumnos[indice]["apelidos"], alumnos[indice]["nome"])
                else:
                    print("Índice no válido.")
        except Exception as e:
            print("Error al modificar la nota del alumno:", e)
    
    elif opcion == "d":
        try:
            aprobados = [alumno for alumno in alumnos if alumno["nota"] >= 5]
            mostrar_alumnos(aprobados)
        except Exception as e:
            print("Error al mostrar los alumnos aprobados:", e)
    
    elif opcion == "e":
        try:
            ordenar_alumnos()
            mostrar_alumnos(alumnos)
        except Exception as e:
            print("Error al ordenar los alumnos:", e)
    
    elif opcion == "f":
        try:
            media = calcular_nota_media()
            if media is not None:
                print("La nota media es:", media)
            else:
                print("No hay alumnos registrados.")
        except Exception as e:
            print("Error al calcular la nota media:", e)
    
    elif opcion == "g":
        print("Saliendo de la aplicación. ¡Adiós!")
        break
    
    else:
        print("Opción no válida. Inténtalo de nuevo.")
