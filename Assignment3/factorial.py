
number=int(input("enter your number: "))
fact = 1
r=1
for i in range(1,number+1):
    fact = fact * i
    if fact==number:
        print("yes")
        r=0

if r==1:
    print("no")