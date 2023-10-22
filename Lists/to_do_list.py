#Creatin a to do list application.

todo_list = []

#Adding items to the to-do list:
while True:
    task = input("Enter a task (or 'q' to quit): ")
    if task == 'q':
        break
    todo_list.append(task)

#Function that displays the to-do list:
def display_todo_list(todo_list):
    for index, task in enumerate(todo_list, 1):
        print(f"{index}. {task}")

#Updatin tasks as done and update the list:
def mark_task_done(todo_list, index):
    if 1 <= index <= len(todo_list):
        del todo_list[index - 1]
    else:
        print("Invalid index. Task not found")

#Creating the menu for the user to interact with, add tasks, view the list, mark as done and exit the program.
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View List")
    print("3. Mark Task as Done")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter a task: ")
        todo_list.append(task)
    elif choice == '2':
        display_todo_list(todo_list)
    elif choice == '3':
        index = int(input("Enter the task number to mark as done (remove from list)"))
        mark_task_done(todo_list, index)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose from the menu")