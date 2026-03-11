
print("lets starrt ")
game=input("do you want to play the quiz competion? ")
if game.lower() == "yes":
    print("lets start")
else:
    quit() 
score=0    
answer=input("what is the full form of cpu? ")
if answer.lower() == "central processing unit" : 
    print('correct')
    score+=1
else:
    print('incorrect')

answer=input("what is the full form of gpu? ")
if answer.lower() == "graphical processing unit" : 
    print('correct')
    score+=1
else:
    print('incorrect')

answer=input("what is the full form of RAM? ")
if answer.lower() == "random access memory" : 
    print('correct')
    score+=1
else:
    print('incorrect')  

print(f"you got {score} number")       

