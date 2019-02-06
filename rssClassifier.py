import nltk
from nltk.stem import RSLPStemmer


#Code from: https://www.linkedin.com/pulse/classifica%C3%A7%C3%A3o-de-textos-em-python-luiz-felipe-araujo-nunes/
def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence

def Stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase

def RemoveStopWords(sentence):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    phrase = []
    for word in sentence:
        if word not in stopwords:
            phrase.append(word)
    return phrase

def Train():
    pass
    
def Learning(training_data):
    corpus_words = {}
    for data in training_data:
        frase = data['frase']
        frase = Tokenize(frase)
        frase = Stemming(frase)
        frase = RemoveStopWords(frase)
        class_name = data['classe']
        if class_name not in list(corpus_words.keys()):
            corpus_words[class_name] = {}
        for word in frase:
            if word not in list(corpus_words[class_name].keys()):
                corpus_words[class_name][word] = 1
            else:
                corpus_words[class_name][word] += 1
    return corpus_words

def calculate_class_score(sentence,class_name):
    score = 0
    sentence = Tokenize(sentence)
    sentence = Stemming(sentence)
    for word in sentence:
        if word in dados[class_name]:
            score += dados[class_name][word]
    return score

def calculate_score(sentence):
    high_score = 0
    classname = 'default'
    for classe in dados.keys():
        pontos = 0
        pontos = calculate_class_score(sentence,classe)
        if pontos > high_score:
            high_score = pontos
            classname = classe
    return classname,high_score
