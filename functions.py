#Description: This file contains the functions that will be used in the main program.
#Author: Jose Alexander Sotelo Opayome
#First function: add_task
def add_task(tasks: list, task_name: str):
    """Añade una tarea a la lista de tareas."""
    task = {"name": task_name, "completed": False}  # Guarda como diccionario
    tasks.append(task)
    print("Tarea añadida.")

#Second function: complete_task
def complete_task(tasks: list, task_id: int):
    """Marca una tarea como completada."""
    if 0 <= task_id < len(tasks):  # Verifica que el índice sea válido
        tasks[task_id]["completed"] = True  # Cambia el estado de la tarea
        print("Tarea completada.")
    else:
        print("Error: La tarea no existe.")

#Third function: show_tasks
def show_tasks(tasks: list) -> str:
    """Devuelve una lista de tareas numeradas en formato de string."""
    if not tasks:
        return "No hay tareas añadidas aún."
    
    # Construcción eficiente del resultado con join()
    result = "\n".join(f"{i}. {task}" for i, task in enumerate(tasks, 1))
    return result

#Fourth function: clear_tasks
def clear_tasks(tasks: list):
    """Elimina todas las tareas de la lista."""
    tasks.clear()
    print("Lista de tareas vaciada.")

