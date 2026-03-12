import random

number=(random.randint(1,100))
guess=0
while(guess != number):
 guess=int(input("guess the number "))
 if guess<number:
    print("higher than this")
 elif(guess>number):
   print("lower than this")
 else:
   print("you won!")   
   
