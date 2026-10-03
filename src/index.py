def build_index(documents):
    index={}

    for filename,content in documents.items():
        words=content.lower().split()

        for word in words:

            if word not in index:
                index[word]=[]

            if filename not in index[word]:
                index[word].append(filename)

    return index                 



           
