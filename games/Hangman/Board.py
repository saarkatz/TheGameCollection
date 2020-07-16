"""
The model of the Hangman
"""
from string import ascii_letters
from random import choice


class WordList:
    def __init__(self, dict_file):
        self.words_file = dict_file
        self.words = self.get_words_from_file()

    def get_random_word(self):
        """
        Choose a random word from a dictionary file.
        :return: a random word from the file
        """
        return choice(self.words)

    def get_words_from_file(self):
        """
        Gets gets words file, returns list of words from the file
        :return:
        """
        with open(self.words_file) as word_file:
            words = word_file.read().split()
        return words


class HangmanLogic:
    def __init__(self, secret_word, tries):
        self.secret_word = secret_word
        self.tries = tries
        self.mistakes = 0
        self.guesses_list = []
        self.is_win = False

    def get_word(self):
        """
       Returns the secret word: the letters that were guessed are shown,
        Other letters appear as "_"
        :return: the secret word, with only the guessed letters shown
        """
        secret_word_shown = ""
        for letter in self.secret_word:
            if letter in self.guesses_list:
                secret_word_shown += letter
            else:
                secret_word_shown += "_"
            secret_word_shown += " "
        return secret_word_shown[:-1:]

    def try_update_letter_guessed(self, letter):
        """
        Checks if guess is valid - if yes, adds it to the guessed letters, otherwise prints X.
        :param letter: the player's input (string)
        :return: old_letters_guessed (if guess was valid - with the new guess)
        """
        letter = letter.lower()
        if self.check_valid_input(letter):
            self.guesses_list.append(letter)
            if letter not in self.secret_word:
                self.tries -= 1

    def check_valid_input(self, guessed_letter):
        """
        Checks if payer's input is valid: a letter that wasn't guessed before
        :param guessed_letter: the player's input (string)
        :return: True if the input is valid, else - False
        """
        if guessed_letter in self.guesses_list:
            return False
        if len(guessed_letter) != 1:
            return False
        if guessed_letter not in ascii_letters:
            return False
        return True

    def check_win(self):
        """
        Checks if player won.
        :return: True if won, else - False
        """
        for letter in self.secret_word:
            if letter not in self.guesses_list:
                return False
        return True
