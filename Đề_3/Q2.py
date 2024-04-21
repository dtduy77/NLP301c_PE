def words_not_in_vocab(text, vocabulary):
    # Tokenize the text string into words
    text_words = text.split()
    
    # Convert both the text and vocabulary lists to sets for faster lookup
    text_set = set(text_words)
    vocab_set = set(vocabulary)
    
    # Use set difference to find words in the text that are not in the vocabulary
    words_not_in_vocab_set = text_set - vocab_set
    
    return words_not_in_vocab_set

# Example usage:
text = "apple banana orange kiwi pear"
vocabulary = ["apple", "banana", "grape", "kiwi", "pineapple"]
result = words_not_in_vocab(text, vocabulary)
print(result)  # Output: {'orange', 'pear'}