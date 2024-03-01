from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QTableView
from  Window2 import addWindow2
class GoodAdd(addWindow2):
    def __init__(self):
        super().__init__()
        self.addGoods()
    def addGoods(self): 
        # if self.label.text() and self.label_2.text(): 

            queru_gd =QSqlTableModel(parent=self.tableView_2)
            queru_gd.setTable('goods')
            queru_gd.select()
            self.tableView_2.setModel(queru_gd)