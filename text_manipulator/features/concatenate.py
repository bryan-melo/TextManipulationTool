def concatenate_strings(str1, str2):
    """
    Concatenates two strings using the concatenation method.

    :param:
        str1: Input string.
        str2: Input string.

    :return:
        If both strings have content, it will return a concatenated string.

        If one input string has content but the other doesn't, it will only
        return the string with content.

        If both strings have no content, it will return None.
    """

    if str1 and str2:                   # if both strings are not empty
        return str1 + str2              # return: concatenated string
    elif str1 or str2:                  # If one string is non-empty and the other is empty
        return str1 if str1 else str2   # return: the non-empty string
    else:                               # if both strings are empty
        return ''                       # return: empty string


