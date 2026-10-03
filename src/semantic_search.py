from sklearn.metrics.pairwise import cosine_similarity


def semantic_search(model,documents,documents_embedding,query,threshold=0.2):
    filenames=list(documents.keys())
    content=list(documents.values())

    
    query_embadding=model.encode([query])

    similarities=cosine_similarity(
        query_embadding,
        documents_embedding
    )[0]

    result={}

    for filename,score in zip(filenames,similarities):
        if score>threshold:
            result[filename]=score

    return dict(
        sorted(
            result.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )    


