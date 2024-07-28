import tkinter as tk
from tkinter import messagebox

def display_todo_list():
    listbox.delete(0, tk.END)
    for i, task in enumerate(todo_list, 1):
        status = "Completed" if task['completed'] else "Pending"
        listbox.insert(tk.END, f"{i}. {task['name']} - {status}")

def add_task():
    task_name = entry_task.get()
    if task_name:
        todo_list.append({'name': task_name, 'completed': False})
        entry_task.delete(0, tk.END)
        display_todo_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task name.")

def mark_task_completed():
    try:
        task_index = int(entry_task_index.get()) - 1
        if 0 <= task_index < len(todo_list):
            todo_list[task_index]['completed'] = True
            entry_task_index.delete(0, tk.END)
            display_todo_list()
        else:
            messagebox.showwarning("Index Error", "Invalid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid task number.")

def remove_task():
    try:
        task_index = int(entry_task_index.get()) - 1
        if 0 <= task_index < len(todo_list):
            todo_list.pop(task_index)
            entry_task_index.delete(0, tk.END)
            display_todo_list()
        else:
            messagebox.showwarning("Index Error", "Invalid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid task number.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Initialize the task list
todo_list = []

# Create widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=5)

entry_task_index = tk.Entry(root, width=10)
entry_task_index.pack(pady=5)

btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack(pady=5)

btn_mark_completed = tk.Button(root, text="Mark as Completed", command=mark_task_completed)
btn_mark_completed.pack(pady=5)

btn_remove = tk.Button(root, text="Remove Task", command=remove_task)
btn_remove.pack(pady=5)

# Start the main event loop
root.mainloop()
