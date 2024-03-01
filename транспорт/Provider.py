from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QTableView,QMessageBox
from provader_add import WindowAddProvider
from delete_provader import DeleteProvader

class ProviderAdd(WindowAddProvider):
    def __init__(self,update_method):
        super().__init__()
        self.setupUi(self)
        self.pushButton_provader.clicked.connect(self.add_provider)
        self.pushButton_cl_provader.clicked.connect(self.add_cl_provider)
      
        self.update_method = update_method
        
    def add_provider(self):
        if self.lineEdit_add.text() and self.lineEdit_add2.text(): 
            queru_pr =QSqlQuery()
            queru_pr.exec(f"INSERT INTO public.provider (name, address) VALUES ('{self.lineEdit_add.text()}','{self.lineEdit_add2.text()}')")
            self.update_method()
            self.close()
            
    def add_cl_provider(self):
        self.close()
            
    
class ProviderChange(WindowAddProvider):
    def __init__(self, tableView_provader:QTableView, update):
        super().__init__()
        self.setupUi(self)
        self.methodUpdate = update
        row = tableView_provader.currentIndex().row()
        id = tableView_provader.model().index(row, 0).data()
        OldName = tableView_provader.model().index(row, 1).data()
        OldAddress = tableView_provader.model().index(row, 2).data()
        self.id = id
        self.lineEdit_add.setText(OldName)
        self.lineEdit_add2.setText(OldAddress)
        self.pushButton_provader.clicked.connect(self.change_provider)
        
    def change_provider(self):
        if self.lineEdit_add.text() and self.lineEdit_add2.text(): 
            queru_pr =QSqlQuery()
            SQL = f"UPDATE public.provider SET  name='{self.lineEdit_add.text()}', address='{self.lineEdit_add2.text()}' WHERE id="+str(self.id)
            queru_pr.exec(SQL)
            self.methodUpdate()
            self.close()
            
class ProviderDelete(DeleteProvader):
    def __init__(self, tableView_provader:QTableView, update):
        super().__init__()
        self.setupUi(self)
        self.methodUpdate = update
        row = tableView_provader.currentIndex().row()
        self.id = tableView_provader.model().index(row, 0).data()
        self.pushButton_delete_pd_yes.clicked.connect(self.OKAction)
        self.pushButton_canse_no.clicked.connect(self.CancelAction)
    
    def OKAction(self):
        SQL = f"DELETE FROM public.provider WHERE id='{self.id}'"
        query =QSqlQuery()
        query.exec(SQL)
        self.methodUpdate()
        self.close()
        
    def CancelAction(self):
        self.close()