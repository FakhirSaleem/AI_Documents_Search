def search_documents(index,query):
    query=query.lower()

    if query in index:
        return index[query]

    return []
            

