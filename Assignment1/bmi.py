
print('please enter your weight(kg)')
weight=float(input())
print('please enter your heigh(m)')
heigh=float(input())
BMI=weight/(heigh*heigh)
if (BMI<18.5):
    print('underweight')
elif ((18.5<BMI) and (BMI<24.9)):
    print(' normal')

elif ((25<BMI) and (BMI<29.9)):
     print('overweight')

elif ((30<BMI )and (BMI<34.9)):
    print(' obese')

elif (35<BMI ):
    print('extremely obese')    
    
                
