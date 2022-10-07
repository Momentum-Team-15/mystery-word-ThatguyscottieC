import timeit
import string
import re
from string import punctuation


def strip_punctuation(text):
    for character in string.punctuation:
        text = text.replace(character, "")
    return text


# dictionary for word count
word_count = {}

# remove stop words


def no_stop_words(text):
    for word in text:
        if word in STOP_WORDS:
            text.remove(word)
    return text

# function to count number of words


def word_count_function(file):
    # remove the punctuation characters
    clean_file = strip_punctuation(file)
    # separate words by spaces into a list, convert words to lower case
    words = [word.lower() for word in clean_file.split()]
    # remove the stop words
    clean_text = no_stop_words(words)
    # count the number of words
    for word in clean_text:
        if word not in word_count:
            # create a new entry if it doesn't exist in dictionary
            word_count[word] = 1
        # start the counter
        word_count[word] += 1
    print(word_count)


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    # goes through the lines in the file
    with open(file, 'r') as f:
        read_file = f.read()
        word_count_function(read_file)
        # takes out all of the punctuation characters


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
