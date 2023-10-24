#Self -adjusting task scheduler.

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.next = None

class TaskScheduler:
    def __init__(self):
        self.head = None

    #Function to add the tasks.
    def add_task(self):
        task_name = input("Enter task name: ")
        task_priority = int(input("Enter task priority (1 for low, 2 for medium, 3 for high): "))
        new_task = Task(task_name, task_priority)

        if not self.head:
            self.head = new_task
        else:
            if new_task.priority >= self.head.priority:
                new_task.next = self.head
                self.head = new_task
            else:
                current = self.head
                while current.next and new_task.priority < current.next.priority:
                    current = current.next
                new_task.next = current.next
                current.next = new_task
        print("Task added successfully!")

    #Function to list all the current tasks.
    def list_tasks(self):
        current = self.head
        if not current:
            print("No tasks in the list.")
            return
        print("Tasks:")
        while current:
            print(f"{current.name} (Priority: {current.priority})")
            current = current.next

    #Function to remove the tasks.
    def remove_task(self):
        self.list_tasks()
        if not self.head:
            print("No tasks to remove.")
            return
        task_name = input("Enter the name of the task to remove: ")
        if self.head.name == task_name:
            self.head = self.head.next
            print(f"Removed task: {task_name}")
        else:
            current = self.head
            while current.next and current.next.name != task_name:
                current = current.next
            if current.next:
                current.next = current.next.next
                print(f"Removed task: {task_name}")
            else:
                print(f"Task '{task_name}' not found.")

    #Main Loop
    def run(self):
        while True:
            print("\nTask Scheduler Menu: ")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Remove Task.")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                print("Exiting Task Scheduler. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__== "__main__":
    task_scheduler = TaskScheduler()
    task_scheduler.run()