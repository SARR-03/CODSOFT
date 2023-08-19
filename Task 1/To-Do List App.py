import tkinter as tk
from tkinter import messagebox


class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, font=("Verdana", 14), width=40, border="2px solid black")
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", font=("Verdana", 12), border="2px solid black", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, font=("Verdana", 14), width=40, height=10, border="2px solid black")
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", font=("Verdana", 12), border="2px solid black", command=self.delete_task)
        self.delete_button.pack()


        self.complete_button = tk.Button(root, text="Mark as Completed", font=("Verdana", 12), border="2px solid black",
                                         command=self.mark_completed)
        self.complete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[x] " if task["completed"] else "[ ] "
            self.task_listbox.insert(tk.END, status + task["task"])

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["completed"] = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
