def freq_word(word,text):
    num = text.split().count(word)
    percent = num/len(text.split()) * 100
    return num, percent


text = "I want to sleep. I"
word = "I"
print(freq_word(word,text))