import tkinter as tk
from tkinter import messagebox
import json
import os

TODO_FILE = 'todo.json'

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

def add_task():
    task = task_entry.get()
    if task:
        todos.append({"task": task, "done": False})
        save_todos(todos)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def update_listbox():
    listbox.delete(0, tk.END)
    for i, todo in enumerate(todos):
        status = "Done" if todo["done"] else "Not Done"
        listbox.insert(tk.END, f"{i + 1}. {todo['task']} - {status}")

def mark_done():
    selected_task = listbox.curselection()
    if selected_task:
        index = selected_task[0]
        todos[index]["done"] = True
        save_todos(todos)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "You must select a task.")

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        index = selected_task[0]
        todos.pop(index)
        save_todos(todos)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "You must select a task.")

def update_task():
    selected_task = listbox.curselection()
    if selected_task:
        index = selected_task[0]
        new_task = task_entry.get()
        if new_task:
            todos[index]["task"] = new_task
            save_todos(todos)
            update_listbox()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    else:
        messagebox.showwarning("Warning", "You must select a task.")

todos = load_todos()

root = tk.Tk()
root.title("To-Do List Application")

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=50)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=60, height=15)
listbox.pack(pady=10)
update_listbox()

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

mark_done_button = tk.Button(buttons_frame, text="Mark as Done", command=mark_done)
mark_done_button.pack(side=tk.LEFT, padx=10)

update_button = tk.Button(buttons_frame, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(buttons_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
