from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QTextCharFormat, QIcon
from PyQt5 import uic

class MyGUI(QMainWindow):

    # variables 
    tasks = 0
    completed_count = 0

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('todo.ui', self)
        self.show()
        
        self.setWindowTitle("Task Manager v1.0")
        self.setWindowIcon(QIcon("Images\logo.png"))
        self.setFixedSize(470, 594)
        # Text view-list Model
        # object for model
        self.model = QStandardItemModel()
        # Set text_view to model 
        self.listView.setModel(self.model)
        
        # Push-Button
        self.add.clicked.connect(self.insert)
        self.completed.clicked.connect(self.mark_completed)
        self.restart.clicked.connect(self.reset_all)
        self.edit.clicked.connect(self.edit_content)
        self.delete_2.clicked.connect(exit)

        # Menu
        self.new_menu.triggered.connect(self.reset_all)

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

        # Enable Completed and Reset
        if self.tasks != 0:
            self.completed.setEnabled(True)
            self.restart.setEnabled(True)     
            self.edit.setEnabled(True)         

        # Clear the text field
        self.input_field.setText("")

        # update LCD
        self.lcd_update()

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

            # update LCD
            self.lcd_update()


        else:
            caution_box = QMessageBox()
            caution_box.setWindowTitle("CAUTION")
            caution_box.setText("No Task Selected")
            caution_box.exec_()

    # Reset function
    def reset_all(self):
        
        reset_box = QMessageBox()
        reset_box.setWindowTitle("New")
        reset_box.setText(f"{self.tasks} Remaining !! Do you wanna still Continue")
        reset_box.addButton(QPushButton("YES"), QMessageBox.YesRole)
        reset_box.addButton(QPushButton("NO"), QMessageBox.NoRole)

        if reset_box.exec_() == 0:
            self.model.clear()
            self.completed_count, self.tasks = 0 , 0
            self.lcd_update()
        
    # Edit function
    def edit_content(self):
        if len(self.listView.selectedIndexes()) != 0:

            selected_index = self.listView.selectedIndexes()[0]
            sel_item = self.model.itemFromIndex(selected_index)

            text, ok = QInputDialog.getText(self, "Edit", "Edit Task", QLineEdit.Normal, sel_item.text())
            if text and ok is not None:
                sel_item.setText(text)



    # Update LCD function
    def lcd_update(self):
        self.lcd_uncompleted.display(self.completed_count)
        self.lcd_tasks.display(self.tasks)



def main():
    app = QApplication([])
    window = MyGUI()
    
    app.exec_()

if __name__ == "__main__":
    main()