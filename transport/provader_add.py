# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'provader_add.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5 import QtCore, QtGui, QtWidgets


class WindowAddProvider(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(241, 295)
        self.pushButton_provader = QtWidgets.QPushButton(Form)
        self.pushButton_provader.setGeometry(QtCore.QRect(90, 240, 80, 26))
        self.pushButton_provader.setObjectName("pushButton_provader")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 50, 59, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(68, 130, 61, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_add = QtWidgets.QLineEdit(Form)
        self.lineEdit_add.setGeometry(QtCore.QRect(20, 70, 181, 26))
        self.lineEdit_add.setObjectName("lineEdit_add")
        self.lineEdit_add2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_add2.setGeometry(QtCore.QRect(20, 150, 181, 26))
        self.lineEdit_add2.setObjectName("lineEdit_add2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "добавление поставщика "))
        self.pushButton_provader.setText(_translate("Form", "добавить "))
        self.label.setText(_translate("Form", "Имя"))
        self.label_2.setText(_translate("Form", "Адрес"))

        