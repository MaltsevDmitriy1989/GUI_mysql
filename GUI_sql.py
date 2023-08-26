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
        self.pushButton_2.clicked.connect(self.evt_click_ok)
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.evt_click_clear)
        self.pushButton_5.clicked.connect(self.evt_click_add)
        self.pushButton_6.clicked.connect(self.evt_click_del)
        self.model = QStandardItemModel()
        self.model2 = QStandardItemModel()
        self.listView.setModel(self.model)
        self.listView_2.setModel(self.model2)
        self.st = []
        self.st2 = []
        self.quest_id = 1
        self.answ_id = 1

        # for i in range (1, 8):
        #     self.textEdit_answ_[i].hide()
        self.label_answ_1.hide()
        self.label_answ_2.hide()
        self.label_answ_3.hide()
        self.label_answ_4.hide()
        self.label_answ_5.hide()
        self.label_answ_6.hide()
        self.label_answ_7.hide()
        self.label_answ_8.hide()
        self.spinBox_answ_1.hide()
        self.spinBox_answ_2.hide()
        self.spinBox_answ_3.hide()
        self.spinBox_answ_4.hide()
        self.spinBox_answ_5.hide()
        self.spinBox_answ_6.hide()
        self.spinBox_answ_7.hide()
        self.spinBox_answ_8.hide()
        self.checkBox_answ_1.hide()
        self.checkBox_answ_2.hide()
        self.checkBox_answ_3.hide()
        self.checkBox_answ_4.hide()
        self.checkBox_answ_5.hide()
        self.checkBox_answ_6.hide()
        self.checkBox_answ_7.hide()
        self.checkBox_answ_8.hide()
        self.textEdit_answ_1.hide()
        self.textEdit_answ_2.hide()
        self.textEdit_answ_3.hide()
        self.textEdit_answ_4.hide()
        self.textEdit_answ_5.hide()
        self.textEdit_answ_6.hide()
        self.textEdit_answ_7.hide()
        self.textEdit_answ_8.hide()

    def evt_click_view(self):
        if self.checkBox.isChecked() == True:
            select_query = "SELECT quest_text from T121_quest"
            select_query2 = "SELECT answer_text from T122_answer"
        else:
            number = self.spinBox.value()
            select_query = f"SELECT quest_text from T121_quest where quest_num = {number}"
            select_query2 = f"SELECT answer_text from T122_answer where quest_num = {number}"
        self.cursor.execute(select_query)
        for row in self.cursor.fetchall():
            self.st.append(str(row))
        for i in self.st:
            self.model.appendRow(QStandardItem(i))
        self.cursor.execute(select_query2)
        for row in self.cursor.fetchall():
            self.st2.append(str(row))
        for i in self.st2:
            self.model2.appendRow(QStandardItem(i))

    def evt_click_clear(self):
        self.st = []
        self.model.clear()
        self.model2.clear()


    def evt_click_ok(self):
        select_query = "SELECT quest_num FROM t121_quest ORDER BY quest_num DESC LIMIT 1"
        self.cursor.execute(select_query)
        for row in self.cursor.fetchall():
            self.quest_id = int(row[0]) + 1
        select_query = "SELECT answer_num FROM t122_answer ORDER BY answer_num DESC LIMIT 1"
        self.cursor.execute(select_query)
        for row in self.cursor.fetchall():
            self.spinBox_9.setValue(int(row[0]) + 1)
            self.answ_id = int(row[0]) + 1
        answer_kol = self.spinBox_8.value()
        if answer_kol == 8:
            self.label_answ_1.show()
            self.label_answ_2.show()
            self.label_answ_3.show()
            self.label_answ_4.show()
            self.label_answ_5.show()
            self.label_answ_6.show()
            self.label_answ_7.show()
            self.label_answ_8.show()
            self.spinBox_answ_1.show()
            self.spinBox_answ_2.show()
            self.spinBox_answ_3.show()
            self.spinBox_answ_4.show()
            self.spinBox_answ_5.show()
            self.spinBox_answ_6.show()
            self.spinBox_answ_7.show()
            self.spinBox_answ_8.show()
            self.checkBox_answ_1.show()
            self.checkBox_answ_2.show()
            self.checkBox_answ_3.show()
            self.checkBox_answ_4.show()
            self.checkBox_answ_5.show()
            self.checkBox_answ_6.show()
            self.checkBox_answ_7.show()
            self.checkBox_answ_8.show()
            self.textEdit_answ_1.show()
            self.textEdit_answ_2.show()
            self.textEdit_answ_3.show()
            self.textEdit_answ_4.show()
            self.textEdit_answ_5.show()
            self.textEdit_answ_6.show()
            self.textEdit_answ_7.show()
            self.textEdit_answ_8.show()
        elif answer_kol == 7:
            self.label_answ_1.show()
            self.label_answ_2.show()
            self.label_answ_3.show()
            self.label_answ_4.show()
            self.label_answ_5.show()
            self.label_answ_6.show()
            self.label_answ_7.show()
            self.spinBox_answ_1.show()
            self.spinBox_answ_2.show()
            self.spinBox_answ_3.show()
            self.spinBox_answ_4.show()
            self.spinBox_answ_5.show()
            self.spinBox_answ_6.show()
            self.spinBox_answ_7.show()
            self.checkBox_answ_1.show()
            self.checkBox_answ_2.show()
            self.checkBox_answ_3.show()
            self.checkBox_answ_4.show()
            self.checkBox_answ_5.show()
            self.checkBox_answ_6.show()
            self.checkBox_answ_7.show()
            self.textEdit_answ_1.show()
            self.textEdit_answ_2.show()
            self.textEdit_answ_3.show()
            self.textEdit_answ_4.show()
            self.textEdit_answ_5.show()
            self.textEdit_answ_6.show()
            self.textEdit_answ_7.show()
        elif answer_kol == 6:
            self.label_answ_1.show()
            self.label_answ_2.show()
            self.label_answ_3.show()
            self.label_answ_4.show()
            self.label_answ_5.show()
            self.label_answ_6.show()
            self.spinBox_answ_1.show()
            self.spinBox_answ_2.show()
            self.spinBox_answ_3.show()
            self.spinBox_answ_4.show()
            self.spinBox_answ_5.show()
            self.spinBox_answ_6.show()
            self.checkBox_answ_1.show()
            self.checkBox_answ_2.show()
            self.checkBox_answ_3.show()
            self.checkBox_answ_4.show()
            self.checkBox_answ_5.show()
            self.checkBox_answ_6.show()
            self.textEdit_answ_1.show()
            self.textEdit_answ_2.show()
            self.textEdit_answ_3.show()
            self.textEdit_answ_4.show()
            self.textEdit_answ_5.show()
            self.textEdit_answ_6.show()
        elif answer_kol == 5:
            self.label_answ_1.show()
            self.label_answ_2.show()
            self.label_answ_3.show()
            self.label_answ_4.show()
            self.label_answ_5.show()
            self.spinBox_answ_1.show()
            self.spinBox_answ_2.show()
            self.spinBox_answ_3.show()
            self.spinBox_answ_4.show()
            self.spinBox_answ_5.show()
            self.checkBox_answ_1.show()
            self.checkBox_answ_2.show()
            self.checkBox_answ_3.show()
            self.checkBox_answ_4.show()
            self.checkBox_answ_5.show()
            self.textEdit_answ_1.show()
            self.textEdit_answ_2.show()
            self.textEdit_answ_3.show()
            self.textEdit_answ_4.show()
            self.textEdit_answ_5.show()
        elif answer_kol == 4:
            self.label_answ_1.show()
            self.label_answ_2.show()
            self.label_answ_3.show()
            self.label_answ_4.show()
            self.spinBox_answ_1.show()
            self.spinBox_answ_2.show()
            self.spinBox_answ_3.show()
            self.spinBox_answ_4.show()
            self.checkBox_answ_1.show()
            self.checkBox_answ_2.show()
            self.checkBox_answ_3.show()
            self.checkBox_answ_4.show()
            self.textEdit_answ_1.show()
            self.textEdit_answ_2.show()
            self.textEdit_answ_3.show()
            self.textEdit_answ_4.show()
        elif answer_kol == 3:
            self.label_answ_1.show()
            self.label_answ_2.show()
            self.label_answ_3.show()
            self.spinBox_answ_1.show()
            self.spinBox_answ_2.show()
            self.spinBox_answ_3.show()
            self.checkBox_answ_1.show()
            self.checkBox_answ_2.show()
            self.checkBox_answ_3.show()
            self.textEdit_answ_1.show()
            self.textEdit_answ_2.show()
            self.textEdit_answ_3.show()
        elif answer_kol == 2:
            self.label_answ_1.show()
            self.label_answ_2.show()
            self.spinBox_answ_1.show()
            self.spinBox_answ_2.show()
            self.checkBox_answ_1.show()
            self.checkBox_answ_2.show()
            self.textEdit_answ_1.show()
            self.textEdit_answ_2.show()
        elif answer_kol == 1:
            self.label_answ_1.show()
            self.spinBox_answ_1.show()
            self.checkBox_answ_1.show()
            self.textEdit_answ_1.show()

    def evt_click_add(self):
        quest_num = self.quest_id
        baza_num = self.spinBox_3.value()
        disc_num = self.spinBox_4.value()
        QuestID = self.quest_id
        quest_type = self.spinBox_6.value()
        quest_lev = self.spinBox_7.value()
        answer_kol = self.spinBox_8.value()
        quest_text = self.textEdit.toPlainText()
        sql = ("INSERT INTO T121_quest (quest_num, baza_num, disc_num, QuestID, quest_type, quest_lev, answer_kol, quest_text) " \
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        values = [quest_num, baza_num, disc_num, QuestID, quest_type, quest_lev, answer_kol, quest_text]
        self.cursor.execute(sql, values)
        self.con.commit()
        if answer_kol == 1:
            answer_num = self.answ_id
            AnswerID = 1
            answer_type = self.spinBox_answ_1.value()
            if self.checkBox_answ_1.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_1.toPlainText()
            sql1 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values1 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql1, values1)
            self.con.commit()
        if answer_kol == 2:
            answer_num = self.answ_id
            AnswerID = 1
            answer_type = self.spinBox_answ_1.value()
            if self.checkBox_answ_1.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_1.toPlainText()
            sql1 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values1 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql1, values1)
            self.con.commit()
            answer_num = self.answ_id + 1
            AnswerID = 2
            answer_type = self.spinBox_answ_2.value()
            if self.checkBox_answ_2.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_2.toPlainText()
            sql2 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values2 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql2, values2)
            self.con.commit()
        if answer_kol == 3:
            answer_num = self.answ_id
            AnswerID = 1
            answer_type = self.spinBox_answ_1.value()
            if self.checkBox_answ_1.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_1.toPlainText()
            sql1 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values1 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql1, values1)
            self.con.commit()
            answer_num = self.answ_id + 1
            AnswerID = 2
            answer_type = self.spinBox_answ_2.value()
            if self.checkBox_answ_2.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_2.toPlainText()
            sql2 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values2 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql2, values2)
            self.con.commit()
            answer_num = self.answ_id + 2
            AnswerID = 3
            answer_type = self.spinBox_answ_3.value()
            if self.checkBox_answ_3.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_3.toPlainText()
            sql3 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values3 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql3, values3)
            self.con.commit()
        if answer_kol == 4:
            answer_num = self.answ_id
            AnswerID = 1
            answer_type = self.spinBox_answ_1.value()
            if self.checkBox_answ_1.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_1.toPlainText()
            sql1 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values1 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql1, values1)
            self.con.commit()
            answer_num = self.answ_id + 1
            AnswerID = 2
            answer_type = self.spinBox_answ_2.value()
            if self.checkBox_answ_2.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_2.toPlainText()
            sql2 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values2 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql2, values2)
            self.con.commit()
            answer_num = self.answ_id + 2
            AnswerID = 3
            answer_type = self.spinBox_answ_3.value()
            if self.checkBox_answ_3.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_3.toPlainText()
            sql3 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values3 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql3, values3)
            self.con.commit()
            answer_num = self.answ_id + 3
            AnswerID = 4
            answer_type = self.spinBox_answ_4.value()
            if self.checkBox_answ_4.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_4.toPlainText()
            sql4 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values4 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql4, values4)
            self.con.commit()
        if answer_kol == 5:
            answer_num = self.answ_id
            AnswerID = 1
            answer_type = self.spinBox_answ_1.value()
            if self.checkBox_answ_1.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_1.toPlainText()
            sql1 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values1 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql1, values1)
            self.con.commit()
            answer_num = self.answ_id + 1
            AnswerID = 2
            answer_type = self.spinBox_answ_2.value()
            if self.checkBox_answ_2.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_2.toPlainText()
            sql2 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values2 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql2, values2)
            self.con.commit()
            answer_num = self.answ_id + 2
            AnswerID = 3
            answer_type = self.spinBox_answ_3.value()
            if self.checkBox_answ_3.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_3.toPlainText()
            sql3 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values3 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql3, values3)
            self.con.commit()
            answer_num = self.answ_id + 3
            AnswerID = 4
            answer_type = self.spinBox_answ_4.value()
            if self.checkBox_answ_4.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_4.toPlainText()
            sql4 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values4 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql4, values4)
            self.con.commit()
            answer_num = self.answ_id + 4
            AnswerID = 5
            answer_type = self.spinBox_answ_5.value()
            if self.checkBox_answ_5.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_5.toPlainText()
            sql5 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values5 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql5, values5)
            self.con.commit()
        if answer_kol == 6:
            answer_num = self.answ_id
            AnswerID = 1
            answer_type = self.spinBox_answ_1.value()
            if self.checkBox_answ_1.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_1.toPlainText()
            sql1 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values1 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql1, values1)
            self.con.commit()
            answer_num = self.answ_id + 1
            AnswerID = 2
            answer_type = self.spinBox_answ_2.value()
            if self.checkBox_answ_2.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_2.toPlainText()
            sql2 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values2 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql2, values2)
            self.con.commit()
            answer_num = self.answ_id + 2
            AnswerID = 3
            answer_type = self.spinBox_answ_3.value()
            if self.checkBox_answ_3.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_3.toPlainText()
            sql3 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values3 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql3, values3)
            self.con.commit()
            answer_num = self.answ_id + 3
            AnswerID = 4
            answer_type = self.spinBox_answ_4.value()
            if self.checkBox_answ_4.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_4.toPlainText()
            sql4 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values4 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql4, values4)
            self.con.commit()
            answer_num = self.answ_id + 4
            AnswerID = 5
            answer_type = self.spinBox_answ_5.value()
            if self.checkBox_answ_5.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_5.toPlainText()
            sql5 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values5 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql5, values5)
            self.con.commit()
            answer_num = self.answ_id + 5
            AnswerID = 6
            answer_type = self.spinBox_answ_6.value()
            if self.checkBox_answ_6.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_6.toPlainText()
            sql6 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values6 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql6, values6)
            self.con.commit()
        if answer_kol == 7:
            answer_num = self.answ_id
            AnswerID = 1
            answer_type = self.spinBox_answ_1.value()
            if self.checkBox_answ_1.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_1.toPlainText()
            sql1 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values1 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql1, values1)
            self.con.commit()
            answer_num = self.answ_id + 1
            AnswerID = 2
            answer_type = self.spinBox_answ_2.value()
            if self.checkBox_answ_2.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_2.toPlainText()
            sql2 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values2 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql2, values2)
            self.con.commit()
            answer_num = self.answ_id + 2
            AnswerID = 3
            answer_type = self.spinBox_answ_3.value()
            if self.checkBox_answ_3.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_3.toPlainText()
            sql3 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values3 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql3, values3)
            self.con.commit()
            answer_num = self.answ_id + 3
            AnswerID = 4
            answer_type = self.spinBox_answ_4.value()
            if self.checkBox_answ_4.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_4.toPlainText()
            sql4 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values4 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql4, values4)
            self.con.commit()
            answer_num = self.answ_id + 4
            AnswerID = 5
            answer_type = self.spinBox_answ_5.value()
            if self.checkBox_answ_5.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_5.toPlainText()
            sql5 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values5 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql5, values5)
            self.con.commit()
            answer_num = self.answ_id + 5
            AnswerID = 6
            answer_type = self.spinBox_answ_6.value()
            if self.checkBox_answ_6.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_6.toPlainText()
            sql6 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values6 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql6, values6)
            self.con.commit()
            answer_num = self.answ_id + 6
            AnswerID = 7
            answer_type = self.spinBox_answ_7.value()
            if self.checkBox_answ_7.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_7.toPlainText()
            sql7 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values7 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql7, values7)
            self.con.commit()
        if answer_kol == 8:
            answer_num = self.answ_id
            AnswerID = 1
            answer_type = self.spinBox_answ_1.value()
            if self.checkBox_answ_1.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_1.toPlainText()
            sql1 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values1 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql1, values1)
            self.con.commit()
            answer_num = self.answ_id + 1
            AnswerID = 2
            answer_type = self.spinBox_answ_2.value()
            if self.checkBox_answ_2.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_2.toPlainText()
            sql2 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values2 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql2, values2)
            self.con.commit()
            answer_num = self.answ_id + 2
            AnswerID = 3
            answer_type = self.spinBox_answ_3.value()
            if self.checkBox_answ_3.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_3.toPlainText()
            sql3 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values3 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql3, values3)
            self.con.commit()
            answer_num = self.answ_id + 3
            AnswerID = 4
            answer_type = self.spinBox_answ_4.value()
            if self.checkBox_answ_4.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_4.toPlainText()
            sql4 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values4 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql4, values4)
            self.con.commit()
            answer_num = self.answ_id + 4
            AnswerID = 5
            answer_type = self.spinBox_answ_5.value()
            if self.checkBox_answ_5.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_5.toPlainText()
            sql5 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values5 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql5, values5)
            self.con.commit()
            answer_num = self.answ_id + 5
            AnswerID = 6
            answer_type = self.spinBox_answ_6.value()
            if self.checkBox_answ_6.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_6.toPlainText()
            sql6 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values6 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql6, values6)
            self.con.commit()
            answer_num = self.answ_id + 6
            AnswerID = 7
            answer_type = self.spinBox_answ_7.value()
            if self.checkBox_answ_7.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_7.toPlainText()
            sql7 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values7 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql7, values7)
            self.con.commit()
            answer_num = self.answ_id + 7
            AnswerID = 8
            answer_type = self.spinBox_answ_8.value()
            if self.checkBox_answ_8.isChecked() == True:
                ok = 1
            else:
                ok = 0
            answer_text = self.textEdit_answ_8.toPlainText()
            sql8 = (
                "INSERT INTO T122_answer (answer_num, quest_num, AnswerID, answer_type, ok, answer_text) " \
                "VALUES (%s, %s, %s, %s, %s, %s)")
            values8 = [answer_num, quest_num, AnswerID, answer_type, ok, answer_text]
            self.cursor.execute(sql8, values8)
            self.con.commit()
        # answer_num, quest_num, AnswerID, answer_type, ok, answer_text, ans

    def evt_click_del(self):
        number = self.spinBox.value()
        select_query = f"DELETE FROM t121_quest WHERE quest_num = {number}"
        self.cursor.execute(select_query)
        self.con.commit()
        select_query2 = f"DELETE FROM t122_answer WHERE quest_num = {number}"
        self.cursor.execute(select_query2)
        self.con.commit()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = Start()
    Window.show()
    sys.exit(app.exec())