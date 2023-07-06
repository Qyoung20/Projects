tasks = []

def display_tasks():
    if len(tasks) == 0:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def add_task(task):
    tasks.append(task)
    print("Task added successfully.")

def remove_task(task_index):
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index.")
    else:
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed successfully.")