class mokhtalet:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b

    def show(self):
        print(self.a ,'+',self.b,'i')

    def sum(self,other):
        result=mokhtalet()
        result.a=self.a+other.a
        result.b=self.b+other.b
        return result

    def sub(self,other):
        result=mokhtalet()
        result.a=self.a-other.a
        result.b=self.b-other.b
        return result

    def mul(self,other):
        result=mokhtalet()
        result.a=self.a * other.a -self.b*other.b
        result.b=self.a*other.b +self.b*other.a
        return result    
        
text1=[]
text2=[]
a=input("enter the first number in this format-> a+bi : ")
a1=int(a[0])
a2=int(a[2])

b=input("enter the second number in this format-> a+bi : ")

b1=int(b[0])
b2=int(b[2])
    


while(True):    
        print("choose from menu:")
        print("1->sum ")
        print("2->sub")
        print("3->mul")
        print("4->exit")
        n=int(input())

        if n==1:
         m1=mokhtalet(int(a1),int(a2))
         m2=mokhtalet(int(b1),int(b2))
         m3=m1.sum(m2)
         m3.show()

        if n==2:
         m1=mokhtalet(int(a1),int(a2))
         m2=mokhtalet(int(b1),int(b2))
         m3=m1.sub(m2)
         m3.show()

        if n==3:
         m1=mokhtalet(int(a1),int(a2))
         m2=mokhtalet(int(b1),int(b2))
         m3=m1.mul(m2)
         m3.show()

        if n==4:
            print("goodbye")
            exit()








