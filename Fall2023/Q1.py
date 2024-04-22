import re

# Define the regular expression pattern
pattern = r'\b\d+(?:\s*[\+\-\/]\s*\d+)*\b'

# Input text
text = 'Calculate 3 + 5 + 4 - 5 - 6 - 2'
# Find all matches in the text
a = re.findall(pattern, text)

# Print the matches
print(a)

b = re.findall(r'\b(a|an|the)\b', 'There is an apple on the top of a lunchbox at the room')
print(b)