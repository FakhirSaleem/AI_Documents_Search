from pathlib import Path

Data_Folder=Path("data")

def read_documents():
    documents={}

    for file in Data_Folder.glob("*.txt"):
        with open(file,"r",encoding="utf-8") as f:
            documents[file.name]=f.read()

    return documents
