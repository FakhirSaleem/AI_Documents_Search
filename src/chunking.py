def chunk_text(text,chunk_size=50,ovelapping=3):
    words=text.split()
    chunks=[]
    start=0

    while start<len(words):
        end=start+chunk_size

        if ovelapping>=chunk_size:
            print("Overlap must be samller than chunk size")


        chunk=" ".join(words[start:end])
        chunks.append(chunk)

        start+=chunk_size-ovelapping

    
    return chunks    




