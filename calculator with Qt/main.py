
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore  import *
from PySide6.QtUiTools import QUiLoader
import math

class calculator(QMainWindow):
    def __init__(self):
        super().__init__()       
        loader=QUiLoader()
        self.ui =loader.load("design.ui")
        self.ui.show()
        self.ui.one.clicked.connect(self.one)
        self.ui.two.clicked.connect(self.two)
        self.ui.three.clicked.connect(self.three)
        self.ui.four.clicked.connect(self.four)
        self.ui.five.clicked.connect(self.five)
        self.ui.six.clicked.connect(self.six)
        self.ui.seven.clicked.connect(self.seven)
        self.ui.eight.clicked.connect(self.eight)
        self.ui.nine.clicked.connect(self.nine)
        self.ui.zero.clicked.connect(self.zero)
        self.ui.summ.clicked.connect(self.add)
        self.ui.equal.clicked.connect(self.equal)
        self.ui.sub.clicked.connect(self.sub)
        self.ui.div.clicked.connect(self.div)
        self.ui.mul.clicked.connect(self.mul)
        self.ui.remaind.clicked.connect(self.remaind)
        self.ui.sin.clicked.connect(self.sin)
        self.ui.cos.clicked.connect(self.cos)
        self.ui.tan.clicked.connect(self.tan)
        self.ui.cot.clicked.connect(self.cot)
        self.ui.log.clicked.connect(self.log)
        self.ui.ac.clicked.connect(self.ac)
        self.ui.sign.clicked.connect(self.sign)
        self.ui.sqrt.clicked.connect(self.sqrt)
        self.ui.dot.clicked.connect(self.dot)
       
        
        self.num='0'
        self.num1=0
        self.num3=1
        self.count=0
       
     
    def one(self):
       
       self.num=self.ui.tb_1.text()+'1'
       self.ui.tb_1.setText(str(self.num))
    
    def two(self):
        self.num=self.ui.tb_1.text()+'2'
        self.ui.tb_1.setText(str(self.num))
    
    def three(self):
        self.num=self.ui.tb_1.text()+'3'
        self.ui.tb_1.setText(str(self.num))
    
    def four(self):
        self.num=self.ui.tb_1.text()+'4'
        self.ui.tb_1.setText(str(self.num))
    
    def five(self):
        self.num=self.ui.tb_1.text()+'5'
        self.ui.tb_1.setText(str(self.num))
            
    
    def six(self):
        self.num=self.ui.tb_1.text()+'6'
        self.ui.tb_1.setText(str(self.num))
    
    
    def seven(self):
        self.num=self.ui.tb_1.text()+'7'
        self.ui.tb_1.setText(str(self.num))
    
    def eight(self):
        self.num=self.ui.tb_1.text()+'8'
        self.ui.tb_1.setText(str(self.num))
                              
    
    def nine(self):
        self.num=self.ui.tb_1.text()+'9'
        self.ui.tb_1.setText(str(self.num))
    
    
    def zero(self):
       self.num=self.ui.tb_1.text()+'0'
       self.ui.tb_1.setText(str(self.num))
      
        
    def add (self):
        
        
        self.num1+=float(self.num)
        self.ui.tb_1.setText("")
        self.t=1
        
    
    def sub (self):
        
        if self.count == 0:
         self.x=2*float(self.num)
            
        
        self.num1-=float(self.num)
        
        self.ui.tb_1.setText("")   
        self.t=2 
        self.count+=1
        
    def div(self):
       
        self.num3=float(self.num)
            
        self.ui.tb_1.setText("")            
        self.t=3
        
            
    def mul(self):
        
        self.num3*=float(self.num)   
        self.ui.tb_1.setText("")   
        self.t=4
        
    def remaind(self):
        self.num1=float(self.num)  
        self.ui.tb_1.setText("")   
        self.t=5
                            
    def sin(self):
        
       result= math.sin(float(self.num)* math.pi / 180)
       self.ui.tb_1.setText(str(result))
       
    def cos(self):
        
       result= math.cos(float(self.num)* math.pi / 180)
       self.ui.tb_1.setText(str(result))   
    
    def tan(self):
            
       result= math.tan(float(self.num)* math.pi / 180)
       self.ui.tb_1.setText(str(result))   
                                         
    def cot(self):
            
       result= math.tan(float(self.num)* math.pi / 180)
       self.ui.tb_1.setText(str(result))       
                                        
    def log(self):
       result= math.log10(int(self.num))
       self.ui.tb_1.setText(str(result))     
    
    def ac(self):  
        self.ui.tb_1.setText("") 
        
    def sign(self):
         result= int(self.num)*-1
         self.ui.tb_1.setText(str(result))   
    def sqrt(self):
         result= math.sqrt(int(self.num))
         self.ui.tb_1.setText(str(result))    
         
    def dot(self):
        
         self.ui.tb_1.setText(self.ui.tb_1.text() + '.') 
        
        
        
                                                                                                                 
    def equal (self):
        if self.t==1:
            self.num2=float(self.num)
            result=self.num1+self.num2
            
                    
        elif self.t==2:
            self.num2=float(self.num)
            result=self.num1+self.x-self.num2
           
        elif self.t==3:
            self.num2=float(self.num)
            if self.num==0:
                print("devision is impossible")
            result=self.num3/self.num2
        
           
        elif self.t==4:
            self.num2=float(self.num)
            result=self.num3*self.num2
                              
           
        elif self.t==5:
            self.num2=float(self.num)
            result=self.num1%self.num2
                          
  
  
        self.ui.tb_1.setText(str(result))
        
if __name__ == "__main__" :       
    app =QApplication()        
    main_window=calculator()
    app.exec()
