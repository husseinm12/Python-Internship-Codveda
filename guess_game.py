import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    max_attempts = 3
    attempts = 0
    print ("Welcome to your number guessing game!\n")
    print ("I'm thinking of a number betweem 1 and 100\n")
    print (f"you have {max_attempts} attempts to guess it.\n")

    while attempts<max_attempts:
        try:
            guess = int (input(f"Attempt {attempts+1}:Enter your guess: \n"))
        except ValueError:
            print("please enter a valid number.\n")
            continue
        attempts +=1

        if guess <1 or guess>100:
            print("Your guess must be between 1 and 100.")
        elif guess>secret_number:
            print("Too High!")
        elif guess<secret_number:
            print("Too Low!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break
    else:
        print(f"Sorry, you've used all your attempts, the number is {secret_number}.") 
                     
number_guessing_game()