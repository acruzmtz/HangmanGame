""" Final Challenge: Hangman Game """

# Game class
from game import Game
import os

def main():
    game = Game()
    word = game.get_random_word()
    length = len(word) - 1
    found = False
    hidden_word = ['_'] * length
    tries = 0

    print("Welcome to Hangman Game")

    while not found:
        print(hidden_word)

        if tries >= 7:
            print("YOU LOSE!!!")
            print(f'The word was: {word}')
            print(f'intentos: {tries}')
            break

        user_letter = input("Enter a letter: ")
        if len(user_letter) != 1:
            os.system('clear')
            continue

        result = Game.is_correct(user_letter, word)

        if not result:
            os.system('clear')
            tries += 1
            print(f'intentos: {tries}')
            continue
        else:
            for index in result:
                hidden_word[index] = user_letter

        try:
            hidden_word.index('_')
            os.system('clear')
        except ValueError:
            print("YOU WIN!!!")
            print(hidden_word)
            print(f'The word is: {word}, adivinaste en {tries} intentos')
            found = True

        print(f'intentos: {tries}')


if __name__ == '__main__':
    main()
