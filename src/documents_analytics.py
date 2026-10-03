import numpy as np

def documents_statistics(documents):
    words_count=[]

    for filename,content in documents.items():
        words=content.lower().split()
        words_count.append(len(words))

    words_count=np.array(words_count)

    return {
        "Total Documents":len(words_count),  
        "Total Words": np.sum(words_count),
        "Average Words": round(np.mean(words_count),2),
        "Smallest Document":np.min(words_count),
        "Largest Document":np.max(words_count)
    }    


