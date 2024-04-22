import re

delimiter = ['is','the','was','.']
sentence = "Walter was feeling anxious. He was diagnosed today. He probably is the best person I know."

# Create a regex pattern that matches the delimiters
pattern = '|'.join(map(re.escape, delimiter))

# Split the sentence on the delimiters
tokens = re.split(pattern, sentence)

# Remove empty strings from the list of tokens
tokens = [token.strip() for token in tokens if token.strip()]

# Print the tokens
print(tokens)