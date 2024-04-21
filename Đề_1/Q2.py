import nltk
from nltk.corpus import nps_chat
from nltk import FreqDist

def find_four_letter_words(text):
    """
    Find all four-letter words in a given text.

    Parameters
    ----------
    text : str
        The text to search for four-letter words in.

    Returns
    -------
    List[str]
        A list of all four-letter words in the given text.
    """
    four_letter_words = [word.lower() for word in text if len(word) == 4 and word.isalpha()]
    return four_letter_words

# Download the Chat Corpus (text5)
nltk.download('nps_chat')
chat_corpus = nps_chat.words()

# Find four-letter words
four_letter_words = find_four_letter_words(chat_corpus)

# Create a frequency distribution
freq_dist = FreqDist(four_letter_words)

# Display four-letter words in decreasing order of frequency
sorted_by_frequency = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)
for word, frequency in sorted_by_frequency:
    print(f"{word}: {frequency}")
