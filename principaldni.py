#Un constructor, donde los datos pueden estar vacíos.
#Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#mostrar(): Muestra los datos de la persona.
#esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

import clasedni as c
import os

documento = c.documento()

def ingresardatos():
    try:
        os.system("cls")
        nombre = input("Nombre : ")
        edad = int(input("Edad: "))
        dni = input("DNI: ")
        persona = c.persona(nombre,edad,dni)
        documento.AgregarDatos(persona)
    except:
        print("Parece que hubo un error")

def datos():
    while True:
        os.system("cls")
        print("1. ingresa Datos personales")
        print("2. Mostrar los Ingresado")
        print("3. EXIT")
        try:
            opcion = int(input("Opcion = "))
            if opcion == 1:
                ingresardatos()
            elif opcion == 2:
                print("Mostrar Datos personales")
                documento.mostrar()
                os.system("pause")
            elif opcion == 3:
                break
            else:
                print("Lo siento hubo un ERROR")
        except:
            print("Lo siento no queremos incovenientes queremos que usted ingrese datos requeridos")

def main():
    datos()

if __name__ == "__main__":
    main()

