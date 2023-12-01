from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x500+500+200")



        #----------------------------- Menu ------------------------------------------
        self.todo_menu = Menu(root)

        # File Menu
        self.m1 = Menu(self.todo_menu, tearoff=0)
        self.m1.add_command(label="New", command=refresh)
        self.m1.add_command(label="Uncompleted", command=uncompleted)
        self.m1.add_command(label="Save", command=save)

        self.todo_menu.add_cascade(label="File", menu=self.m1)

        # Other Menu
        self.todo_menu.add_command(label="Download", command=download)

        self.root.config(menu = self.todo_menu)



# Menu Functions 
def refresh():
    pass
def save():
    pass
def uncompleted():
    pass
def download():
    pass

def main():
    root = Tk()
    win = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()