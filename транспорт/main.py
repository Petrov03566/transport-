import sys,psycopg2
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QMainWindow,QApplication,QVBoxLayout, QComboBox,QHeaderView,QMessageBox,QTableView
from PyQt5 import QtCore, QtGui, QtWidgets
from table import Ui_MainWindow 
from Provider import ProviderAdd, ProviderChange, ProviderDelete
from invoices import InvoicesAdd
from delete_Invoice import DeleteInvoice
from goodsinvoice import addGoodsInvoice
from Window2 import addWindow2
from chanceProvader import AddProvaderchance
from changeInvoice import Change2
from invoices import InvoiceChance

class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.db_connection()
        self.setTables('provider')
        self.setTables('invoices')
        self.setTables('goodsinvoice')
        
        self.tableView_provader.hideColumn(0)
        self.tableView_invoices.hideColumn(0)
        self.tableView_invoices.hideColumn(3)
        self.tableView_tovar_invoices.hideColumn(0)
        
        self.pushButton_add_provader.clicked.connect(self.add_provider)
        self.pushButton_change_provider.clicked.connect(self.change_provider)
        self.pushButton_invoice.clicked.connect(self.changeInvoices)
        self.pushButton_add_invoices.clicked.connect(self.add_invoice)
        self.pushButton_add_tovar_invoices.clicked.connect(self.open_goods_invoices)
        self.pb_window.clicked.connect(self.open_window2)
        
        
        self.pushButton_delete_provader.clicked.connect(self.delete_provider)
        self.pushButton_delete_invoices.clicked.connect(self.delete_invoice)
        self.pushButton_delete_tovar_invoices.clicked.connect(self.delete_goods)
        
        self.tableView_provader.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_invoices.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_tovar_invoices.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
    def db_connection(self):
        
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setUserName("postgres")
        db.setPassword("student")
        db.setPort(5432)
        db.setDatabaseName("transport")
        db.setHostName("localhost")
        db.open()
          # LoginMain.auth_login_cl
        self.db2 = psycopg2.connect(dbname= 'transport', user = 'postgres', password = 'student', host = 'localhost', port = 5432)
        self.cursor = self.db2.cursor()
        
    def setTables(self, name):
        model =QSqlTableModel()
        model.setTable(name)
        model.select()
        match(name):
            case 'provider':
                self.tableView_provader.setModel(model)
                model.setHeaderData(1, QtCore.Qt.Horizontal,"название")
                model.setHeaderData(2, QtCore.Qt.Horizontal,"адрес")
            case 'invoices':
                self.tableView_invoices.setModel(model)
                model.setHeaderData(1, QtCore.Qt.Horizontal,"номер накладных")
                model.setHeaderData(2, QtCore.Qt.Horizontal,"данные")
            case 'goodsinvoice':
                self.tableView_tovar_invoices.setModel(model)
                model.setHeaderData(1, QtCore.Qt.Horizontal,"Имя товара")
                model.setHeaderData(2, QtCore.Qt.Horizontal,"цена")
                model.setHeaderData(3, QtCore.Qt.Horizontal,"количества")
                model.setHeaderData(4, QtCore.Qt.Horizontal,"стоимость")
            case 'goods':
                self.table
                
    
    #функции для открытия окон(добавление,изменение,удаление)
    def add_provider(self):
        self.addProvider =ProviderAdd(update_method=self.updateProvider)
        self.addProvider.show()
        
    def change_provider(self):
        self.changeProvider =ProviderChange(self.tableView_provader, self.updateProvider)
        self.changeProvider.show()
        
        
    def delete_provider(self):
        self.deleteProvider = ProviderDelete(self.tableView_provader, self.updateProvider)
        self.deleteProvider.show()
    def cancel_provider(self):
        self.cancelProvider = ProviderAdd(update_method=self.updateProvider)
        self.cancelProvider.show()
        
 # кнопка удаление данных         
    def add_invoice(self):
        self.invoice =InvoicesAdd(self.tableView_invoices, self.updateInvoices)
        self.invoice.show()
        
    def changeInvoices(self):
        self.invoice2 = InvoiceChance()
        self.invoice2.show()
    
    def delete_invoice(self):
        selected_indexes = self.tableView_invoices.selectedIndexes()
        if len(selected_indexes) > 0:
            selected_row = selected_indexes[0].row()
        model = self.tableView_invoices.model()
        model.removeRow(selected_row) 

    def open_goods_invoices(self):
        self.goods =addGoodsInvoice(tableView_goods_invoice=self.tableView_tovar_invoices)
        self.goods.show()
        
    def open_window2(self):
        self.window2 = addWindow2()
        self.window2.setupUi(self.window2)
        self.window2.show() 

    def delete_goods(self):
        selected_row = self.tableView_tovar_invoices.selectedIndexes()[0].row()
        model = self.tableView_tovar_invoices.model()
        model.removeRow(selected_row)
        
    # change 
    def change1(self):
        seleted_indexes = self.tableView_provader.selectedIndexes()
        if seleted_indexes:
            row = seleted_indexes[0].row()
            model = self.tableView_provader.model()
    

            
    def updateProvider(self):
        query =QSqlTableModel()
        query.setTable("provider")
        query.select()
        query.setHeaderData(1, QtCore.Qt.Horizontal,"название")
        query.setHeaderData(2, QtCore.Qt.Horizontal,"адрес")
        self.tableView_provader.setModel(query)
        
    def updateInvoices(self):
        query =QSqlTableModel()
        query.setTable("invoices")
        query.select()
        query.setHeaderData(1, QtCore.Qt.Horizontal,"номер накладной")
        query.setHeaderData(2, QtCore.Qt.Horizontal,"дата")
        self.tableView_invoices.setModel(query) 

app =QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

