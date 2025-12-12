import random
playing =True
number=str(random.randint(1,9))
print("I will generate a number from 1 to 9 an dyou have to guess it")
print("The game  ends when you get 1 hero")
while playing:
    guess=input("Give me your guess:")
    if number==guess:
        print("You win the game.THe number was ",number)
        break
    else:
        print("Your guess isn't write.Try again.")