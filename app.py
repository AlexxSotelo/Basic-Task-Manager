from flask import Flask, render_template, request, redirect, url_for
import functions as fn  # Asegúrate de que este archivo existe y está en la misma carpeta


app = Flask(__name__)
tasks = []  # Lista para almacenar las tareas

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task", "").strip()
    
    if not task_name:
        return "Error: No ingresaste una tarea.", 400

    fn.add_task(tasks, task_name)
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    """Marca una tarea como completada."""
    if 0 <= task_id < len(tasks):  # Validación para evitar errores de índice
        fn.complete_task(tasks, task_id)
    else:
        app.logger.warning(f"Intento de completar tarea inexistente con ID {task_id}")
    
    return redirect(url_for("index"))

@app.route("/clear", methods=["POST"])
def clear():
    fn.clear_tasks(tasks)
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)