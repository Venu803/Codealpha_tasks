import random
words = ["python", "data", "chair", "table", "code"]
word = random.choice(words)
guessed_letters = []
attempts = 6
display_word = ["-"] * len(word)
print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time")
while attempts > 0 and "-" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

if "-" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over! The word was:", word)
