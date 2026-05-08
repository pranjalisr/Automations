# 📂 Google Drive to Pinecone RAG Pipeline — n8n Workflow

An automated AI ingestion pipeline built with n8n that watches Google Drive for newly uploaded files, processes documents, generates OpenAI embeddings, and stores them inside a Pinecone vector database for Retrieval-Augmented Generation (RAG) systems.

This workflow enables fully automated knowledge base creation from documents stored in Google Drive.

## 🚀 Features

* 📁 Google Drive file monitoring
* ⚡ Automatic document ingestion
* 🧠 OpenAI embedding generation
* 🔎 Pinecone vector database storage
* ✂️ Recursive text chunking
* 📚 RAG-ready architecture
* 🤖 AI knowledge base automation
* 🔄 Real-time vector indexing

## 🏗 Workflow Overview

### 1️⃣ Google Drive Monitoring

The workflow automatically triggers whenever a new file is uploaded to Google Drive.

### 2️⃣ File Download

* The uploaded file is downloaded automatically.

### 3️⃣ Document Processing

* Default Data Loader extracts document content.
* Recursive Character Text Splitter breaks large documents into optimized chunks.

### 4️⃣ Embedding Generation

* OpenAI Embeddings convert text chunks into semantic vectors.

### 5️⃣ Pinecone Storage

* The embeddings are stored inside Pinecone Vector Store for future retrieval.

The indexed data can later power:

* AI chatbots
* RAG systems
* Semantic search engines
* Internal knowledge assistants

## 🧩 Nodes Used

* Google Drive Trigger
* Download File
* Default Data Loader
* Recursive Character Text Splitter
* OpenAI Embeddings
* Pinecone Vector Store

## 💡 Example Use Cases

* Automated RAG pipeline
* AI document search
* Internal company knowledge base
* Smart document indexing
* AI-powered file retrieval
* Customer support knowledge systems
* Research assistant infrastructure

## ⚙️ Tech Stack

* n8n
* Google Drive API
* OpenAI Embeddings
* Pinecone
* Vector Databases
* RAG Architecture

## 📸 Workflow Preview

This workflow automatically converts uploaded Google Drive documents into searchable semantic vectors stored inside Pinecone for AI-powered retrieval applications.


## 📝 License

MIT License

---

⭐ If you found this workflow useful, consider starring the repository and sharing it with the community.
