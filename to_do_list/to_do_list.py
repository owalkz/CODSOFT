import tkinter as tk
from tkinter.ttk import *

task_list = {}


class ToDoListUI:
    def __init__(self):
        self.main_page = tk.Tk()
        self.main_page.title("To-Do List")
        self.main_page.geometry("800x600")

        self.add_new_task = tk.Button(
            self.main_page,
            text="Add New Task",
            font=("Arial", 18),
            command=lambda: self.add_task(),
        )
        self.add_new_task.pack(padx=10, pady=10, fill="x")

        self.label = tk.Label(self.main_page, text="List of Tasks:", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.list_functions()

        self.main_page.mainloop()

    def list_functions(self):
        if task_list:
            i = 0
            button_name = "button" + str(i)
            for task in task_list:
                self.button_name = tk.Button(
                    self.main_page,
                    text=task,
                    font=("Arial", 11),
                    command=lambda x=task: self.view_tasks(x),
                )
                self.button_name.pack(padx=10, pady=5, fill="x")
        else:
            self.label = tk.Label(
                self.main_page, text="Wohoo! No Tasks!", font=("Arial", 11)
            )
            self.label.pack(padx=10, pady=10)

    def add_task(self):
        self.addTaskWindow = tk.Toplevel(self.main_page)
        self.addTaskWindow.geometry("600x500")
        self.addTaskWindow.title("Add New Task")

        instruction = tk.Label(
            self.addTaskWindow,
            text="Enter the Name of the task on the first line. Add each new sub-task on a newline.",
            font=("Arial", 11),
        )
        instruction.pack(padx=10, pady=10)

        self.instruction_textbox = tk.Text(self.addTaskWindow, height=10)
        self.instruction_textbox.pack(padx=10, pady=10, fill="x")

        save_task_button = tk.Button(
            self.addTaskWindow,
            text="Save Task",
            font=("Arial", 11),
            command=lambda: self.save_task(),
        )
        save_task_button.pack(padx=10, pady=10)

    def save_task(self):
        list_of_subtasks = []
        obtained = self.instruction_textbox.get("1.0", "end-1c")
        task_name, subtasks = obtained.split("\n", maxsplit=1)
        subtask_count = subtasks.count("\n")
        for _ in range(subtask_count):
            subtask, subtasks = subtasks.split("\n", maxsplit=1)
            list_of_subtasks.append(subtask)
        list_of_subtasks.append(subtasks)
        task_list[task_name] = list_of_subtasks
        self.addTaskWindow.destroy()
        self.main_page.destroy()
        ToDoListUI()

    def view_tasks(self, value):
        self.taskViewWindow = tk.Toplevel(self.main_page)
        self.taskViewWindow.geometry("500x500")
        self.taskViewWindow.title(f"Subtasks of {value}")

        tasks = task_list[value]
        for task in tasks:
            label = tk.Label(self.taskViewWindow, text=task, font=("Arial", 11))
            label.pack(padx=5, pady=5)

        complete = tk.Button(
            self.taskViewWindow,
            text="Change Task Name",
            font=("Arial", 11),
            command=lambda x=value: self.modify_name(x),
        )
        complete.pack(padx=10, pady=10, fill="x")
        complete = tk.Button(
            self.taskViewWindow,
            text="Mark as Complete",
            font=("Arial", 11),
            command=lambda x=value: self.clicked_button(x),
        )
        complete.pack(padx=10, pady=10, fill="x")

    def clicked_button(self, task):
        task_list.pop(task)
        self.taskViewWindow.destroy()
        self.main_page.destroy()
        ToDoListUI()

    def modify_name(self, taskname):
        self.taskNameChange = tk.Toplevel(self.taskViewWindow)
        self.taskNameChange.title("Change Name")
        self.taskNameChange.geometry("300x200")

        self.entry = tk.Text(self.taskNameChange, height=2)
        self.entry.pack(padx=10, pady=10)
        change_name_button = tk.Button(
            self.taskNameChange,
            text="Save New Name",
            font=("Arial", 11),
            command=lambda x=taskname: self.modify_name_fn(x),
        )
        change_name_button.pack(padx=10, pady=10)

    def modify_name_fn(self, taskname):
        newname = self.entry.get("1.0", "end-1c")
        task_list[newname] = task_list[taskname]
        del task_list[taskname]
        self.taskNameChange.destroy()
        self.taskViewWindow.destroy()
        self.main_page.destroy()
        ToDoListUI()


ToDoListUI()
