class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def complete_task(self, task_index):
        if task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.completed = True

    def remove_task(self, task_index):
        if task_index < len(self.tasks):
            del self.tasks[task_index]

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "[X]" if task.completed else "[ ]"
            print(f"{i+1}. {status} {task.description}")

# Запуск програми
if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("----- To-Do List -----")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            task_index = int(input("Enter task index: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == "3":
            task_index = int(input("Enter task index: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == "4":
            todo_list.view_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")