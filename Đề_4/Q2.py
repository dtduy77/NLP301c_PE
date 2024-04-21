import nltk
from nltk.corpus import brown
from collections import Counter

nltk.download('brown')

def find_words_with_frequency(corpus: str, frequency: int=3):

    words = brown.words(categories=corpus)
    word_counts = Counter(words)
    answers = [word for word, count in word_counts.items() if count >= frequency]
    return answers

#Choose a possible type in Brown Corpus, for example 'news';
corpus_category = 'news'

#Show answer;
answers = find_words_with_frequency(corpus_category, 3)
print(answers)