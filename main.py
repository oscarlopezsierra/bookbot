from stats import count_words
from stats import count_characters
from stats import sort_character_counts
import sys

def get_book_test(filepath):
    """
    Returns the contents of the filepath as a string.
    :param filepath: file
    :return: contents of the file as a string
    """
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    contents = get_book_test(filepath)
    number_of_words = count_words(contents)
    print(f"{number_of_words} words found in the document")
    character_counts = count_characters(contents)
    print(character_counts)
    sorted_character_counts = sort_character_counts(character_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for character in sorted_character_counts:
        char = character['char']
        if char.isalpha():
            print(f"{character['char']}: {character['num']}")
    print("============= END ===============")

main()
