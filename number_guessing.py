
import random

print("================================")
print("     NUMBER GUESSING GAME")
print("================================")

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Guess a number between 1 and 100.")
print(f"You have {max_attempts} attempts.")

while attempts < max_attempts:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess == secret_number:
            score = (max_attempts - attempts + 1) * 10

            print("\nCongratulations! You won!")
            print("Correct number:", secret_number)
            print("Attempts used:", attempts)
            print("Your score:", score)
            break

        elif guess < secret_number:
            print("Too low! Try a higher number.")

        else:
            print("Too high! Try a lower number.")

        print("Attempts remaining:", max_attempts - attempts)

    except ValueError:
        print("Please enter a valid number.")

else:
    print("\nGame Over!")
    print("The correct number was:", secret_number)
    print("Your score: 0")

print("\nThanks for playing!")