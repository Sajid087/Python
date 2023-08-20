# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found!")

# Function to display all tasks
def display_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            print("- " + task)

# Main program loop
while True:
    print("\n--- MENU ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Option Selection")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("--- OPTION SELECTION ---")
        option = input("Choose an option (A, B, C): ")

        if option == "A":
            print("You selected option A.")
            # Add your logic and functionality for option A here

        elif option == "B":
            print("You selected option B.")
            # Add your logic and functionality for option B here

        elif option == "C":
            print("You selected option C.")
            # Add your logic and functionality for option C here

        else:
            print("Invalid option selected.")

    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
