from nltk.tokenize import regexp_tokenize


def text_split(text: str) -> list:

    pattern = r"\w+|[^\w\s]"
    list_word = regexp_tokenize(text, pattern)

    return list_word

text = "Reset your password if you just can't remember your old one."

print(text_split(text)) # Output: