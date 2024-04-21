import re
import nltk
from nltk.corpus import stopwords, gutenberg

def remove_punctuation(text):
    # Define a regular expression pattern to match all punctuation
    pattern = r'[^\w\s]'
    
    # Use re.sub() to replace all matches of the pattern with an empty string
    text_without_punctuation = re.sub(pattern, '', text)
    
    return text_without_punctuation

def frequently_words(text: str, stop_words: set, number_words: int=50) -> dict:

    dict_words = {}

    word_list_from_text = re.split(r'[ \n]+', text)

    for word in word_list_from_text:

        if word not in stop_words:

            if word not in dict_words:
                dict_words[word] = 1
            else:
                dict_words[word] += 1
    dict_words = dict(sorted(dict_words.items(), key=lambda item: item[1], reverse=True))
    top_words = {k: v for k, v in list(dict_words.items())[:number_words]}
    return top_words

#Create stopwords;
stop_words = set(stopwords.words('english'))

#Create dataset from nltk;
nltk.download('gutenberg')
book_names = gutenberg.fileids()
selected_book = 'austen-emma.txt'
book_text = gutenberg.raw(selected_book)

book_text = remove_punctuation(book_text)
#Show answer
answers = frequently_words(book_text, stop_words)
print(answers)