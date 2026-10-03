import numpy as np
import hashlib

vector_store_path="vector_store/vector_store.npz"

def create_hash(documents):
    content=""


    for filename in sorted(documents):
        content+=filename
        content+=documents[filename]


    return hashlib.sha256(
        content.encode("utf-8")
    ).hexdigest()






def create_hashes(documents):
    hashes={}

    for filename,content in documents.items():
        hashes[filename]=hashlib.sha256(
            content.encode("utf-8")
        ).hexdigest()

    return hashes






def save_vector_store(embeddings,chunk_text,chunk_info,chunk_ids,hashes,filename=vector_store_path):
    np.savez(
        filename,
        embeddings=embeddings,
        chunk_text=np.array(chunk_text,dtype=object),
        chunk_info=np.array(chunk_info,dtype=object),
        chunk_ids=np.array(chunk_ids,dtype=object),
        document_hashes=np.array(list(hashes.items()),dtype=object)
    )   





def load_vector_store(filename=vector_store_path):
    data=np.load(filename,allow_pickle=True)

    embeddings=data["embeddings"]
    chunk_text=data["chunk_text"].tolist()
    chunk_info=data["chunk_info"].tolist()
    chunk_ids=data["chunk_ids"].tolist()
    document_hashes=dict(data["document_hashes"].tolist())

    return embeddings,chunk_text,chunk_info,chunk_ids,document_hashes




def split_documents(documents,documents_hashes,current_hashes):
    changed={}
    unchanged={}

    for filename,content in documents.items():
        if filename in documents_hashes and current_hashes[filename]==documents_hashes[filename]:
            unchanged[filename]=content
        else:
            changed[filename]=content

    return unchanged,changed






def get_unchanged_chunks(embeddings,chunk_text,chunk_info,chunk_ids,unchaged_documents):
    old_embeddings=[]
    old_chunk_text=[]
    old_chunk_info=[]
    old_chunk_ids=[]

    for embedding,text,filename,ids in zip(embeddings,chunk_text,chunk_info,chunk_ids):
        if filename in unchaged_documents:
            old_embeddings.append(embedding)
            old_chunk_text.append(text)
            old_chunk_info.append(filename)
            old_chunk_ids.append(ids)


    return np.array(old_embeddings),old_chunk_text,old_chunk_info,old_chunk_ids



    



                

