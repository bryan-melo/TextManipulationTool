def search_replace(text, find, replacement):
    """
    Searches for specific text and if found, text will be replaced with replacement.

    :param:
        str text: Input string.

        str find: Target text to search for.

        str replacement: Text to replace target text.

    :return:
        Return text with replacement if text was found, otherwise return original.
    """
    if find in text:
        return text.replace(find, replacement)
    else:
        return text
