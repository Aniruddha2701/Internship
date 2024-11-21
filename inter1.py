import tkinter as tk
from tkinter import messagebox, simpledialog
class Task:
    def __init__(self, title, description='', completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        return f"{'[x]' if self.completed else '[ ]'} {self.title}: {self.description}"

    def toggle_completed(self):
        self.completed = not self.completed

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.toggle_button = tk.Button(self.button_frame, text="Toggle Task", command=self.toggle_task)
        self.toggle_button.pack(side=tk.LEFT, padx=5)

        self.refresh_button = tk.Button(self.button_frame, text="Refresh", command=self.refresh_task_list)
        self.refresh_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self.button_frame, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.load_button = tk.Button(self.button_frame, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack(side=tk.LEFT, padx=5)

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

    def toggle_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index].toggle_completed()
            self.refresh_task_list()
        else:
            messagebox.showwarning("Toggle Task", "Please select a task to toggle.")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.title}:{task.description}:{str(task.completed)}\n")
        messagebox.showinfo("Save Tasks", "Tasks saved successfully.")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = []
                for line in file.readlines():
                    title, description, completed = line.strip().split(":")
                    self.tasks.append(Task(title, description, completed == "True"))
                self.refresh_task_list()
        except FileNotFoundError:
            messagebox.showwarning("Load Tasks", "No saved tasks found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
