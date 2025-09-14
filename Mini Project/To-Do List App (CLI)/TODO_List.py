tasks = [] # List vide Au debut vide

# Ajout dans la liste
def add_task(task):
    tasks.append(task)
    print(f"Task {task} Added!!")

# Remeove de la liste 
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed!")
    else:
        print(f"Task '{task}' not found.")

#Show Liste
def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

add_task("Learn Python")
add_task("Build a project")
show_tasks()

remove_task("Learn Python")
show_tasks()