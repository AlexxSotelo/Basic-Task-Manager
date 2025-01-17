
![Proyecto web](https://github.com/user-attachments/assets/a0ef80d6-09f4-4fdb-86cf-69f4c6731f53)

# Basic Task Manager

A simple command-line task manager to add, complete, and view tasks. This project demonstrates basic task management features like adding, completing, and displaying tasks.

### **Created for fun and practice**

I created this project to practice Python syntax and improve my coding skills. It was a fun way to experiment with task management functionalities and understand how to work with lists and basic control flow. If you have any suggestions or feedback, feel free to let me know! 😊

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Test Functions](#test-functions)
- [Contributing](#contributing)

## Installation

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/AlexxSotelo/Basic-Task-Manager.git
cd Basic-Task-Manager
```
## Usage
The program will present a simple menu with the following options:
```markdown
---MENÚ---
1. Añadir tarea
2. Marcar tarea como completada
3. Ver lista de tareas
4. Salir
```
Select an option by entering the corresponding number (e.g., 1 to add a task, 2 to mark a task as completed).

### Option 1: **Add a task**
When you choose to add a task (option 1), the application will prompt you to enter the name of the task:
```yaml
Introduce el nombre de la tarea:
```
After entering the task name, it will be added to the list, and you will see:
```css
Tarea añadida.
```
### Option 2: **Mark a task as completed**
If you select option 2, the application will ask you to enter the task number that you want to mark as completed:
```yaml
Introduce el número de la tarea completada:
```
Once you input the number, the task will be marked as completed, and you will see a message like this:
```
Tarea completada.
```
### Option 3: **View the list of tasks**
Choosing option 3 will display the current list of tasks with their numbers and completion status. A task that is completed will have a checkmark, and an incomplete task will have an empty box. For example:
```less
Lista de tareas:
1. [ ] Comprar comida
2. [✔] Estudiar Python
```
### Option 4: **Exit**
Selecting option 4 will exit the program with the message:
```
Gracias por usar TaskManager.
```
Now you're ready to manage your tasks using the Basic Task Manager! 😄

## Test Functions
You can test the core functions of the project using the unittest module in Python. Below is a basic test suite to test the functions of add_task, complete_task, and show_tasks.

**Example Test (test_functions.py):**
```python
import unittest
from Functions import add_task, complete_task, show_tasks

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        """Set up a new task list for each test."""
        self.tasks = []

    def test_add_task(self):
        """Test adding a task to the list."""
        add_task(self.tasks)
        self.assertEqual(len(self.tasks), 1)
        self.assertIn("[ ]", self.tasks[0])

    def test_complete_task(self):
        """Test marking a task as completed."""
        add_task(self.tasks)  # Add a task
        complete_task(self.tasks)  # Complete the first task
        self.assertIn("[✔]", self.tasks[0])

    def test_show_tasks(self):
        """Test showing tasks."""
        add_task(self.tasks)
        result = show_tasks(self.tasks)
        self.assertIn("1.", result)  # Check if task number appears
        self.assertIn("[ ]", result)  # Ensure the task is listed

if __name__ == "__main__":
    unittest.main()
```
### **Running the tests**
To run the tests, simply execute the following command:
```bash
python -m unittest test_functions.py
```
## Contributing
If you want to contribute to the project, feel free to fork it, create a branch, and submit a pull request with your improvements.

Please ensure your code follows the same style as the existing code and add relevant tests if you're making changes to functionality.
