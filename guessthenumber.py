#Guess the number game.
import random

name = input("Hello Pal!!  Ebter your name to begin the game : ")

print("Dear "+name+", I was thinking of a number between 1 to 25. Can you guess??")

thenum = random.randint(1,25)

#Starting the guessing loop.

for noofguess in range(1,7):
    i=int(input("Enter your guess : "))

    if i < thenum:
        print("You guessed low...")
    elif i > thenum:
        print("You guessed high...")
    else:
        print("Bingo!! You got it...")
        break

#Final result.
    
if i == thenum:
    print("Well done! See you next time..."+name)
else:
    print("You lost buddy, The correct number is "+str(thenum))
print("You took "+ str(noofguess) + " guesses...")
