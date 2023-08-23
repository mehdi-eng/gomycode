import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0
    
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    
    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Your guess is too low. Guess again.")
            elif guess > secret_number:
                print("Your guess is too high. Guess again.")
            else:
                print(f"Congratulations! You guessed the number correctly in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
