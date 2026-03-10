import random

# Function to generate a random number
def generate_number( ):
     
     return random.randint(1, 100)  # range can be adjusted


# Function to get the user's guess
def get_guess():

    return int(input("Enter your guess (1-100): "))
       

# Function to check the guess
def check_guess(secret, guess):
    if guess < secret:
        return "Too low!"
    elif guess > secret:
        return "Too high!"
    else:
        return "Correct!"
    
    




# Main function to control program flow
def main():
    input("Welcome to Guess the Number! Press Enter to start...")
    secret_number = generate_number()
    attempts = 0
    result = ""

    print("Welcome to Guess the Number!")

    while result != "Correct!" :
        print("Try to guess the number between 1 and 100.")
        guess = get_guess()
        attempts += 1
        result = check_guess(secret_number, guess)
        print(result)

    print(f"Congratulations! You guessed the number in {attempts} attempts.")
    treyse = input("Do you want to play again? (yes/no): ")
    if treyse.lower() == "yes":
        main()  
    else:
        print("Thanks for playing! Goodbye!")

    

# Call main at the botto
main()






















#import random
#numbers = random.randint(1, 100)
#guess = 0
#gussnum = int(input("Guess a number between 1 and 100: "))
#while guess != numbers:
#    if gussnum < numbers:
#        print("higher! Try again.")
 #   elif gussnum > numbers:
#        print("lower ! Try again.")
 #   else:
 #       print("Congratulations! You guessed the number." + " It took you " + str(guess+1) + " guesses.")
 #       break 
 #   guess += 1
 #   gussnum = int(input("Guess a number between 1 and 100: "))