class fraction:

    def __init__(self,a,b,c,d):
        self.x=a/b
      
        self.y=c/d
       
    def sum(self):
        print("sum of 2 frictions is:",self.x+self.y)
        

    def sub(self):
         print("sub of 2 frictions is:",self.x-self.y)

    def mul(self):
        print("mul of 2 frictions is:",self.x*self.y)

    def div(self):
        print("div of 2 frictions is:",self.x/self.y)

    



a=int(input(" Enter the numerator of first fraction: "))
while(True):
        b=int(input(" Enter the denominator of first fraction: "))
        if b==0:
            print("dominator can't be 0 please try again ")
            
        else:
            break  


c=int(input(" Enter the numerator of second fraction :"))

while(True):
        d=int(input(" Enter the denominator of second fraction: "))
        if d==0:
            print("dominator can't be 0 please try again")
            
        else:
            break  
while(True):    
    print("choose!")
    print("1->sum")
    print("2->sub")
    print("3->mul")
    print("4->div")
    print("5->exit")
    n=int(input())



    f=fraction(a,b,c,d)
    if n==1:
        f.sum()
    if n==2:
        f.sub()
    if n==3:
        f.mul() 
    if n==4:
        f.div()  
    if n==5:
        exit()         
