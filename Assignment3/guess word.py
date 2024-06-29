import random
words_bank=['tree','python','linux','mac','windows','java','oslab','book','pen']
word=random.choice(words_bank)
joon=7


user_true_chars=[]
while(True):
    win=1
    for char in word:
        
        if char in user_true_chars:
            print(char,end='')
            
        else:
            print('-',end='')
            win=0
            

    if (win==1):
            print(" \n you win")
              

    user_char=input("\n please enter character: ")
    if user_char in word:
        user_true_chars.append(user_char)
        print('✅')
        
       
    else:
        print('❌')
        joon-=1
        
        

    if(joon==0):
        print("Game Over")
        break
