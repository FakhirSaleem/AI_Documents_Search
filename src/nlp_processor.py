import re
# import nltk

from nltk.stem import WordNetLemmatizer 
from nltk import pos_tag
from nltk.corpus import wordnet

# nltk.download("wordnet")
# nltk.download("averaged_perceptron_tagger")
# nltk.download("averaged_perceptron_tagger_eng")


stop_words= {
    "the", "is", "a", "an", "and",
    "of", "to", "in", "on", "for",
    "with", "this", "that", "it"
    }

lemitizer=WordNetLemmatizer()

def get_wordnet_pos(word):
    tag=pos_tag([word])[0][1]

    if tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("R"):
        return wordnet.ADV

    return wordnet.NOUN

def preprocess_text(text):
    text=text.lower()

    words=re.findall(r'\b\w+\b',text)

    words=[
        word
        for word in words
        if word not in stop_words]
    
    words=[
        lemitizer.lemmatize(
            word,
            get_wordnet_pos(word)
            )
        for word in words]



    return words