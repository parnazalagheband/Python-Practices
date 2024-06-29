numb=input("enter your number: ")
l=len(numb)
s=0

number=int(numb)
a=[]

for i in range(l):
    a.append (number % 10)
    number =int( number / 10)
    s+=a[i]**l
   


if(s==int(numb)):
     print("yes")
else:
    print("no")