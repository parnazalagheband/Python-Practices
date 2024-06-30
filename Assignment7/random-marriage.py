import random
boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
married=[]
result=[]
c=0
while(True):
   
    while(True):
        t=1   
        g=random.choice(girls)
    
        for x in married:
            if x==g:
                
                t=0     
        if t==1: 
         married.append(g)
         c+=1
         break   

    while(True):
      t=1   
      b=random.choice(boys)
   
      for x in married:
        if x==b:
            
            t=0     
      if t==1: 
       married.append(b)
       break   
      
    result.append((g,b))
    if c==8:
        
        break

print(result)
       