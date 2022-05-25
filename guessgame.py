import random

print ("NumberGuessingGame")
number=random.randint(1,9)
chances=0
print("Guess a number between 1 and 9 ")
while chances <5 :
    gusses=int(input("Enter your guess"))
    if gusses== number:
        print("Congratulations YOU WIN!!!")
        break
    elif gusses<number : 
        print ("your guess was low")

    else:
        print("your guess was too high!!")
    chances+=1
if not chances <5: 
    print("you lose!! The Answer is ",number)
