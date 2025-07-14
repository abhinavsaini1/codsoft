import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x550")
root.config(bg="white")

tasks = []

# Functions
def add_task():
    task = e.get()
    if task.strip() == "":
        messagebox.showwarning("Empty Input", "Please enter a task.")
    else:
        listbox.insert(tk.END, task)
        tasks.append(task)
        e.delete(0, tk.END)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except IndexError:
        messagebox.showwarning("No Selection", "Please select task to delete.")

def mark_as_done():
    try:
        index = listbox.curselection()[0]
        task_text = listbox.get(index)
        if not task_text.endswith("✅"):
            listbox.delete(index)
            task_text += " ✅"
            listbox.insert(index, task_text)
            tasks[index] = task_text
    except IndexError:
        messagebox.showwarning("Please select a task to mark as done.")

def clear_all():
    if messagebox.askyesno("Clear All", "Are you sure to delete all tasks?"):
        listbox.delete(0, tk.END)
        tasks.clear()

# Widgets
e = tk.Entry(root, font=("Arial", 14), width=25)
e.pack(pady=10, ipady=10) 

add_btn = tk.Button(root, text="Add Task", command=add_task, width=20, bg="light green")
add_btn.pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 12), height=15, width=35, selectbackground="light blue")
listbox.pack(pady=10,ipady=8)

done_btn = tk.Button(root, text="Mark as Done ✅", command=mark_as_done, bg="yellow", width=20)
done_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Selected", command=delete_task, bg="orange", width=20)
delete_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear All", command=clear_all, bg="blue", width=20)
clear_btn.pack(pady=5)

root.mainloop()