from nltk.tokenize import regexp_tokenize


def text_split(text: str) -> list:
    """
    This function takes a string as input and returns a list of words after tokenizing it.

    Parameters:
    text (str): The input text.

    Returns:
    list: A list of words after tokenizing the input text.

    """
    pattern = r"\w+|[^\w\s]"
    list_word = regexp_tokenize(text, pattern)

    return list_word

text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."

list_word = text_split(text)
print(list_word)