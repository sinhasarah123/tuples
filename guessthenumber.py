import random

number= random.randint(1,10)
print("welcome to the game")
print("im thinking of a number between 1 to 10 ")
while True:
    guess=int(input("make a guess"))
    if guess==number:
        print("you guessed it right")
        break
    else:
        if guess<number:
            print("too low")
        else:
            print("too high")
        guess=int(input("guess again"))