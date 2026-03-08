import random
numbers = random.randint(1, 100)
guess = 0
gussnum = int(input("Guess a number between 1 and 100: "))
while guess != numbers:
    if gussnum < numbers:
        print("higher! Try again.")
    elif gussnum > numbers:
        print("lower ! Try again.")
    else:
        print("Congratulations! You guessed the number." + " It took you " + str(guess+1) + " guesses.")
        break 
    guess += 1
    gussnum = int(input("Guess a number between 1 and 100: "))