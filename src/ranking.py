def ranked_documents(documents,query,results):
    scores={}
    query=query.lower()

    for filename in results:
        content=documents[filename]
        words=content.lower().split()

        score=words.count(query)

        scores[filename]=score

    ranked_result=sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )    

    return ranked_result


