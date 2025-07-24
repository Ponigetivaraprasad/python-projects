import random

print("Hello, welcome to the Guess the Number game. Let's get started!")

print("1. difficult level (10 chances)")
print("2. easy level (7 chances)")
while True:
    level = input("Please select a level (1 or 2): ")
    if level == '1':
        chances = 10
        break
    elif level == '2':
        chances = 7
        break
    else:
        print("Invalid input. Please enter 1 or 2.")


    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the higher bound: "))

    print("\n I have selected a number between", low, "and", high, ". You have 7 tries to guess it.")

    num = random.randint(low, high)
    ch = 7
    gc = 0

    while gc < ch:
        gc += 1
        guess = int(input("Enter your guess: "))

        if guess == num:
            print(f"Congratulations! You guessed the number {num} in {gc} tries.")
            break
        elif gc >= ch and guess != num:
            print("Sorry, the number was {num}. you guessed it in {gc} tries")

        elif guess < num:
            print("Your guess is too low. Try again.")
        elif guess > num:
            print("Your guess is too high. Try again.")
    