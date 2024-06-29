n=(int(input("how many numbers do you have?")))
a=[]

for  i in range(n):
    print("enter your number")
    a.append(int(input()))
    

b=sorted(a)
if a==b :
    print("sorted")
else :
    print(" not sorted")