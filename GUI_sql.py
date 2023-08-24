import sys
import PyQt5
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import *
import testingsql
from mysql.connector import connect, Error


class Start(QtWidgets.QMainWindow, testingsql.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = connect(host="127.0.0.1",
                    user="root",
                    password="123q",
                    database='exam',
            )
        self.cursor = self.con.cursor()
        self.pushButton.clicked.connect(self.evt_click_view)
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.evt_click_clear)
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.st = []



    def evt_click_view(self):
        if self.checkBox.isChecked() == True:
            select_query = "SELECT quest_text from T121_quest"
        else:
            number = self.spinBox.value()
            select_query = f"SELECT quest_text from T121_quest where quest_num = {number}"
        self.cursor.execute(select_query)
        for row in self.cursor.fetchall():
            self.st.append(str(row))
        for i in self.st:
            self.model.appendRow(QStandardItem(i))

    def evt_click_clear(self):
        self.st = []
        self.model.clear()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = Start()
    Window.show()
    sys.exit(app.exec())