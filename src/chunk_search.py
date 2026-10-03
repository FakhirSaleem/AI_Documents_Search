from sklearn.metrics.pairwise import cosine_similarity



def get_neighbour_chunk_id(chunk_id):
    filename,chunk_number=chunk_id.rsplit("_chunk_",1)
    chunk_number=int(chunk_number)
    neighbours=[]
    if chunk_number>1:
        neighbours.append(f"{filename}_chunk_{chunk_number-1}")
    
    neighbours.append(f"{filename}_chunk_{chunk_number+1}")
    return neighbours



def chunk_search(model,embeddings,chunk_text,chunk_info,chunk_ids,query,top_k=None,threshold=None):
    query_embeddings=model.encode([query])

    similarities=cosine_similarity(
        query_embeddings,
        embeddings
    )[0]
    

    results=[]

    for text,filename,score,ids in zip(chunk_text,chunk_info,similarities,chunk_ids):
        if score>threshold:
            results.append((text,filename,ids,score))

    results.sort(
        key=lambda item: item[3],
        reverse=True
    )
    if top_k is None:
        return results


    selected = results[:top_k]

    chunk_lookup = {
        chunk_id: (text, filename, chunk_id, score)
        for text, filename, chunk_id, score in zip(chunk_text, chunk_info, chunk_ids, similarities)
        }
    for result in results[:top_k]:
        chunk_id = result[2]
        for neighbor_id in get_neighbour_chunk_id(chunk_id):
            if neighbor_id in chunk_lookup:
                neighbor = chunk_lookup[neighbor_id]
                if neighbor not in selected:
                    selected.append(neighbor)
    return selected