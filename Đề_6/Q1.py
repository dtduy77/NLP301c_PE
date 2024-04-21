import nltk
from nltk.corpus import nps_chat

# Download the NPS Chat Corpus if not already downloaded
nltk.download('nps_chat')

# Access the Chat Corpus (text5)
chat_corpus = nps_chat.words()

# Filter four-letter words
four_letter_words = [word for word in chat_corpus if len(word) == 4 and word.isalpha()]

# Create a frequency distribution
freq_dist = nltk.FreqDist(four_letter_words)

# Display four-letter words in decreasing order of frequency
for word, frequency in freq_dist.most_common():
    print(f"{word}: {frequency}")