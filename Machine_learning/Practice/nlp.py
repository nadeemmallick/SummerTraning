import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

text = "Heelo nadeem! Language Processing is really"

sentences = sent_tokenize(text)
print("Sentences:")
print(sentences)

words = word_tokenize(text)
print("words:")
print(words)

filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]
print("words after removing stopwords:")
print(filtered_words)

pos_tags = nltk.pos_tag(filtered_words)
print("part of speech tags:")
print(pos_tags)


