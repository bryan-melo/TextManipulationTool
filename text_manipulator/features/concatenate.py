def concatenate_strings(initialStr, strToConcatenate):
    """
    Concatenates two strings using the concatenation method.

    :param:
        str initialString: Input string.
        str strToConcatenate: Input string.

    :return:
        If both strings have content, it will return a concatenated string.

        If one input string has content but the other doesn't, it will only
        return the string with content.

        If both strings have no content, it will return None.
    """

    if initialStr and strToConcatenate:    # if both strings are not empty
        return initialStr + strToConcatenate    # return: concatenated string
    elif initialStr or strToConcatenate:    # If one string is non-empty and the other is empty
        return initialStr if initialStr else strToConcatenate    # return: the non-empty string
    else:    # if both strings are empty
        return ''    # return: empty string


