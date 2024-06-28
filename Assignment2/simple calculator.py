import math
while True:
    print("Select the number you want")
    print("sum->1") 
    print("sub->2")
    print("mul->3")
    print("div->4")
    print("sin->5")
    print("cos->6")
    print("tan->7")
    print("cot->8")
    print("log->9")
    print("exit->10")

    number=int(input())

    if(number==1 or number==2 or number==3 or number==4  ):
     print("enter the numbers")   
     a=int(input())
     b=int(input())
     if number==1:
          resault=a+b 
     elif number==2:
           resault=a-b
     elif number==3:
           resault=a*b
     elif number==4:
           if b!=0:
            resault=a/b 
           else:
             resault="you can't divide by zero" 
            



    elif(number==5 or number==6 or number==7 or number==8):
      print("enter the angle")
      c=int(input())
      if number==5:
          resault=math.sin(c* math.pi / 180)
      elif number==6:
          resault=math.cos(c* math.pi / 180)
      elif number==7:
          resault=math.tan(c* math.pi / 180)
      elif number==8:
          resault=1/math.tan(c* math.pi / 180)        

    elif(number==9):
      print("enter the number and it's base for logarithm") 
      d=int(input())
      base=int(input())
      resault=math.log(d,base)

    elif(number==10):
      break 
       
    print(resault)

 
 





     
   
        
        

 


    