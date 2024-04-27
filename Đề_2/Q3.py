from nltk.tokenize import regexp_tokenize

def text_split(text: str) -> list:
    
    # pattern = r"\w+|[^\w\s]"
    pattern = r"\w+|[',.]"
    list_word = regexp_tokenize(text, pattern)
    return list_word

#Create dataset;
text = "Reset your password if you just can't remember your old one."

#Show answers;
list_word = text_split(text)
print(list_word)

