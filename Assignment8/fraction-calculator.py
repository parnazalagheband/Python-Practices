class fraction:
    def __init__(self,s=0,m=None):
        self.s=s
        self.m=m


    def show (self):
        print("answer:",self.s,"/",self.m)

    def mul(self,y):
        result=fraction()
        result.s=self.s * y.s
        result.m=self.m * y.m
        return result   
    
    def sum(self,y):
        result=fraction()
        result.s=self.s * y.m +self.m *y.s
        result.m=self.m *y.m
        return result

    def sub(self,y):
        result=fraction()
        result.s=self.s * y.m - self.m *y.s
        result.m=self.m * y.m
        return result

    def div(self,y):
        result=fraction()
        result.s=self.s *y.m
        result.m=self.m *y.s
        return result   
    
    def simple(self):
        fl=0
        if self.s<0 :
            self.s*=-1
            fl=1
        if self.m<0:
             self.m*=-1
             fl=1
           
        if self.s > self.m: 
         small = self.m
        else: 
         small = self.s 
        for i in range(1, small+1): 
         if((self.s % i == 0) and (self.m % i == 0)): 
            gcd = i  

        result=fraction()
        result.s=int(self.s/gcd)
        result.m=int(self.m/gcd)
        if fl==1:
            print("after simplize:",-1*result.s,"/",result.m)
        else:
            print("after simplize:",result.s,"/",result.m)





aa=int(input(" Enter the numerator of first fraction: "))
while(True):
        bb=int(input(" Enter the denominator of first fraction: "))
        if bb==0:
            print("dominator can't be 0 please try again ")
            
        else:
            break  


cc=int(input(" Enter the numerator of second fraction :"))

while(True):
        dd=int(input(" Enter the denominator of second fraction: "))
        if dd==0:
            print("dominator can't be 0 please try again")
            
        else:
            break  



a=fraction(aa,bb)


b=fraction(cc,dd)


              
while(True):    
    print("choose!")
    print("1->sum")
    print("2->sub")
    print("3->mul")
    print("4->div")
    
    print("5-exit")
    n=int(input())



    if n==1:
        c=a.sum(b)
        c.show()
        c.simple()

    if n==2:
        c=a.sub(b)
        c.show()
        c.simple()
    if n==3:
        c=a.mul(b)
        c.show()
        c.simple()

    if n==4:
        c=a.div(b)
        c.show()
        c.simple()


    if n==5:
        print("goodbye")
        exit()         