from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.nlp_processor import preprocess_text

def create_tfidf(documents):
    filenames=list(documents.keys())
    content=[
        " ".join(preprocess_text(content))
        for content in documents.values()
    ]

    vectorizer=TfidfVectorizer()
    documents_vector=vectorizer.fit_transform(content)
    return filenames,vectorizer,documents_vector



def tfidf_search(filenames,vectorizer,documents_vector,query):
    query=" ".join(preprocess_text(query))

    query_vector=vectorizer.transform([query])


    similarities=cosine_similarity(
        query_vector,
        documents_vector
    )[0]
    result={}

    for filename, score in zip(filenames,similarities):
        if score>0:
            result[filename]=score

    return dict(
        sorted(
        result.items(),
        key=lambda item: item[1],
        reverse=True
    ))




