from src.chunk_search import chunk_search
from src.llm import generate_answer
from src.reranker import reranking
from src.quer_rewriter import query_rewriter

def Question_Answer(model,embeddings,chunk_texts,chunk_info,chunk_ids,query,top_k,final_k,threshold,history):

    if history is None:
        history=[]

    search_query=query_rewriter(query,history)   

    chunk_search_result=chunk_search(model,embeddings,chunk_texts,chunk_info,chunk_ids,search_query,top_k=top_k,threshold=threshold)


    if not chunk_search_result:
        print("No Matching Text")
        return None, set()


    chunk_search_result=reranking(chunk_search_result,query)

    chunk_search_result=chunk_search_result[:final_k]



    content="\n\n".join(
    f"[{i}] Source: {filename} ({ids})\n"
    f"Retrieved Text:{text}"
    for i,(text,filename,ids,similarity_score,rerank_score) in enumerate(chunk_search_result,start=1)
    )



    if not chunk_search_result:
        print("No matching text ! ")
        return None, set()



    answer=generate_answer(content,query,history)

    sources = []


    for i,(text, filename,ids,similarity_score,rerank_score) in enumerate(chunk_search_result,start=1):
        sources.append((i,filename,ids,float(similarity_score),float(rerank_score),text))
            
            

    return answer, sources    

