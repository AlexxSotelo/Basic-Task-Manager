#Description: This file is the main file of the program. It shows the menu and calls the functions from the other file.
#Author: Jose Alexander Sotelo Opayome
#I import my functions from another file
import functions as fn
tasks = []
#I show different options for the cx to interact 
def main():
    print("""---MENÚ---
    1. Añadir tarea
    2. Marcar tarea como completada
    3. Ver lista de tareas
    4. Salir
    """)
    while True:
        try:
            option = int(input("ELige una opción: "))
            if option == 1:
                #I call the function from the other file
                fn.add_task(tasks)
            elif option == 2:
                fn.complete_task(tasks)
            elif option == 3:
                print(fn.show_tasks(tasks))
            elif option == 4:
                print("Gracias por usar TaskManager.")
                break
            #I raise a new restriction to void missunderstandings
            else:
                raise ValueError("Ingrese una opción correcta.")
        except ValueError:
            print("El valor ingresado es incorrecto. Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()

