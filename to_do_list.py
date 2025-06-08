#to do list
counter = 0

def view_tasks():
    try:
        with open("tasks.txt" , "r") as f:
            tasks = f.readlines()
            if tasks:
                for i,task in enumerate(tasks,1):
                    print(f"{i}.{task.strip()}")
            else:
                print("Your to-do list is empty.")

    except FileNotFoundError:
        print("No tasks found yet.")

def add_task(task):
    global counter
    with open("tasks.txt","a") as f:
        f.write(task + "\n")
    counter+=1
    print("Task added")

def remove_task():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        if not tasks:
            print("No tasks to remove.")
            return
        view_tasks()
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            with open("tasks.txt" , "w") as f:
                f.writelines(tasks)
            print(f"Removed task: {removed.strip()}")
        else:
            print("Invalid task number.")
    except (FileNotFoundError, ValueError):
        print("Error: Unable to remove task.")

def clear_list():
    with open("tasks.txt" , "w"):
        pass

def stop():
    exit()

while counter <100:
    task = input("Enter task, (-) to remove, (v) to view list, (c) to clear, (q) to quit: ").strip()
    if task.lower() == "v":
        view_tasks()
    elif task == "-":
        remove_task()
    elif task =="c":
        clear_list()
    elif task == "q":
        stop()
    elif task:
        add_task(task)

    else:
        print("Enter a valid input.")
