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
    if str1 and str2:
        return str1 + str2
    elif str1 and not str2:
        return str1
    elif str2 and not str1:
        return str2
    else:
        return ''
