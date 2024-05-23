import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List by @Rushaad Haradhwala")

#Create GUI

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=15, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side = tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

def add_task():
    task = entry_task.get()
    if task != "":
            listbox_tasks.insert(tkinter.END, task)
            entry_task.delete(0,tkinter.END)
    else:
          tkinter.messagebox.showwarning(title= "Warning!", message = "You have not entered a Task")


def delete_task():
      try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
      except:
           tkinter.messagebox.showwarning(title= "Warning!", message = "You have not selected a Task")
              
def load_tasks():
      try: 
            tasks = pickle.load(open("tasks.dat","rb"))
            listbox_tasks.delete(0, tkinter.END)
            for task in tasks:
                  listbox_tasks.insert(tkinter.END, task)
      except:
            tkinter.messagebox.showwarning(title= "Warning!", message = "Cannot load tasks as the file does not exist")
def save_tasks():
      tasks = listbox_tasks.get(0,listbox_tasks.size())
      pickle.dump(tasks, open("tasks.dat", "wb"))



entry_task = tkinter.Entry(root, width=50,)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add Task", width=42, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete Task", width=42, command=delete_task)
button_delete_task.pack()

button_load_task = tkinter.Button(root, text="Load Tasks", width=42, command=load_tasks)
button_load_task.pack()

button_save_task = tkinter.Button(root, text="Save Tasks", width=42, command=save_tasks)
button_save_task.pack()








root.mainloop()