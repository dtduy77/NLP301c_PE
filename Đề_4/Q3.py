import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

def tokenize_sentences_and_words(text: str):
    # Tokenize the text into sentences. Defaults.PunktSentenceTokenizer 
    sentences = sent_tokenize(text)
    # Tokenize each sentence into words
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    
    return tokenized_sentences

# Example usage:
text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."
print('Original text:', text)
tokenized_sentences = tokenize_sentences_and_words(text)
for sentence in tokenized_sentences:
    print(sentence)
