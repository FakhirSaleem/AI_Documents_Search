from flask import Flask,request,jsonify,render_template
from main import initialize_rag
from src.rag import Question_Answer
from src.embedding import model
from werkzeug.utils import secure_filename
import os
from pathlib import Path
import json

app=Flask(__name__,template_folder="../templates")


base_folder=Path(__file__).resolve().parent.parent
Upload_Folder=base_folder/"data"
app.config["UPLOAD_FOLDER"]=Upload_Folder
UPLOADED_DOCUMENTS_FILE= base_folder/"uploaded_documents.json"

if not UPLOADED_DOCUMENTS_FILE.exists():
    with open(UPLOADED_DOCUMENTS_FILE,"w") as file:
        json.dump([],file)

        

embeddings,chunk_texts,chunk_info,chunk_ids=initialize_rag()




@app.route("/")
def home():
    return render_template("index.html")




history=[]

@app.route("/ask",methods=["POST"])
def ask():


    data=request.get_json()
    query=data.get("query")


    if not query:
        return jsonify({
            "error":"Query is Required"
        }),400

    answer,sources= Question_Answer(model,embeddings,chunk_texts,chunk_info,chunk_ids,query,top_k=10,final_k=3,threshold=0.25,history=history)

    if answer is None:
        return jsonify({
            "answer":None,
            "sources":[]
        })

    history.append((query,answer))
    history[:]=history[-5:]


    return jsonify({
        "answer": answer,
        "sources": sources
    })



@app.route("/upload",methods=["POST"])
def upload():
    files = request.files.getlist("documents")

    if not files or all(file.filename == "" for file in files):
        return jsonify({
            "error": "Please select at least one document."
        }), 400

    # Validate all files before saving any
    for file in files:

        if file.filename == "":
            return jsonify({
                "error": "One of the selected files has no filename."
            }), 400

        if not file.filename.lower().endswith(".txt"):
            return jsonify({
                "error": "Only .txt files are allowed."
            }), 400

    uploaded_files = []

    for file in files:

        filename = secure_filename(file.filename)

        if not filename:
            return jsonify({
                "error": "Invalid filename."
            }), 400

        file.save(
            os.path.join(app.config["UPLOAD_FOLDER"], filename)
        )

        uploaded_files.append(filename)



    with open(UPLOADED_DOCUMENTS_FILE, "r") as file:
        uploaded_documents = json.load(file)

    uploaded_documents.extend(uploaded_files)

    with open(UPLOADED_DOCUMENTS_FILE, "w") as file:
        json.dump(uploaded_documents, file, indent=4)


    global embeddings,chunk_texts,chunk_info,chunk_ids
    embeddings,chunk_texts,chunk_info,chunk_ids=initialize_rag()


    return jsonify({
        "message": f"{len(uploaded_files)} documents uploaded successfully.",
        "files": uploaded_files
    })






@app.route("/documents", methods=["GET"])
def documents():

    with open(UPLOADED_DOCUMENTS_FILE, "r") as file:
        files = json.load(file)

    return jsonify({
        "documents": files
    })












if __name__=="__main__":
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=5000)

    # with app.test_client() as client:
    #     response= client.post(
    #         "/ask",
    #         json={"query":"What is Python"}

    #     )
    # print(response.json)    