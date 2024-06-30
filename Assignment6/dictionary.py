
words_bank=[]
def load_data():
    print('loading...')    
    with open('words_bank.txt','r') as f:
      big_text=f.read()
      words=big_text.split('\n')

      for i in range(0, len(words) ,2):
         my_dict={'english':words[i],'persian':words[i+1]}
         words_bank.append(my_dict)

   
    print('loaded!')    

def translate1(input_text):
  user_words=user_text.split(' ')
  output_text=""
  for user in user_words:
      for word in words_bank:
            if word['english']==user:
                  output_text+=word['persian']+' '
                  break

      else:
            output_text +=user +' '
  return output_text


def translate2(input_text):
      user_words=user_text.split(' ')
      output_text=""
      for user in user_words:
          for word in words_bank:
              if user==word['persian']:
                  output_text+=word['english']+' '
                  break

          else:
            output_text +=user +' '
      return output_text

     
while(True):      
      load_data()
      print("select from menu.")
      print("1->english to persian")
      print("2->persian to english")
      print("3->add a new word")
      print("4->exit")
      choice=int(input())

      if choice==1:
            
       user_text=input('please write your text:')
       output_text=translate1(user_text)
       print(output_text)

      elif choice==2:
              
       user_text=input('please write your text:')
       output_text=translate2(user_text)
       print(output_text)

      elif choice==3:
        n=input("Eneter the word in English:")
        m=input("Enter the translation: ")
        f=open('words_bank.txt','a')
        f.write('\n'+n+'\n'+m)
        f.close()
      elif choice==4:
        exit()  
