import random
from words import words
import string

def get_valid_word(words):
    while True:
        try:
            length = int(input("Please enter the word length between 3 and 14: "))
            break
        except ValueError:
            print("Please enter a valid entry. ")
        
    word = random.choice(words)
    while (len(word) != length):
        while length not in range(3, 15):
            length = int(input("Invalid entry. Please enter the word length between 3 and 14: "))
        word = random.choice(words)
    while "-" in word or " " in word:
        if length not in range(3, 15):
            length = int(input("Invalid entry. Please enter the word length between 3 and 14: "))
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while True:
        try:
            lives = int(input("Please enter the number of lives you want: "))
            break
        except ValueError:
            print("Please enter a valid entry. ")

    while len(word_letters) > 0 and lives > 0:
        print("You have ", lives,"lives left and you have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
                print("The letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that character. Player try again.")
        else:
            print("Invalid character. Please try again.")
    
    if lives == 0:
        print(f"Sorry, you died. The word was {word}.")
    else:
        print(f"Yayy! You gessed the word. The word was {word}.")


hangman()