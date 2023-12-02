from PyQt5.QtWidgets import *
from PyQt5.QtGui  import QStandardItemModel, QStandardItem

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.model = QStandardItemModel()
        self.list_view = QListView()
        self.list_view.setModel(self.model)

        self.setup_data()

        layout = QVBoxLayout(self)
        layout.addWidget(self.list_view)

        clear_button = QPushButton("Clear List")
        clear_button.clicked.connect(self.clear_list)
        layout.addWidget(clear_button)

        self.setLayout(layout)

    def setup_data(self):
        for text in ["Item 1", "Item 2", "Item 3"]:
            item = QStandardItem(text)
            self.model.appendRow(item)

    def clear_list(self):
        self.model.clear()

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()
