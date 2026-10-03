# AI-Powered Semantic Document Search & Question Answering System

## Overview

The **AI-Powered Semantic Document Search & Question Answering System** is a web-based application that allows users to upload text documents and ask questions about their content.

Instead of relying only on exact keyword matching, the system uses **semantic search** to find information based on meaning.

> **Find relevant information, even when the exact words are different.**

The system combines document processing, embeddings, vector search, reranking, and Retrieval-Augmented Generation (RAG) to produce answers based on the uploaded documents.

## Features

* Upload multiple `.txt` documents
* Automatically process newly uploaded documents
* Semantic document search
* Question answering using RAG
* Relevant source retrieval
* Similarity and reranking scores
* Display retrieved text used for answering
* Conversation history for follow-up questions
* Persistent list of uploaded documents
* Web-based interface using Flask, HTML, CSS, and JavaScript

## Technologies Used

### Backend

* Python
* Flask

### Natural Language Processing & Machine Learning

* Sentence Transformers
* Transformers
* Scikit-learn
* NLTK
* NumPy
* PyTorch

### Frontend

* HTML
* CSS
* JavaScript

### AI / RAG Components

* Text chunking
* Text embeddings
* Vector similarity search
* Reranking
* Query rewriting
* Retrieval-Augmented Generation (RAG)

## How It Works

The general workflow is:

```text
User uploads documents
        ↓
Documents are saved
        ↓
Documents are divided into chunks
        ↓
Chunks are converted into embeddings
        ↓
Embeddings are stored in the vector store
        ↓
User asks a question
        ↓
Question is converted into an embedding
        ↓
Relevant chunks are retrieved
        ↓
Retrieved chunks are reranked
        ↓
RAG generates an answer
        ↓
Answer + sources are displayed
```

## Project Structure

## Project Structure

```text
AI_Document_Search/
│
├── backend/
│   ├── app.py
│   └── static/
│       ├── style.css
│       └── script.js
│
├── data/
│   └── Text documents
│
├── src/
│   ├── embedding.py
│   ├── chunking.py
│   ├── chunks_embedding.py
│   ├── rag.py
│   ├── vector_store.py
│   ├── llm.py
│   ├── reranker.py
│   └── quer_rewriter.py
│
├── templates/
│   └── index.html
│
├── tests/
│
├── main.py
├── uploaded_documents.json
├── requirements.txt
├── .gitignore
└── README.md
```


## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI_Document_Search
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask application with:

```bash
python -m backend.app
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

Open this address in your browser.

## Using the Application

### Upload Documents

1. Select one or more `.txt` files.
2. Click **Upload**.
3. The documents are processed and added to the system.
4. Uploaded document names appear in the Documents List.

### Ask Questions

Enter a question about the uploaded documents and click **Ask**.

The system retrieves relevant information and displays:

* The generated answer
* Source document
* Chunk information
* Similarity score
* Reranking score
* Retrieved text

## Example

A user could upload a document containing information about Python and ask:

```text
What is Python used for?
```

The system searches the document collection based on semantic similarity and retrieves relevant information before generating the answer.

## Purpose

This project demonstrates the integration of:

* Python programming
* Data Structures and Algorithms
* Natural Language Processing
* Machine Learning
* Generative AI
* Retrieval-Augmented Generation
* Vector search
* Web development

The goal is to build a practical AI application that can search and answer questions from user-provided documents.

## Future Improvements

Possible future improvements include:

* Support for PDF and DOCX documents
* Document deletion
* Better duplicate-file handling
* User authentication
* Improved conversation management
* More advanced vector databases
* Additional LLM providers
* Deployment to a cloud platform
