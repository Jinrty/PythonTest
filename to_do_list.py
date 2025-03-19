import json

def load_tasks(file_path):  #This function takes as an argument path to file and returns it
    with open(file_path, 'r') as file:
        return json.load(file)

def save_tasks(tasks, file_path): #This function takes as an argument path and task and saves it
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(file_path, task_description): #This function takes as an argument path and  descripttion of an task to add to given file
    tasks = load_tasks(file_path)
    task_id = len(tasks) + 1
    new_task = {'id': task_id, 'description': task_description, 'completed': False}
    tasks.append(new_task)
    save_tasks(tasks, file_path)

def remove_task(file_path, task_id): #This function takes as an argument path and ID to remove task from the given file by ID
    tasks = load_tasks(file_path)
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks, file_path)

def mark_task_completed(file_path, task_id): ##This function takes as an argument path and ID changes completed value to True by ID in given file
    tasks = load_tasks(file_path)
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
    save_tasks(tasks, file_path)

def list_tasks(file_path): #It just loads tasks from file
    tasks = load_tasks(file_path)
    return tasks

def space_beetwen(): #it prints nothinfg 3 times. I needed it for visual purposes
    print("")
    print("")
    print("")

while True: # basic while loop and menu
    print("1 Display")
    print("3 Add")
    print("4 Remove")
    print("5 Mark Completed")
    print(" ")
    choice = input("What do you want to do? (enter number) : ")
    if choice == "1":
        print(load_tasks("tasks.json"))
        space_beetwen()
        pass
    if choice == "2":
        print("I cant count and I realised to late so it is not a mistake but an ester egg")
        space_beetwen()
    if choice == "3":
        description = input("Desrcibe task: \n")
        add_task("tasks.json", description)
        print("Succesfuly saved")
        space_beetwen()
        pass
    if choice == "4":
        something = int(input("Give id of task you want to remove: \n"))
        remove_task("tasks.json", something)
        print("If that task existed then is is delted")
        space_beetwen()
        pass
    if choice == "5":
        id = int(input("Give id of task you want to mark as done: \n"))
        mark_task_completed("tasks.json", id)
        print("It's now marked as completed")
        space_beetwen()
        pass
    else:
        pass
