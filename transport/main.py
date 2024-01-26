import sys
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QMainWindow,QApplication
from table import Ui_MainWindow 
from Provider import ProviderAdd
from invoices import InvoicesAdd
from PyQt5 import QtCore, QtGui, QtWidgets
class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.tableView_provader.setModel()
        
        self.db_connection()
        self.db_table1()
        self.db_table2()
        self.db_table3()
        
        
        self.pushButton_add_provader.clicked.connect(self.open_provider)   
        self.pushButton_add_invoices.clicked.connect(self.open_invoice)
        
    def db_connection(self):
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setUserName("postgres")
        db.setPassword("Doctor")
        db.setPort(5432)
        db.setDatabaseName("transport")
        db.setHostName("localhost")
        db.open()
        


    def db_table1(self):
        stm =QSqlTableModel()
        stm.setTable('provider')
        stm.select()
        self.tableView_provader.setModel(stm)
        
    def db_table2(self):
        stm2 =QSqlTableModel()
        stm2.setTable('invoices')
        stm2.select()
        self.tableView_invoices.setModel(stm2)
        
    def db_table3(self):
        stm3 =QSqlTableModel()
        stm3.setTable('goods_invoices')
        stm3.select()
        self.tableView_tovar_invoices.setModel(stm3)
        
    # def add_provider(self):
    #     queru_pr =QSqlQuery()
    #     queru_pr.exec(f"INSERT INTO public.provider (name, address) VALUES ('{self.lineEdit_add.text()}','{self.lineEdit_add2.text()}')")
    #     queru =QSqlTableModel()
    #     queru.setTable("provider")
    #     queru.select()
    #     self.tableView_provader.setModel(queru)
    
    
    # открыть окно поставщика
    def open_provider(self):
        self.provider =ProviderAdd(tableView_provader=self.tableView_provader)
        self.provider.show()
        
    def open_invoice(self):
        self.invoice =InvoicesAdd(tableView_invoice=self.tableView_invoices)
        self.invoice.show()
    
    def delete_provider_click(self):
        model =QSqlTableModel()
        model.setTable('provider')
        model.select()
        selecttedIndex =self.tableView_provader.selectedIndexes()
        if selecttedIndex:
            row =selecttedIndex[0].row()
            model.removeRow(row)
            model.submitAll()
        self.tableView_provader.setModel(model)
        model.setHeaderData(1, QtCore.Qt.Horizontal,"Поставшик" )
        model.setHeaderData(2, QtCore.Qt.Horizontal,"адрес" )
    
        

        

        
    
        
app =QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
