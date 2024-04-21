import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "I may bake a cake for my birthday. The talk will introduce reader about Use of baking"

# Process text with spaCy
doc = nlp(text)

# Extract verb phrases
verb_phrases = []
for token in doc:
    if token.pos_ == 'VERB':
        verb_phrase = [token.text]
       # print(verb_phrase) # ['bake'], ['introduce'], ['baking]
        for child in token.children:
            if child.dep_ in ['aux', 'auxpass']:
              #  print(child.text) # may, will
                verb_phrase.insert(0, child.text) 
              #  print(verb_phrase) # ['may', 'bake'], ['will', 'introduce']
        if len(verb_phrase) > 1:
            verb_phrases.append(' '.join(verb_phrase))
       # print(verb_phrases) # ['may bake', 'will introduce']
# Print verb phrases
print('Verb phrases:')
for phrase in verb_phrases:
    print(phrase)
