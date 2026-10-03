def recall(results,relevant_documents):
    results=set(results.keys())
    relevant_documents=set(relevant_documents)
    correct=results & relevant_documents
    if len(relevant_documents)==0:
        return 0
    score=len(correct)/len(relevant_documents)
    return score



def precison(results,relevant_documents):
    results=set(results.keys())
    relevant_documents=set(relevant_documents)
    correct=results & relevant_documents
    if len(results)==0:
        return 0
    score=len(correct)/len(results)
    return score



def f1_Score(results,relevant_documents):
    p=precison(results,relevant_documents)
    r=recall(results,relevant_documents)
    if p+r==0:
        return 0
    f1=2*(p*r)/(p+r)
    return f1



