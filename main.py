import os
import numpy as np
from src.document_reader import read_documents
from src.embedding import model
from src.chunking import chunk_text
from src.chunks_embedding import chunks_embedding
from src.rag import Question_Answer
from src.vector_store import load_vector_store,save_vector_store,create_hashes,split_documents,get_unchanged_chunks,vector_store_path



CANDIDATE_K=10
FINAL_K=3
THRESHOLD=0.25



def initialize_rag():


    documents=read_documents()
    current_hashes=create_hashes(documents)
    chunks={}
    for filename,text in documents.items():
        chunks[filename]=chunk_text(text)





    if os.path.exists(vector_store_path):

        embeddings,chunk_texts,chunk_info,chunk_ids,documents_hashes=load_vector_store()

        if current_hashes==documents_hashes:
                print("Loaded existing Vector Store")

        else:
            unchanged,changed=split_documents(documents,documents_hashes,current_hashes)
            changed_chunks={}


            for filename,text in changed.items():
                changed_chunks[filename]=chunk_text(text)


            if changed_chunks:
                new_embeddings,new_chunk_texts,new_chunk_info,new_chunk_ids=chunks_embedding(model,changed_chunks)
            else:
                new_embeddings=np.array([])
                new_chunk_texts=[]
                new_chunk_info=[]
                new_chunk_ids=[]


            old_embeddings,old_chunk_texts,old_chunk_info,old_chunk_ids=get_unchanged_chunks(embeddings,chunk_texts,chunk_info,chunk_ids,unchanged)


            if changed_chunks:
                if old_embeddings.size == 0:
                    embeddings=new_embeddings
                else:
                    embeddings=np.concatenate(
                        [old_embeddings,
                         new_embeddings]
                         )    
            
                chunk_texts=old_chunk_texts+  new_chunk_texts
                chunk_info=old_chunk_info + new_chunk_info
                chunk_ids=old_chunk_ids + new_chunk_ids
            else:
                embeddings=old_embeddings
                chunk_texts=old_chunk_texts
                chunk_info=old_chunk_info
                chunk_ids=old_chunk_ids


            save_vector_store(embeddings,chunk_texts,chunk_info,chunk_ids,current_hashes)

            print("Document changed, New Embeddings have been Saved")    


    else:
        embeddings,chunk_texts,chunk_info,chunk_ids=chunks_embedding(model,chunks)
        save_vector_store(embeddings,chunk_texts,chunk_info,chunk_ids,current_hashes)
        print("New Embeddings have been Saved")


    return embeddings,chunk_texts,chunk_info,chunk_ids         
   





if __name__=="__main__":

    embeddings,chunk_texts,chunk_info,chunk_ids=initialize_rag()

    history=[]

    while True:
        query=input("Enter Query (or exit to quit): ")
        if query.lower()=="exit":
            break


        answer,sources=Question_Answer(model,embeddings,chunk_texts,chunk_info,chunk_ids,query,top_k=CANDIDATE_K,final_k=FINAL_K,threshold=THRESHOLD,history=history)



        if answer is None:
            print("\nNo relevant information found in the documents.")
        else:
            print("\nAnswer:")
            print(answer)
            print("\nSources:")
            for i,filename,ids,similarity_score,rerank_score,text in sources:
                print ( f"[{i}] {filename} ->  {ids} -> Similarity_score: {similarity_score*100:.2f}% -> Rerank: {rerank_score:.2f}")
                print(" Retrieved text: ",text)
            history.append((query,answer))
            history=history[-5:]







