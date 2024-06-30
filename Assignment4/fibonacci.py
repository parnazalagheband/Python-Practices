def Fibonacci(n): 
    if n==0: 
        return 0
    
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
n=int(input("enter n: "))
a=[0]
for i in range(n):
  
 a.append(Fibonacci(i+1))

print(a)