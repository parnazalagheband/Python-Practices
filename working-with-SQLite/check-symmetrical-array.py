array=[]
t=0 
n=int(input("enter the number of array:"))
for i in range(n):
    a=int(input("enter the array:"))
    array.append(a)
l=len(array) 

for i in  range(l):
    if array[i]==array[l-i-1]:
        t=0
    
    else:
        t=1
        break
        

if t==0:
    print("array is Symmetrical")

else:
    print("array is not Symmetrical")    