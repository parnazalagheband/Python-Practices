a = int(input("Enter the first number: "))
b = int(input("Enter the seccond number: "))
bmm = 1
if a > b:
    t = b
else:
    t = a
for i in range(t, 1, -1):
    if ((a % i == 0) and (b % i == 0)):
        bmm = i
        break


print("bmm :",bmm)
print("kmm:",int((a*b)/bmm))   
