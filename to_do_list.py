import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks_to_file()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        save_tasks_to_file()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def save_tasks_to_file():
    tasks = listbox.get(0, tk.END)
    with open("data.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack widgets
frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame, text="Enter Task:")
label.grid(row=0, column=0, padx=5)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Load tasks from file if it exists
try:
    with open("data.txt", "r") as file:
        tasks = file.read().splitlines()
        for task in tasks:
            listbox.insert(tk.END, task)
except FileNotFoundError:
    pass

# Run the Tkinter event loop
root.mainloop()
