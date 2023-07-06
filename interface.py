import tkinter as tk
from program_logic import display_tasks, add_task, remove_task, tasks

def display_tasks_command():
    display_tasks()
    update_task_text()

def add_task_command():
    task = entry.get()
    if task:
        add_task(task)
        entry.delete(0, tk.END)
        display_tasks_command()

def remove_task_command():
    task_index = int(entry.get())
    remove_task(task_index)
    display_tasks_command()

def update_task_text():
    if len(tasks) == 0:
        task_text.set("No tasks to display.")
    else:
        task_text.set("Tasks:\n" + "\n".join(f"{index + 1}. {task}" for index, task in enumerate(tasks)))

# Create the main window
window = tk.Tk()
window.title("Task Manager")

# Create and configure the task display label
task_text = tk.StringVar()
task_label = tk.Label(window, textvariable=task_text, justify=tk.LEFT)
task_label.pack()

# Create the entry field for task input
entry = tk.Entry(window)
entry.pack()

# Create the buttons
display_button = tk.Button(window, text="Display tasks", command=display_tasks_command)
display_button.pack()

add_button = tk.Button(window, text="Add task", command=add_task_command)
add_button.pack()

remove_button = tk.Button(window, text="Remove task", command=remove_task_command)
remove_button.pack()

# Start the main event loop
window.mainloop()
