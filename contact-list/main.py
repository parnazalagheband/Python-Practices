from PySide6.Qt3DCore import*
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader
import sqlite3
class MainWINDOW(QMainWindow):
    def __init__(self):
        super().__init__()
        loader =QUiLoader()
        self.ui=loader.load("design.ui")
        self.ui.show()
        self.id=0
        self.conn=sqlite3.connect("database.db")
        self.my_cursor =self.conn.cursor()
        self.load_data()
        
    
    def load_data(self):
        self.my_cursor.execute("SELECT * FROM persons")
        result = self.my_cursor.fetchall()
        for item in result:
            lable =QLabel()
            try:
             lable.setText(item[1]+ " "+item[2]+": "+str(item[4]))
            except:
              lable.setText(item[1]+": "+str(item[4]))
            self.ui.verticalLayout.addWidget(lable)
            
        print("data loaded successfully!")   
    def add(self):
        name=self.app.lineEdit.text()
        family=self.app.lineEdit_2.text()
        phone_number=self.app.lineEdit_3.text()
        mobile_number=self.app.lineEdit_4.text()
        email=self.app.lineEdit_5.text()
        self.id+=1
    
        self.my_cursor.execute(f"INSERT INTO persons(id, name,family, phone_number, mobile_number, email) VALUES({id}, '{name}','{family}', '{phone_number}', '{mobile_number}','{email}' )")   
        self.conn.commit()
        result2 = self.mycursor.fetchall()
        for item in result2:
            lable2 =QLabel()
            try:
             lable2.setText(item[1]+ " "+item[2]+": "+str(item[4]))
            except:
              lable2.setText(item[1]+": "+str(item[4]))
            self.ui.verticalLayout.addWidget(lable2)
       
app = QApplication()
main_window=MainWINDOW()
app.exec()        





