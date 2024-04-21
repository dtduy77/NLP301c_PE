import spacy

text = "Robert Langdon is a famous character in various books and movies"

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Tokenize the input text
doc = nlp(text)

# Merge the first name and last name as a single token
with doc.retokenize() as retokenizer:
    retokenizer.merge(doc[0:2])

# Print the tokens
for token in doc:
    print(token.text)
