
#ADDING TASK
def add_task():
    task = input("task: ")
    with open('ToDolist.txt', 'a') as f:
        f.write(task +'\n')
#DISPLAYING A TASK
def display_task():
    try:
        with open('ToDolist.txt', 'r') as f:
            tasks = f.readlines()
            if tasks:
                print("\nYour To-Do List:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task.strip()}")
            else:
                print("\nYour To-Do List is empty!")
    except FileNotFoundError:
        print("\nNo To-Do List found. Start by adding tasks.")

#REMOVING A TASK
def remove_task(file_name):
    try:
        with open(file_name, 'r') as f:
            tasks = f.readlines()
        
        if not tasks:
            print("\nYour To-Do List is empty!")
            return
        
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task.strip()}")
        
        try:
            index = int(input("\nEnter the task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                del tasks[index]
                with open(file_name, 'w') as f:  # Overwrite the file with updated tasks
                    f.writelines(tasks)
                print("Task removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    except FileNotFoundError:
        print("\nNo To-Do List found. Start by adding tasks.")




    

while True:
    choice = input("CHOOSE: \n(a).to add task \n(r).to remove task \n(q).to quit \n(d).to display \n\n")
    if choice == "q":
        print("byeeee")
        break
    elif choice == "a":
       add_task()
    elif choice == "d":
        display_task() 
    elif choice == "r":
        
        remove_task('ToDolist.txt')
    else:
        print("enter a valid")
        
