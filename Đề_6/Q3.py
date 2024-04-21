import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Sample input text
text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."

# Tokenize sentences
sentences = sent_tokenize(text)

# Tokenize words sentence-wise and store them in a list
tokenized_sentences = []
for sentence in sentences:
    words = word_tokenize(sentence)
    tokenized_sentences.append(words)

# Print the original string
print("Original string:")
print(text)

# Print the tokenized words sentence-wise
print("Tokenize words sentence wise:\nRead the list:")
for i, words in enumerate(tokenized_sentences):
    print(words)
