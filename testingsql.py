# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testingsql.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1301, 938)
        self.h1_titul = QtWidgets.QLabel(Dialog)
        self.h1_titul.setGeometry(QtCore.QRect(50, 40, 991, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.h1_titul.setFont(font)
        self.h1_titul.setTextFormat(QtCore.Qt.AutoText)
        self.h1_titul.setAlignment(QtCore.Qt.AlignCenter)
        self.h1_titul.setObjectName("h1_titul")
        self.h2_quest = QtWidgets.QLabel(Dialog)
        self.h2_quest.setGeometry(QtCore.QRect(30, 120, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.h2_quest.setFont(font)
        self.h2_quest.setAlignment(QtCore.Qt.AlignCenter)
        self.h2_quest.setObjectName("h2_quest")
        self.h2_answer = QtWidgets.QLabel(Dialog)
        self.h2_answer.setGeometry(QtCore.QRect(560, 120, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.h2_answer.setFont(font)
        self.h2_answer.setAlignment(QtCore.Qt.AlignCenter)
        self.h2_answer.setObjectName("h2_answer")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 480, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(151, 480, 71, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(9999)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 480, 91, 21))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(290, 480, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 480, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 520, 501, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(180, 580, 71, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(9999)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 580, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(29, 610, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(180, 610, 71, 22))
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(9999)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_6 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(420, 580, 71, 22))
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setMaximum(10)
        self.spinBox_6.setObjectName("spinBox_6")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(270, 580, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(270, 610, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.spinBox_7 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_7.setGeometry(QtCore.QRect(420, 610, 71, 22))
        self.spinBox_7.setMinimum(1)
        self.spinBox_7.setMaximum(3)
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_8 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_8.setGeometry(QtCore.QRect(180, 640, 71, 22))
        self.spinBox_8.setMinimum(1)
        self.spinBox_8.setMaximum(8)
        self.spinBox_8.setObjectName("spinBox_8")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(30, 640, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(30, 670, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 700, 491, 171))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 910, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(560, 500, 501, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.spinBox_9 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_9.setGeometry(QtCore.QRect(760, 530, 71, 22))
        self.spinBox_9.setReadOnly(True)
        self.spinBox_9.setMinimum(1)
        self.spinBox_9.setMaximum(9999)
        self.spinBox_9.setObjectName("spinBox_9")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(610, 530, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_answ_1 = QtWidgets.QLabel(Dialog)
        self.label_answ_1.setGeometry(QtCore.QRect(570, 570, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_answ_1.setFont(font)
        self.label_answ_1.setObjectName("label_answ_1")
        self.spinBox_answ_1 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_answ_1.setGeometry(QtCore.QRect(660, 570, 41, 22))
        self.spinBox_answ_1.setMinimum(1)
        self.spinBox_answ_1.setMaximum(99)
        self.spinBox_answ_1.setObjectName("spinBox_answ_1")
        self.checkBox_answ_1 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_answ_1.setGeometry(QtCore.QRect(720, 570, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_answ_1.setFont(font)
        self.checkBox_answ_1.setObjectName("checkBox_answ_1")
        self.textEdit_answ_1 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_answ_1.setGeometry(QtCore.QRect(840, 570, 271, 31))
        self.textEdit_answ_1.setObjectName("textEdit_answ_1")
        self.label_answ_2 = QtWidgets.QLabel(Dialog)
        self.label_answ_2.setGeometry(QtCore.QRect(570, 610, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_answ_2.setFont(font)
        self.label_answ_2.setObjectName("label_answ_2")
        self.spinBox_answ_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_answ_2.setGeometry(QtCore.QRect(660, 610, 41, 22))
        self.spinBox_answ_2.setMinimum(1)
        self.spinBox_answ_2.setMaximum(99)
        self.spinBox_answ_2.setObjectName("spinBox_answ_2")
        self.checkBox_answ_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_answ_2.setGeometry(QtCore.QRect(720, 610, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_answ_2.setFont(font)
        self.checkBox_answ_2.setObjectName("checkBox_answ_2")
        self.textEdit_answ_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_answ_2.setGeometry(QtCore.QRect(840, 610, 271, 31))
        self.textEdit_answ_2.setObjectName("textEdit_answ_2")
        self.label_answ_3 = QtWidgets.QLabel(Dialog)
        self.label_answ_3.setGeometry(QtCore.QRect(570, 650, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_answ_3.setFont(font)
        self.label_answ_3.setObjectName("label_answ_3")
        self.spinBox_answ_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_answ_3.setGeometry(QtCore.QRect(660, 650, 41, 22))
        self.spinBox_answ_3.setMinimum(1)
        self.spinBox_answ_3.setMaximum(99)
        self.spinBox_answ_3.setObjectName("spinBox_answ_3")
        self.checkBox_answ_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_answ_3.setGeometry(QtCore.QRect(720, 650, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_answ_3.setFont(font)
        self.checkBox_answ_3.setObjectName("checkBox_answ_3")
        self.textEdit_answ_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_answ_3.setGeometry(QtCore.QRect(840, 650, 271, 31))
        self.textEdit_answ_3.setObjectName("textEdit_answ_3")
        self.label_answ_4 = QtWidgets.QLabel(Dialog)
        self.label_answ_4.setGeometry(QtCore.QRect(570, 690, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_answ_4.setFont(font)
        self.label_answ_4.setObjectName("label_answ_4")
        self.spinBox_answ_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_answ_4.setGeometry(QtCore.QRect(660, 690, 41, 22))
        self.spinBox_answ_4.setMinimum(1)
        self.spinBox_answ_4.setMaximum(99)
        self.spinBox_answ_4.setObjectName("spinBox_answ_4")
        self.checkBox_answ_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_answ_4.setGeometry(QtCore.QRect(720, 690, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_answ_4.setFont(font)
        self.checkBox_answ_4.setObjectName("checkBox_answ_4")
        self.textEdit_answ_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_answ_4.setGeometry(QtCore.QRect(840, 690, 271, 31))
        self.textEdit_answ_4.setObjectName("textEdit_answ_4")
        self.label_answ_5 = QtWidgets.QLabel(Dialog)
        self.label_answ_5.setGeometry(QtCore.QRect(570, 730, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_answ_5.setFont(font)
        self.label_answ_5.setObjectName("label_answ_5")
        self.spinBox_answ_5 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_answ_5.setGeometry(QtCore.QRect(660, 730, 41, 22))
        self.spinBox_answ_5.setMinimum(1)
        self.spinBox_answ_5.setMaximum(99)
        self.spinBox_answ_5.setObjectName("spinBox_answ_5")
        self.checkBox_answ_5 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_answ_5.setGeometry(QtCore.QRect(720, 730, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_answ_5.setFont(font)
        self.checkBox_answ_5.setObjectName("checkBox_answ_5")
        self.textEdit_answ_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_answ_5.setGeometry(QtCore.QRect(840, 730, 271, 31))
        self.textEdit_answ_5.setObjectName("textEdit_answ_5")
        self.label_answ_6 = QtWidgets.QLabel(Dialog)
        self.label_answ_6.setGeometry(QtCore.QRect(570, 770, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_answ_6.setFont(font)
        self.label_answ_6.setObjectName("label_answ_6")
        self.spinBox_answ_6 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_answ_6.setGeometry(QtCore.QRect(660, 770, 41, 22))
        self.spinBox_answ_6.setMinimum(1)
        self.spinBox_answ_6.setMaximum(99)
        self.spinBox_answ_6.setObjectName("spinBox_answ_6")
        self.checkBox_answ_6 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_answ_6.setGeometry(QtCore.QRect(720, 770, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_answ_6.setFont(font)
        self.checkBox_answ_6.setObjectName("checkBox_answ_6")
        self.textEdit_answ_6 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_answ_6.setGeometry(QtCore.QRect(840, 770, 271, 31))
        self.textEdit_answ_6.setObjectName("textEdit_answ_6")
        self.label_answ_7 = QtWidgets.QLabel(Dialog)
        self.label_answ_7.setGeometry(QtCore.QRect(570, 810, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_answ_7.setFont(font)
        self.label_answ_7.setObjectName("label_answ_7")
        self.spinBox_answ_7 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_answ_7.setGeometry(QtCore.QRect(660, 810, 41, 22))
        self.spinBox_answ_7.setMinimum(1)
        self.spinBox_answ_7.setMaximum(99)
        self.spinBox_answ_7.setObjectName("spinBox_answ_7")
        self.checkBox_answ_7 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_answ_7.setGeometry(QtCore.QRect(720, 810, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_answ_7.setFont(font)
        self.checkBox_answ_7.setObjectName("checkBox_answ_7")
        self.textEdit_answ_7 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_answ_7.setGeometry(QtCore.QRect(840, 810, 271, 31))
        self.textEdit_answ_7.setObjectName("textEdit_answ_7")
        self.label_answ_8 = QtWidgets.QLabel(Dialog)
        self.label_answ_8.setGeometry(QtCore.QRect(570, 850, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_answ_8.setFont(font)
        self.label_answ_8.setObjectName("label_answ_8")
        self.spinBox_answ_8 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_answ_8.setGeometry(QtCore.QRect(660, 850, 41, 22))
        self.spinBox_answ_8.setMinimum(1)
        self.spinBox_answ_8.setMaximum(99)
        self.spinBox_answ_8.setObjectName("spinBox_answ_8")
        self.checkBox_answ_8 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_answ_8.setGeometry(QtCore.QRect(720, 850, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_answ_8.setFont(font)
        self.checkBox_answ_8.setObjectName("checkBox_answ_8")
        self.textEdit_answ_8 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_answ_8.setGeometry(QtCore.QRect(840, 850, 271, 31))
        self.textEdit_answ_8.setObjectName("textEdit_answ_8")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(1110, 910, 181, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(20, 160, 531, 301))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(Dialog)
        self.listView_2.setGeometry(QtCore.QRect(570, 160, 531, 301))
        self.listView_2.setObjectName("listView_2")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 480, 91, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(1000, 910, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(610, 480, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.h1_titul.setText(_translate("Dialog", "Программа для работы с базой тестовых заданий"))
        self.h2_quest.setText(_translate("Dialog", "Вопросы"))
        self.h2_answer.setText(_translate("Dialog", "Ответы"))
        self.label.setText(_translate("Dialog", "Номер вопроса"))
        self.pushButton.setText(_translate("Dialog", "Отобразить"))
        self.checkBox.setText(_translate("Dialog", "Выбрать все"))
        self.label_2.setText(_translate("Dialog", "или"))
        self.label_3.setText(_translate("Dialog", "Добавить вопрос"))
        self.label_5.setText(_translate("Dialog", "Номер базы"))
        self.label_6.setText(_translate("Dialog", "Номер дисциплины"))
        self.label_8.setText(_translate("Dialog", "Тип вопроса"))
        self.label_9.setText(_translate("Dialog", "Уровень вопроса"))
        self.label_10.setText(_translate("Dialog", "Количество ответов"))
        self.label_11.setText(_translate("Dialog", "Текст вопроса"))
        self.pushButton_2.setText(_translate("Dialog", "Ок"))
        self.label_12.setText(_translate("Dialog", "Добавить ответ"))
        self.label_13.setText(_translate("Dialog", "Номер ответа"))
        self.label_answ_1.setText(_translate("Dialog", "Тип ответа"))
        self.checkBox_answ_1.setText(_translate("Dialog", "Правильный"))
        self.label_answ_2.setText(_translate("Dialog", "Тип ответа"))
        self.checkBox_answ_2.setText(_translate("Dialog", "Правильный"))
        self.label_answ_3.setText(_translate("Dialog", "Тип ответа"))
        self.checkBox_answ_3.setText(_translate("Dialog", "Правильный"))
        self.label_answ_4.setText(_translate("Dialog", "Тип ответа"))
        self.checkBox_answ_4.setText(_translate("Dialog", "Правильный"))
        self.label_answ_5.setText(_translate("Dialog", "Тип ответа"))
        self.checkBox_answ_5.setText(_translate("Dialog", "Правильный"))
        self.label_answ_6.setText(_translate("Dialog", "Тип ответа"))
        self.checkBox_answ_6.setText(_translate("Dialog", "Правильный"))
        self.label_answ_7.setText(_translate("Dialog", "Тип ответа"))
        self.checkBox_answ_7.setText(_translate("Dialog", "Правильный"))
        self.label_answ_8.setText(_translate("Dialog", "Тип ответа"))
        self.checkBox_answ_8.setText(_translate("Dialog", "Правильный"))
        self.pushButton_3.setText(_translate("Dialog", "Выход"))
        self.pushButton_4.setText(_translate("Dialog", "Очистить"))
        self.pushButton_5.setText(_translate("Dialog", "Ок"))
        self.pushButton_6.setText(_translate("Dialog", "Удалить"))
