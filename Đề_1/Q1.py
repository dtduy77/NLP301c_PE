import re

def find_lowercase_words(text: str) -> list:
    """
    Find all lowercase words in a text.

    Parameters:
    text (str): The text to search for lowercase words.

    Returns:
    list: A list of lowercase words found in the text.
    """
    lowercase_words = re.findall(r'\b[a-z]+\b', text)
    return lowercase_words


text = "em YEU truong em voi bao BAN THAN"

print(find_lowercase_words(text))