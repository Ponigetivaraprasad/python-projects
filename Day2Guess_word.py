import random
name = input("Enter your name:")
print("Hi!," + name + " Welcome to the Word Guessing Game.\nYou have 7 chances to guess the word. Let's start!")
words = ["python", "java", "javascript", "ruby", "swift",
        "kotlin", "csharp", "php", "html", "css",
        "typescript", "go", "rust", "perl", "scala"]
word = random.choice(words)
print("Guess the word: ")
guesses = ''
turns = 7
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('-')
            failed += 1
    if failed == 0:
        print("You Won")
        print(f"The word is {word}")
        break
    print()
    guess = input("Guess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong guess")
        print(f"You have {turns} turns left")
        if turns == 0:
            print("You losse")
            print(f"The word was {word}. Better luck next time.")
        print("Try again!")