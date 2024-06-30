m=int(input("m: "))
n=int(input("n: "))

for i in range(m):
    for j in range(n):
        if (i%2==0  and j%2!=0) or (i%2!=0  and j%2==0):
            print('*',end='\t')
        else:
            print('#',end='\t')    



        
    print()   