

from PyQt5 import QtCore, QtGui, QtWidgets


class WindowAddInvoices(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(358, 311)
        Form.setWindowTitle("")
        self.label_tovar_is_invoices = QtWidgets.QLabel(Form)
        self.label_tovar_is_invoices.setGeometry(QtCore.QRect(50, 20, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_tovar_is_invoices.setFont(font)
        self.label_tovar_is_invoices.setObjectName("label_tovar_is_invoices")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_add_invoices = QtWidgets.QPushButton(Form)
        self.pushButton_add_invoices.setGeometry(QtCore.QRect(50, 240, 80, 26))
        self.pushButton_add_invoices.setObjectName("pushButton_add_invoices")
        self.pushButton_cancel_invoices = QtWidgets.QPushButton(Form)
        self.pushButton_cancel_invoices.setGeometry(QtCore.QRect(200, 240, 80, 26))
        self.pushButton_cancel_invoices.setObjectName("pushButton_cancel_invoices")
        self.lineEdit_invoices = QtWidgets.QLineEdit(Form)
        self.lineEdit_invoices.setGeometry(QtCore.QRect(30, 60, 291, 26))
        self.lineEdit_invoices.setObjectName("lineEdit_invoices")
        self.lineEdit_invoices2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_invoices2.setGeometry(QtCore.QRect(40, 150, 281, 26))
        self.lineEdit_invoices2.setObjectName("lineEdit_invoices2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label_tovar_is_invoices.setText(_translate("Form", "Имя товары в накладных"))
        self.label_2.setText(_translate("Form", "Дата "))
        self.pushButton_add_invoices.setText(_translate("Form", "Добавить "))
        self.pushButton_cancel_invoices.setText(_translate("Form", "Отмена "))
