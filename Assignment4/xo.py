import random
import time


start = time.time()



 
def show_game_board():
     for i in range(3):
        for j in range(3):
         print(game[i][j],end='\t')
        print()
         
def check():
   

    j=0
    for i in range(2):
        if game[i][j]==game[i][j+1]==game[i][j+2]=='x':
            print("Player1 win")
            print("Run Time: " + str( time.time() - start ))
            exit() 

        elif game[i][j]==game[i][j+1]==game[i][j+2]=='o':  
            if a==2:
                print("computer win") 
            else:    
             print("Player2 win")
            print("Run Time: " + str( time.time() - start ))
            
            exit()
    i=0
    for j in range(2):
        if game[i][j]==game[i+1][j]==game[i+2][j]=='x':
               print("Player1 win")
               print("Run Time: " + str( time.time() - start ))
               exit()
               
        elif game[i][j]==game[i+1][j]==game[i+2][j]=='o':
        
        
                if a==2:
                 print("computer win")
                else: 
                 print("Player2 win")
                print("Run Time: " + str( time.time() - start ))
                exit()
                


    if game[0][0]==game[1][1]==game[2][2]=='x':
        
            print("Player1 win")
            print("Run Time: " + str( time.time() - start ))
            exit()
                
            

    elif game[0][0]==game[1][1]==game[2][2]=='o':
            if a==2:
                 print("computer win")
            else:     
             print("Player2 win")
            print("Run Time: " + str( time.time() - start ))
            exit()
         

    elif game[0][2]==game[1][1]==game[2][0]=='x':
        
            print("Player1 win")
            print("Run Time: " + str( time.time() - start ))
            exit()
            

    elif game[0][2]==game[1][1]==game[2][0]=='o':
            if a==2:
                 print("computer win")
            else:
             print("Player2 win")
            print("Run Time: " + str( time.time() - start ))
            exit()

    elif count==9:
        print("equal")
        print("Run Time: " + str( time.time() - start ))
        exit()




   




print("choose")
print("1->Play with computer")
print("2->Play with player ") 
a=int (input())

 


count=0
game=[['-','-','-'],
      ['-','-','-'],
      ['-','-','-']]

show_game_board()



while (True):
    
    #player1
    while True:




        print("Player1")
        
        row = int(input('row:'))
        col =int(input('col: '))

        if 0 <= row <=2 and 0<= col <=2:
         if game[row][col]=='-':
             
             game[row][col]='x'
             count+=1
             break
         else:
             print("this cell is not empty")

        else:
            print("invalid inputs,row and col must be between 0 and 2") 

    show_game_board()
    check()

    #player2

    if a==2:
     while True:
        
        print("Player 2")
        row = int(input('row:'))
        col =int(input('col: '))

        if 0 <= row <=2 and 0<= col <=2:
          if game[row][col]=='-':
             
             game[row][col]='o'
             count+=1
             break
          else:
             print("this cell is not empty")

        else:
            print("invalid inputs,row and col must be between 0 and 2")         

     show_game_board()
     check()
    

    
    #copmuter

    if a==1:
     while True:
        
        print("computer:")
        row = random.randint(0,2)
        col = random.randint(0,2)
        
        if game[row][col]=='-':
             
             game[row][col]='o'
             count+=1
             break
        else:
             print("this cell is not empty")
         

     show_game_board()
     check()

   

