<img width="1177" height="562" alt="Screenshot 2026-05-09 at 00 20 33" src="https://github.com/user-attachments/assets/cf740c38-9fef-464a-8aa7-142ffd2520cb" />


# 🤖 Google Drive RAG Chatbot Pipeline — n8n Workflow

An AI-powered RAG (Retrieval-Augmented Generation) pipeline built with n8n that automatically converts documents from Google Drive into a searchable knowledge base using OpenAI embeddings and Pinecone Vector Store.

This workflow acts as the backend ingestion system for a RAG chatbot, enabling AI assistants to answer questions using custom uploaded documents.

## 🚀 Features

* 📂 Automatic Google Drive file monitoring
* 📄 Document ingestion and processing
* ✂️ Intelligent text chunking
* 🧠 OpenAI embedding generation
* 🔎 Pinecone vector database integration
* 🤖 RAG chatbot backend pipeline
* ⚡ Real-time knowledge base updates
* 📚 Semantic search-ready architecture

## 🏗 Workflow Overview

### 1️⃣ Google Drive Trigger

The workflow automatically starts whenever a new file is uploaded to Google Drive.

### 2️⃣ File Processing

* Downloads the uploaded file
* Extracts document content using the Default Data Loader

### 3️⃣ Text Chunking

* Recursive Character Text Splitter breaks documents into optimized chunks for retrieval accuracy

### 4️⃣ Embedding Generation

* OpenAI Embeddings convert text chunks into semantic vectors

### 5️⃣ Pinecone Vector Storage

* The generated embeddings are stored in Pinecone Vector Store

The indexed data can then be used by a RAG chatbot to:

* Answer questions from uploaded documents
* Retrieve contextual knowledge
* Generate grounded AI responses

## 🧩 Nodes Used

* Google Drive Trigger
* Download File
* Default Data Loader
* Recursive Character Text Splitter
* OpenAI Embeddings
* Pinecone Vector Store

## 💡 Example Use Cases

* RAG chatbot backend
* AI document assistant
* Knowledge base chatbot
* PDF Q&A system
* Internal documentation search
* AI learning assistant
* Customer support knowledge retrieval
* Research document chatbot

## ⚙️ Tech Stack

* n8n
* Google Drive API
* OpenAI Embeddings
* Pinecone
* Vector Databases
* RAG Architecture

## 📸 Workflow Preview

This workflow automatically transforms uploaded Google Drive documents into searchable embeddings that power intelligent RAG chatbot conversations.


## 📝 License

MIT License

---

⭐ If you found this workflow useful, consider starring the repository and sharing it with the community.
