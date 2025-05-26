def count_words(contents):
    """
    Returns the number of words in the contents.
    :param contents: string
    :return: number of words in the string
    """
    return len(contents.split())

def count_characters(contents):
    """
    Return a dictionary with the count of each character in the contents.
    :param contents:
    :return: dictionary with character counts
    """
    character_count = {}
    for char in contents:
        key = char.lower()
        if key in character_count:
            character_count[key] += 1
        else:
            character_count[key] = 1
    return character_count

def sort_on(dictionary):
    return dictionary['num']

def sort_character_counts(character_counts):
    """
    Sorts the character counts dictionary by the count in descending order.
    :param character_counts: dictionary with character counts
    :return: sorted list of dictionaries with character and count
    """
    dictionary = []
    for key, value in character_counts.items():
        dictionary.append({'char': key, 'num': value})
    dictionary.sort(reverse=True, key=sort_on)
    return dictionary
