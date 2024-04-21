import re

def percent(word: str, text: str) -> float:
    """
    Calculates the percentage of a word in a text.

    Args:
        word (str): The word to search for.
        text (str): The text to search in.

    Returns:
        float: The percentage of the word in the text.

    """
    pattern = r"\b\w+\b"
    token = re.findall(pattern, text)
    total_words = len(token)
    word_count = token.count(word)
    return (word_count / total_words) * 100

text = "John lives in Canada. James lives in America, though he's not from there lives lives lives lives lives lives"
word = "lives"
print(f"The word '{word}' occurs in the text  {percent(word, text)}% of the time")
