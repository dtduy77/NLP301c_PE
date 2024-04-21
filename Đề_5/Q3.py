from nltk.tokenize import sent_tokenize
def tokenize_text(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    return sentences

# Sample text
text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."

# Tokenize the text
tokenized_text = tokenize_text(text)

# Display original string
print("Original string:")
print(text)

# Display sentence-tokenized copy in a list
print("\nSentence-tokenized copy in a list:")
print(tokenized_text)

# Display the sentences in a readable format
print("\nRead the list:")
for sentence in tokenized_text:
    print(sentence)
