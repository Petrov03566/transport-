import sys
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QTableView
from PyQt5 import QtCore, QtGui, QtWidgets
from AddInvoices import WindowAddInvoices
from changeInvoice import Change2

class InvoicesAdd(WindowAddInvoices):
    def __init__(self,tableView_invoice:QTableView,update):
        super().__init__()
        self.setupUi(self)
        self.pushButton_add_invoices.clicked.connect(self.update_line_edit_date)
        
        self.invoice = tableView_invoice
        self.updatem = update
        
    def add_invoices(self, number, date):
        if self.lineEdit_invoices.text(): 
            queru_nk =QSqlQuery()
            queru_nk.exec(f"INSERT INTO public.invoices (number_invoices,date) VALUES ('{number}', '{date}')")
            queru2 =QSqlTableModel()
            queru2.setTable("invoices")
            queru2.select()
            self.invoice.setModel(queru2)
            self.updatem()
            self.close()
        
    def update_line_edit_date(self):
        selected_date = self.calendarWidget.selectedDate().toString('dd.MM.yyyy')
        number = self.lineEdit_invoices.text()
        self.add_invoices(number, date = selected_date)
        
    def cansel_add_invoices(self):
        self.close()
        
class InvoiceChance(Change2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    