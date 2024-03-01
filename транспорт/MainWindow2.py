from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QTableView
from table import Ui_MainWindow
from Window2 import addWindow2

class GoodAdd(addWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def add_window2(self):
            queru_pr =QSqlQuery()
            queru_pr.exec(f"INSERT INTO public.goods (id,id_invoice,id_goods,quantity) VALUES ('{self.label.text()}','{self.label_2.text()}')")
            queru =QSqlTableModel()
            queru.setTable("goods")
            queru.select()
            self.tableView.setModel(queru)