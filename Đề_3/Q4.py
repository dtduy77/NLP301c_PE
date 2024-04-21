import spacy

# Assuming you've already loaded the spaCy model (e.g., nlp = spacy.load("en_core_web_sm"))
nlp = spacy.load("en_core_web_sm")
text1 = "John lives in Canada"
text2 = "James lives in America, though he's not from there"

doc1 = nlp(text1)
doc2 = nlp(text2)

similarity_score = doc1.similarity(doc2)

print(similarity_score)