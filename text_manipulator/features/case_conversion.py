def all_uppercase_letters(str1):
    """
    Converts all letters in str1 string to uppercase letters.

    :param:
        str str1: Input string.

    :return:
        str: Converted string to uppercase letters.
        None: Returns None if input string is empty.
    """
    if str1:
        return str1.upper()
    else:
        return None


def all_lowercase_letters(str1):
    """
    Converts all letters in str1 string to lowercase letters.

    :param:
        str str1: Input string.

    :return:
        str: Converted string to lowercase letters.
        None: Returns None if input string is empty

    """
    if str1:
        return str1.lower()
    else:
        return None


def capitalisation(str1):
    """
    Converts the first letter of the input string to uppercase, acting as auto-capitalization
    for words at the beginning of a sentence, names, titles, etc.

    :param:
        str str1: Input string.

    :return:
        str: Converted string with the first letter in uppercase.
        None: Returns None if the input string is empty.
    """
    if str1:
        return str1.capitalize()
    else:
        return None
