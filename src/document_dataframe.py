import pandas as pd

def create_documents_dataframe(documents):
    data=[]

    for filename,content in documents.items():
        words=content.lower().split()

        data.append({
            "Document":filename,
            "Words_Count":len(words),
            "Unique":len(set(words))
        })

    return pd.DataFrame(data)    
