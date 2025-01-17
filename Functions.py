#Description: This file contains the functions that will be used in the main program.
#Author: Jose Alexander Sotelo Opayome
#First function: add_task
def add_task(tasks:list)->list:
    """Añade una tarea a la lista de tareas."""
    #I ask the user for the task
    task = input("Introduce el nombre de la tarea: ").strip().title()
    #I add the task to the list
    tasks.append(f"[ ] {task}")
    print("Tarea añadida.")
#Second function: complete_task
def complete_task(tasks:list)->list:
    #I ask the user for the numeration of the task to complete
    index = int(input("Introduce el número de la tarea completada: "))
    #I substract 1 to get the index
    index -= 1
    #I check if the index is valid
    if index>=0 and index<len(tasks):
        #I replace the task mark with the completed task mark
        tasks[index] = tasks[index].replace("[ ]", "[✔]")
        print("Tarea completada.")
    else:
        print("Esta tarea no se encuentra en la lista.") 
#Third function: show_tasks
def show_tasks(tasks:list)->str:
    print("Lista de tareas:")
    #I create a string to store the tasks
    result = ""
    #I check if there are tasks
    if not tasks:
        return "No hay tareas añadidas aún."
    #I get the tasks with their numeration
    for i, task in enumerate(tasks, 1):
        #I add the task to the string
        result += f"{i}. {task}\n"
    #I return and remove the last line break
    return result.strip()
