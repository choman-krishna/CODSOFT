from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x500+500+200")


def main():
    root = Tk()
    win = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()