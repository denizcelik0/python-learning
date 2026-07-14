import random
number = random.randint(1, 100)
chc_dif = input("Choose a difficulty level (easy, medium, hard): ").lower()
if chc_dif == "easy":
    attempts = 10
elif chc_dif == "medium":
    attempts = 7
elif chc_dif == "hard":
    attempts = 5
else:
    print("Invalid difficulty level. Please choose easy, medium, or hard.")
    exit()


for attempts in range(attempts, 0, -1):
    user_guess = int(input(f"You have {attempts} attempts left. Guess a number between 1 and 100: "))
    if user_guess < 1 or user_guess > 100:
        print("Invalid guess. Please enter a number between 1 and 100.")
        continue
    if user_guess < number:
         print("Too low! Try again.")
    elif user_guess > number:
        print("Too high! Try again.")
    elif user_guess == number:
        print("Congratulations! You guessed the number!")
        break 
    if attempts == 1:
        print(f"Sorry, you've run out of attempts. The number was {number}.")
