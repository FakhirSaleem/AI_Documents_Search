def hybrid_search(tfidf_result,semantic_result,alpha=0.5):
    scores={}
    filenames=set(tfidf_result) | set(semantic_result)

    for filename in filenames:
        tfidf_score=tfidf_result.get(filename,0)
        semantic_score=semantic_result.get(filename,0)

        score=(
            alpha*tfidf_score+
            (1-alpha)*semantic_score
        )

        scores[filename]=score

    return dict(
        sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )

