import random
n=int(input("please enter number of array: " ))
numbers=[]
2
for  i in range(n):
    rand1=random.randint(0,100000)
    if rand1 in numbers:
        print( "your number is Repetitious")
       
    else:
        numbers.append(rand1)

           
print(numbers)