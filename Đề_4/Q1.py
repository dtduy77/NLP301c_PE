import re
import nltk
from nltk.corpus import gutenberg


def write_a_expressions(text: str):

    #Write a egular expressions;
    ize_end_word = re.findall(r'\b\w*z\w*\b', text)
    return ize_end_word

#Create dataset from nltk;
nltk.download('gutenberg')
book_names = gutenberg.fileids()
selected_book = 'austen-emma.txt'
book_text = gutenberg.raw(selected_book)

#Show answer;
answers =  write_a_expressions(book_text)
print(answers)
