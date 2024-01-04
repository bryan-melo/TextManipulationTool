def all_uppercase_letters(text):
    """
    Converts all letters in text string to uppercase letters.

    :param:
        str text: Input string.

    :return:
        str: Converted string to uppercase letters.
        None: Returns None if input string is empty.
    """
    if text:
        return text.upper()
    else:
        return None


def all_lowercase_letters(text):
    """
    Converts all letters in text string to lowercase letters.

    :param:
        str text: Input string.

    :return:
        str: Converted string to lowercase letters.
        None: Returns None if input string is empty

    """
    if text:
        return text.lower()
    else:
        return None


def capitalisation(text):
    """
    Converts the first letter of the input string to uppercase, acting as auto-capitalization
    for words at the beginning of a sentence, names, titles, etc.

    :param:
        str text: Input string.

    :return:
        str: Converted string with the first letter in uppercase.
        None: Returns None if the input string is empty.
    """
    if text:
        return text.capitalize()
    else:
        return None
