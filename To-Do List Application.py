todo_list = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        todo_list.append(task)
        print("Task added successfully.")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(i, task)

    elif choice == "3":
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index] = input("Enter new task: ")
            print("Task updated.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Exiting To-Do List.")
        break

    else:
        print("Invalid choice. Try again.")
