class TextManipulation:

    def __init__(self, text=None):
        """
        Constructor for the TextManipulation class.

        :param str text: Input string to be manipulated. Default is None.
        """
        self.text = text

    def all_uppercase_letters(self):
        """
        Converts all letters in text string to uppercase letters.

        :return:
            str: Converted string to uppercase letters.
            None: Returns None if input string is empty.
        """
        if self.text:
            return self.text.upper()
        else:
            return None

    def all_lowercase_letters(self):
        """
        Converts all letters in text string to lowercase letters.

        :return:
            str: Converted string to lowercase letters.
            None: Returns None if input string is empty

        """
        if self.text:
            return self.text.lower()
        else:
            return None

    def capitalisation(self):
        """
        Converts the first letter of the input string to uppercase, acting as auto-capitalization
        for words at the beginning of a sentence, names, titles, etc.

        :return:
            str: Converted string with the first letter in uppercase.
            None: Returns None if the input string is empty.
        """
        if self.text:
            return self.text.capitalize()
        else:
            return None

    def concatenate_string(self, str_to_concatenate):
        """
        Concatenates two strings using the concatenation method.

        :param:
            str strToConcatenate: String to concatenate to.

        :return:
            If both strings have content, it will return a concatenated string.

            If one input string has content but the other doesn't, it will only
            return the string with content.

            If both strings have no content, it will return None.
        """
        return self.text + str_to_concatenate if str_to_concatenate else self.text

    def search_replace(self, find, replacement):
        """
        Searches for specific text and if found, text will be replaced with replacement.

        :param:
            str find: Target text to search for.

            str replacement: Text to replace target text.

        :return:
            Return text with replacement if text was found, otherwise return original.
        """
        return self.text.replace(find, replacement) if find in self.text else self.text

    def substring(self, start, end):
        """
        Slicing function meant to return a substring of a text given a range of indices

        :param:
            int start: Indicates the start of the substring to be returned.
            int end: Indicates the end of the substring to be returned.

        :return:
            Returns a substring of the input text based on the specified range.
        """
        return self.text[start:end]
