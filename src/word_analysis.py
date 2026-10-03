import pandas as pd
import re

def word_frequency(documents):
    words_count={}

    stop_words = {
        "the", "is", "a", "an", "and",
        "of", "to", "in", "on", "for",
        "with", "this", "that", "it"
        }



    for content in documents.values():
        words=re.findall(r'\b\w+\b',content.lower())

        for word in words:
            if word not in stop_words:
                words_count[word]=words_count.get(word,0)+1

        df=pd.DataFrame(
            list(words_count.items()),
            columns=["Words","Frequency"] 
        )    

        df=df.sort_values(
            "Frequency",
            ascending=False
        )

    return df    


