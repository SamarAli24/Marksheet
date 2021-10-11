import random

name = input("What is your name? ")

print("Good Luck ", name , "!")
 
words = ['neduet', 'ubit', 'fast','szabist','usman', 'hamdard', 'sirsyed', 'dhasuffa',
         'iqra', 'barrethogdson', 'iba', 'iobm']


turns=15

predict=""

w=random.choice(words)

print("You have",turns,"turns")

while(turns>0):
    
    loose=0
  
    for x in w:
        
        if x in predict:
            
            print(x)
            
        else:
            print("-") 
            loose+=1
            
    if loose== 0:

        print("You Win")

        print("The word is: ", w)          
            
        break
    q=input("Enter a character = ")       
    predict+=q
    turns-= 1
    print("turns left= ",turns)

    if(q not in w):
        print("Wrong")
       
        
    elif(q in w):
        print("Carry on you are reaching !!! ")
        
        

if turns==0:
    print("failed")                        
            
    
      