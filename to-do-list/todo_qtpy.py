from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('todo.ui', self)
        self.show()

        # Push-Button
        self.add.clicked.connect(self.insert)
        self.completed.clicked.connect(self.mark_completed)
        self.restart.clicked.connect(self.reset_all)
        self.delete_2.clicked.connect(exit)
    
    def insert(self):
        pass
    def mark_completed(self):
        pass
    def reset_all(self):
        pass



def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()