from string import ascii_letters
from random import choice


def check_win(secret_word, old_letters_guessed):
    """
    Gets the secret word and the letters that the player guessed and checks if player won.
    :param secret_word: string
    :param old_letters_guessed: list of letters
    :return: True if won, else - False
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def get_secret_word(secret_word, old_letters_guessed):
    """
   Returns the secret word: the letters that were guessed are shown,
    Other letters appear as "_"
    :param secret_word: string
    :param old_letters_guessed: list of letters
    :return: the secret word, with only the guessed letters shown
    """
    secret_word_shown = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            secret_word_shown += letter
        else:
            secret_word_shown += "_"
        secret_word_shown += " "
    return secret_word_shown[:-1:]


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if payer's input is valid: a letter that wasn't guessed before
    :param letter_guessed: the player's input (string)
    :param old_letters_guessed: list of letters
    :return: True if the input is valid, else - False
    """
    if letter_guessed in old_letters_guessed:
        return False
    if len(letter_guessed) != 1:
        return False
    if letter_guessed not in ascii_letters:
        return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word, tries_left):
    """
    Checks if guess is valid - if yes, adds it to the guessed letters, otherwise prints X.
    :param letter_guessed: the player's input (string)
    :param old_letters_guessed: list of letters
    :param secret_word: the word
    :param tries_left: how many wrong tries are left
    :return: old_letters_guessed (if guess was valid - with the new guess)
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        if letter_guessed not in secret_word:
            return old_letters_guessed, tries_left - 1
        return old_letters_guessed, tries_left
    print("Invalid guess")
    return old_letters_guessed, tries_left


def choose_random_word(file_path):
    """
    Choose a random word from a dictionary file.
    :param file_path: a path to a file with list of words that are separated with spaces
    :return: a random word from the file
    """
    return choice(get_words_from_file(file_path))


def get_words_from_file(file_path):
    """
    Gets gets words file, returns list of words from the file
    :param file_path:
    :return:
    """
    with open(file_path) as word_file:
        words = word_file.read().split()
    return words


def win():
    print("YAY!")


def loose():
    print("YOU LOST.")


def main():
    """
    The Main Function of the game
    """
    old_letters_guessed = []
    is_win = False
    tries_left = 6
    word_file = "Words/words.txt"
    secret_word = choose_random_word(word_file)
    print("Let's start!")
    while not is_win and tries_left > 0:
        print("This is your word: {word}".format(word=get_secret_word(secret_word, old_letters_guessed)))
        if old_letters_guessed:
            print("Your guesses: {guesses}".format(guesses=" ".join(old_letters_guessed)))
        print("Tries left: {tries}".format(tries=tries_left))
        print("Guess a letter: ")
        letter_guessed = input().lower()
        old_letters_guessed, tries_left = try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word,
                                                                    tries_left)
        is_win = check_win(secret_word, old_letters_guessed)

    print("You guessed: {word}".format(word=get_secret_word(secret_word, old_letters_guessed)))
    print("The word was: {secret_word}".format(secret_word=secret_word))
    if tries_left > 0:
        win()
    else:
        loose()


if __name__ == '__main__':
    main()
