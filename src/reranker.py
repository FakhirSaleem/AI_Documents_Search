from sentence_transformers import CrossEncoder

model=CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def reranking(results,query):
    pairs=[
        (query,result[0])
        for result in results
    ]

    scores=model.predict(pairs)

    reranked=[]

    for result,score in zip(results,scores):
        reranked.append(
            (result[0],
            result[1],
            result[2],
            result[3],
            float(score)
            )
        )

    reranked.sort(
        key=lambda item: item[4],
        reverse=True
    )

    return reranked

    