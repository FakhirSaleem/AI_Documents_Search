# Development Journey

This document describes how the **AI-Powered Semantic Document Search & Question Answering System** was developed.

The project was not built as a single application from the beginning. Development started with learning and experimenting with individual concepts such as text processing, search, ranking, embeddings, and NLP. After understanding these concepts, the useful components were gradually combined into a complete semantic search and question-answering application.

> **Important:** Not every file in the repository is a required component of the final application. Some files were created during the learning and experimentation stages to understand, test, or evaluate individual concepts.

---

## 1. Learning and Experimentation

Before building the complete application, individual concepts were explored separately.

The purpose of this stage was to understand **how the underlying technologies work**, rather than immediately building the final system.

Topics explored included:

* Reading and processing documents
* Text preprocessing
* Word and document analysis
* Basic search
* Ranking
* TF-IDF
* Semantic similarity
* Embeddings
* Natural Language Processing
* Document chunking
* Vector search
* Retrieval-Augmented Generation (RAG)

Some files created during this stage are therefore **experimental or educational files**. They may not be directly required when running the final web application.

Examples include:

* `src/word_analysis.py`
* `src/documents_analytics.py`
* `src/document_dataframe.py`
* `src/visualization.py`
* `src/evaluation.py`

These files represent part of the development and learning process rather than being treated as required production components.

---

# 2. Document Processing

The first practical part of the project was working with text documents.

The system needed to be able to read documents and prepare their contents for later search and retrieval.

### Concepts explored

* Reading `.txt` files
* Extracting text
* Cleaning and processing text
* Working with multiple documents
* Analyzing document contents

### Main component

`src/document_reader.py`

Other document-analysis files were also created during this stage for experimentation and understanding.

---

# 3. Basic Keyword Search

After learning how to process documents, a basic search mechanism was developed.

The initial approach relied on words appearing in the documents.

### Concepts explored

* Query processing
* Word matching
* Document relevance
* Basic ranking

### Main components

* `src/search.py`
* `src/ranking.py`

This stage provided the foundation for understanding why simple keyword matching can be useful but also has limitations.

For example, a keyword search may fail when a document contains a concept expressed using different words.

---

# 4. TF-IDF Search

The search system was then improved using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

TF-IDF provides a way to represent how important a word is within a document collection.

### Concepts explored

* Term frequency
* Inverse document frequency
* TF-IDF vectors
* Query-document similarity
* Relevance ranking

### Main component

`src/tfidf_search.py`

Evaluation-related experiments were also performed during this stage.

---

# 5. Semantic Search

The project then moved beyond exact keyword matching.

The goal became:

> **Find relevant information even when the exact words are different.**

Semantic search makes it possible to compare the meaning of text rather than relying only on exact word matches.

### Concepts explored

* Text embeddings
* Vector representations
* Semantic similarity
* Similarity-based retrieval

### Main components

* `src/embedding.py`
* `src/semantic_search.py`

This stage was important because semantic search became one of the central ideas behind the final application.

---

# 6. Hybrid Search

Different retrieval approaches were then explored together.

The project experimented with combining traditional text-based search with semantic search.

### Goal

Use the strengths of different retrieval methods instead of depending entirely on one approach.

### Main component

`src/hybrid_search.py`

This stage helped establish the idea of using multiple retrieval signals when determining document relevance.

---

# 7. Document Chunking

When the project moved toward question answering, working with entire documents was no longer sufficient.

Documents were divided into smaller sections called **chunks**.

### Why chunking was introduced

Instead of retrieving an entire document, the system could retrieve the specific section that was relevant to a user's question.

### Concepts explored

* Splitting documents into chunks
* Managing chunk metadata
* Searching individual chunks
* Preparing chunks for embeddings

### Main components

* `src/chunking.py`
* `src/chunk_search.py`

---

# 8. Chunk Embeddings

After creating chunks, embeddings were generated for the individual chunks.

This allowed the system to compare a user's question with specific sections of documents.

### Concepts explored

* Generating embeddings
* Embedding document chunks
* Comparing query and chunk vectors
* Semantic retrieval

### Main component

`src/chunks_embedding.py`

---

# 9. Vector Store

A vector store was introduced to keep the generated embeddings and associated information available for retrieval.

### Work completed

* Stored chunk embeddings
* Stored chunk information
* Performed similarity-based retrieval
* Reused existing vector data when documents had not changed

### Main component

`src/vector_store.py`

This became an important part of the final retrieval pipeline.

---

# 10. Retrieval-Augmented Generation (RAG)

The next major stage was implementing **Retrieval-Augmented Generation (RAG)**.

The basic idea is:

```text
User Question
      ↓
Retrieve Relevant Information
      ↓
Provide Retrieved Context
      ↓
Generate Answer
```

Instead of asking a language model to answer using only its general knowledge, the system first retrieves relevant information from the user's documents.

### Work completed

* Retrieved relevant document chunks
* Passed retrieved context to the question-answering system
* Generated answers using retrieved information
* Returned sources associated with the answer

### Main components

* `src/rag.py`
* `src/llm.py`

RAG became the core question-answering mechanism of the final application.

---

# 11. Reranking

The retrieval pipeline was further improved by introducing reranking.

The initial retrieval stage could return multiple candidate chunks. Reranking was used to further process these candidates and select the most relevant results.

### Main component

`src/reranker.py`

The final retrieval process therefore became more than simply finding the first matching documents.

---

# 12. Query Rewriting

Query rewriting was also explored as part of the retrieval pipeline.

The purpose was to transform or improve a user's query before retrieval so that relevant information could be found more effectively.

### Main component

`src/quer_rewriter.py`

This component was developed as part of improving the overall retrieval pipeline.

---

# 13. Building the Flask Backend

Once the core search and RAG functionality was working, the project was converted into a web application.

**Flask** was selected as the backend framework.

The Flask backend became the connection between the web interface and the existing Python search/RAG system.

### Work completed

* Created the Flask application
* Connected Flask to the RAG pipeline
* Created the question-answering endpoint
* Created the document upload endpoint
* Created the document listing endpoint
* Connected uploaded documents to the retrieval pipeline

### Main component

`backend/app.py`

---

# 14. Building the Web Interface

A browser-based interface was then created so that users could interact with the system without using the Python terminal.

The frontend uses:

* HTML
* CSS
* JavaScript

### Main components

* `templates/index.html`
* `backend/static/style.css`
* `backend/static/script.js`

### Interface functionality

The web interface allows users to:

* Enter questions
* Ask questions about the documents
* View generated answers
* View retrieved sources
* Upload `.txt` documents
* View uploaded documents
* Clear the current search

JavaScript communicates with the Flask backend using HTTP requests.

---

# 15. Document Upload System

The application was extended to allow users to upload their own text documents.

### Work completed

* Added multiple `.txt` file uploads
* Validated uploaded files
* Stored files in the `data/` directory
* Updated the document list
* Rebuilt/reinitialized the retrieval system when documents changed
* Added persistent tracking of uploaded document names

This turned the project from a fixed demonstration into a system that can work with user-provided documents.

---

# 16. End-to-End Integration

The individual components were eventually connected into one complete workflow.

### Search and RAG pipeline

```text
Text Documents
      ↓
Document Processing
      ↓
Chunking
      ↓
Embeddings
      ↓
Vector Store
      ↓
Semantic Retrieval
      ↓
Reranking
      ↓
RAG
      ↓
Answer + Sources
```

### Web application pipeline

```text
User
 ↓
Web Interface
 ↓
JavaScript
 ↓
Flask Backend
 ↓
Search / RAG Pipeline
 ↓
Answer + Sources
 ↓
Web Interface
```

The application was tested end-to-end with document uploading, retrieval, question answering, and source display.

---

# 17. Learning Files vs Application Files

An important distinction in this project is that the repository contains both **learning/experimental work** and **application components**.

### Learning and experimental work

These files were created primarily to understand, test, analyze, or experiment with individual concepts:

* `src/word_analysis.py`
* `src/documents_analytics.py`
* `src/document_dataframe.py`
* `src/visualization.py`
* `src/evaluation.py`

They are part of the development journey but are not necessarily required for the web application to run.

### Core application work

The following components are directly involved in the main application pipeline:

* `main.py`
* `src/document_reader.py`
* `src/text_processor.py`
* `src/search.py`
* `src/ranking.py`
* `src/tfidf_search.py`
* `src/semantic_search.py`
* `src/hybrid_search.py`
* `src/chunking.py`
* `src/chunk_search.py`
* `src/embedding.py`
* `src/chunks_embedding.py`
* `src/vector_store.py`
* `src/rag.py`
* `src/llm.py`
* `src/reranker.py`
* `src/quer_rewriter.py`
* `backend/app.py`
* `templates/index.html`
* `backend/static/style.css`
* `backend/static/script.js`

The exact role of individual components may overlap because some were first developed independently and later integrated into the final system.

---

# 18. From Learning to Application

The overall development process can be summarized as:

```text
Learn Concepts
      ↓
Experiment with Individual Techniques
      ↓
Build Small Components
      ↓
Test Search and Retrieval Methods
      ↓
Develop Semantic Retrieval
      ↓
Build RAG Pipeline
      ↓
Improve Retrieval
      ↓
Create Flask Backend
      ↓
Create Web Interface
      ↓
Add Document Upload
      ↓
Integrate Everything
      ↓
Test Complete Application
```

The project therefore represents both a **learning process** and the development of a working software application.

---

# 19. Current Status

The project currently provides a web-based system for searching and asking questions about uploaded text documents.

Major areas completed include:

* Document processing
* Keyword search
* TF-IDF search
* Semantic search
* Hybrid retrieval
* Document chunking
* Embeddings
* Vector storage
* RAG
* Reranking
* Query rewriting
* Flask backend
* HTML/CSS/JavaScript frontend
* Document uploading
* Source display
* End-to-end integration

Future development will continue through meaningful changes to the application, with new work recorded through Git commits.

---

## Development History Note

This document records the development journey based on the work completed during the project.

The repository's earlier work was developed before detailed Git history was maintained for every individual development stage. Therefore, this document is intended to explain the actual development process rather than recreate or claim historical Git commits that do not exist.

From this point forward, meaningful changes will be recorded through Git commits so that the ongoing development history is visible directly in the repository.
