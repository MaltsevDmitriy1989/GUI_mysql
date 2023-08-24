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
        self.pushButton_2.clicked.connect(self.evt_click_add)
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.evt_click_clear)
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.st = []
        select_query = "SELECT quest_num FROM t121_quest ORDER BY quest_num DESC LIMIT 1"
        self.cursor.execute(select_query)
        for row in self.cursor.fetchall():
            self.spinBox_2.setValue(int(row[0])+1)
            self.spinBox_5.setValue(int(row[0])+1)
        select_query = "SELECT answer_num FROM t122_answer ORDER BY answer_num DESC LIMIT 1"
        self.cursor.execute(select_query)
        for row in self.cursor.fetchall():
            self.spinBox_9.setValue(int(row[0]) + 1)

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


    def evt_click_add(self):
        quest_num = self.spinBox_2.value()
        baza_num = self.spinBox_3.value()
        disc_num = self.spinBox_4.value()
        QuestID = self.spinBox_5.value()
        quest_type = self.spinBox_6.value()
        quest_lev = self.spinBox_7.value()
        answer_kol = self.spinBox_8.value()
        quest_text = self.textEdit.toPlainText()
        sql = ("INSERT INTO T121_quest (quest_num, baza_num, disc_num, QuestID, quest_type, quest_lev, answer_kol, quest_text) " \
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        values = [quest_num, baza_num, disc_num, QuestID, quest_type, quest_lev, answer_kol, quest_text]
        self.cursor.execute(sql, values)
        self.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = Start()
    Window.show()
    sys.exit(app.exec())