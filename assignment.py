class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, index):
        del self.tasks[index]

    def mark_completed(self, index):
        self.tasks[index]["completed"] = True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks):
                status = "✓" if task["completed"] else " "
                print(f"{i + 1}. [{status}] {task['task']}")

def main():
    todo_app = TodoApp()

    while True:
        print("\nTodo List:")
        todo_app.display_tasks()
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_app.add_task(task)
        elif choice == "2":
            index = int(input("Enter task number to delete: ")) - 1
            todo_app.delete_task(index)
        elif choice == "3":
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_app.mark_completed(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
