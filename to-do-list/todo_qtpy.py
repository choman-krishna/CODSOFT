from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5 import uic

class MyGUI(QMainWindow):

    # variables 
    tasks = 0

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('todo.ui', self)
        self.show()

        # Push-Button
        self.add.clicked.connect(self.insert)
        self.completed.clicked.connect(self.mark_completed)
        self.restart.clicked.connect(self.reset_all)
        self.delete_2.clicked.connect(exit)

        # Text view-list Model
        # object for model
        self.model = QStandardItemModel()
        # Set text_view to model 
        self.listView.setModel(self.model)

    
    def insert(self):
        
        # add the task
        text = QStandardItem(self.input_field.text())
        self.model.appendRow(text)
        self.tasks += 1

        # Enable Completed and Reset
        if self.tasks != 0:
            self.completed.setEnabled(True)
            self.restart.setEnabled(True)

        # Clear the text field
        self.input_field.setText("")

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