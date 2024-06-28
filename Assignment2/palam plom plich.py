import random
counter=5
while(counter):
    print("choose!")
    print("✋->1")
    print("🤚->2")
    user=input()
    comp1=random.randint(1,2)
    comp2=random.randint(1,2)
    counter=-1
    if(comp1==comp2):
        if (user!=comp1):
            print("you lose")
            
        
        else:
            print("no one lose")
            
        
    else:
        if(user==comp1):
            print("compurer2 lose")
            
        
        else:    
            print("computer1 lose")
            
        
            




  
        




