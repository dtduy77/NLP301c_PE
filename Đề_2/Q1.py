import re

def ize_word(text: str) -> list:
    """
    This function takes a string as input and returns a list of all the words in the input string that match the pattern 'ize'.

    Args:
        text (str): The input string

    Returns:
        list: A list of all the words in the input string that match the pattern 'ize'

    """
    patern = r'\b\w*ize\b'
    words = re.findall(patern, text)
    return words

text = "The company plans to reorganize its structure to improve efficiency."
print(ize_word(text))