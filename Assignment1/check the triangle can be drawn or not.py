print('Enter the length of the first side ')
a=float(input())
print('Enter the length of the second side ')
b=float(input())
print('Enter the length of the third side')
c=float(input())
if a<=(c+b) and b<=(a+c) and c<=(a+b):
    print('The triangle can be drawn')
else:
      print('The triangle can not be drawn')
 