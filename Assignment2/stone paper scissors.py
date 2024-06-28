import random
counter=5
cwin=0
uwin=0

while(counter):
  computer=random.randint(1,3)
  print("choose!")
  print("1-> stone")
  print("2->paper")
  print("3-> scissors")
  user=int(input())
  counter-=1
  print("computer choise is",computer)
  if(computer==1 and user==1)or (computer==2 and user==2) or (computer==3 and user==3):
    print("equal")    
  if (computer==1 and user==2):
   uwin+=1
   print("you win in this level.")  

   
  elif(computer==1 and user==3):
   cwin+=1
   print("computer win in this level.")

  elif(computer==2 and user==1): 
   cwin+=1
   print("computer win in this level.")

  elif(computer==2 and user==3):
   uwin+=1
   print("you win in this level.")  

  elif(computer==3 and user==1): 
   uwin+=1
   print("you win in this level.")  

  elif(computer==3 and user==2):
   cwin+=1
   print("computer win in this level.")


if(cwin>uwin):
    print("you lose.")
else:
     print("congratulation!!you win.")
