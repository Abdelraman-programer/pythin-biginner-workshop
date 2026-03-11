import random

def generate_number( ):
     
     return random.randint(1, 100)  

def get_guess():

    return int(input("Enter your guess (1-100): "))
       
def check_guess(secret, guess):
    if guess < secret:
        return "Too low!"
    elif guess > secret:
        return "Too high!"
    else:
        return "Correct!"

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

main()






















