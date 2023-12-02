from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QTextCharFormat
from PyQt5 import uic

class MyGUI(QMainWindow):

    # variables 
    tasks = 0
    completed_count = 0

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

        # LCD
        # object for lcd
        self.lcd_tasks = self.findChild(QLCDNumber, "task_count_display_2")
        self.lcd_uncompleted = self.findChild(QLCDNumber, "un_count_display")
        

        

    # Add to list 
    def insert(self):
        
        # add the task
        text = QStandardItem(self.input_field.text())
        self.model.appendRow(text)
        self.tasks += 1
        self.lcd_tasks.display(self.tasks)

        # Enable Completed and Reset
        if self.tasks != 0:
            self.completed.setEnabled(True)
            self.restart.setEnabled(True)            

        # Clear the text field
        self.input_field.setText("")

    # Mark complete
    def mark_completed(self):

        if len(self.listView.selectedIndexes()) != 0:

            selected_index = self.listView.selectedIndexes()[0]
            sel_item = self.model.itemFromIndex(selected_index)

            change_font = QTextCharFormat()
            change_font.setFontStrikeOut(not sel_item.font().strikeOut())

            sel_item.setFont(change_font.font())
            
            if sel_item.font().strikeOut():
                self.completed_count += 1
                self.tasks -= 1
            else:
                self.completed_count -= 1
                self.tasks += 1

            self.lcd_uncompleted.display(self.completed_count)


        else:
            caution_box = QMessageBox()
            caution_box.setWindowTitle("CAUTION")
            caution_box.setText("No Task Selected")
            caution_box.exec_()

    def reset_all(self):
        pass



def main():
    app = QApplication([])
    window = MyGUI()
    
    app.exec_()

if __name__ == "__main__":
    main()