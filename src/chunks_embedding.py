def chunks_embedding(model,chunks):
    chunks_text=[]
    chunk_info=[]
    chunk_ids=[]

    for filenames,doc_chunks in chunks.items():
        for i,chunk in enumerate(doc_chunks,start=1):
            chunks_text.append(chunk)
            chunk_info.append(filenames)
            chunk_ids.append(f"{filenames}_chunk_{i}")

    embeddings=model.encode(chunks_text)

    return embeddings,chunks_text,chunk_info,chunk_ids



