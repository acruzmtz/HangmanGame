""" Game class with methods to help play Hangman """

# random to select random word
import random

class Game:

    def __init__(self):
        """ open file with words """
        self.words = []
        with open('data.txt', mode='r', encoding='utf-8') as file:
            for word in file:
                self.words.append(word)


    def get_random_word(self):
        """ choose and return a random word """
        words_with_accents = {'á': 'a','é': 'e','í': 'i','ó': 'o','ú': 'u'}
        word = lambda words: random.choice(self.words)
        random_word = word(self.words)

        n = [random_word.replace(letter, words_with_accents[letter]) for letter in random_word if letter in words_with_accents]
        if n: random_word = n[0]
        
        return random_word


    @staticmethod
    def is_correct(user_letter, word):
        """ return indices where user_letter is in word """
        return [index for index, value in enumerate(word) if value == user_letter]
