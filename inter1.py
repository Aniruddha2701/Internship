import tkinter as tk
from tkinter import messagebox, simpledialog

class Task:
    def __init__(self, title, description='', completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        return f"{'[x]' if self.completed else '[ ]'} {self.title}: {self.description}"

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.refresh_task_list()

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, str(task))

    def add_task(self):
        title = simpledialog.askstring("Task Title", "Enter task title:")
        if title:
            description = simpledialog.askstring("Task Description", "Enter task description:")
            task = Task(title, description)
            self.tasks.append(task)
            self.refresh_task_list()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            title = simpledialog.askstring("Update Task Title", "Enter new task title:", initialvalue=self.tasks[index].title)
            if title:
                description = simpledialog.askstring("Update Task Description", "Enter new task description:", initialvalue=self.tasks[index].description)
                self.tasks[index].title = title
                self.tasks[index].description = description
                self.refresh_task_list()
        else:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.refresh_task_list()
        else:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()