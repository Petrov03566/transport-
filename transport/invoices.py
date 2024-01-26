import sys
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from AddInvoices import WindowAddInvoices

class InvoicesAdd(WindowAddInvoices):
    def __init__(self,tableView_invoice):
        super().__init__()
        self.setupUi(self)
        self.pushButton_add_invoices.clicked.connect(self.add_invoices)
        self.invoice = tableView_invoice
    
    
    def add_invoices(self):
        if self.lineEdit_invoices.text() and self.lineEdit_invoices2.text(): 
            queru_nk =QSqlQuery()
            queru_nk.exec(f"INSERT INTO public.invoices (number_invoices,date) VALUES ('{self.lineEdit_invoices.text()}',{self.lineEdit_invoices2.text()})")
            queru2 =QSqlTableModel()
            queru2.setTable("invoices")
            queru2.select()
            self.invoice.setModel(queru2)
            
        
        