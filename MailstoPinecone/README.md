<img width="1308" height="562" alt="Screenshot 2026-05-09 at 00 01 58" src="https://github.com/user-attachments/assets/1a489139-77e4-409b-b00b-bdd904f295b3" />


# 📩 Gmail to Pinecone Vector Store — n8n Workflow

An AI-powered document ingestion workflow built with n8n that extracts content from documents and stores semantic embeddings inside a Pinecone vector database using OpenAI embeddings.

This workflow is designed for building searchable AI knowledge bases, RAG pipelines, and intelligent retrieval systems from Gmail attachments or imported documents.

## 🚀 Features

* 📄 Document ingestion pipeline
* 🧠 OpenAI embedding generation
* 🔎 Pinecone vector database storage
* ⚡ Semantic search-ready architecture
* 🛠 AI knowledge base creation
* 📚 Automatic document vectorization
* 🔗 RAG-ready workflow setup
* 🤖 AI retrieval infrastructure

## 🏗 Workflow Overview

1. The workflow starts manually when executed.
2. A document is fetched using the document node.
3. The document content is processed through the Default Data Loader.
4. OpenAI Embeddings generate vector representations of the document text.
5. The embeddings are stored inside Pinecone Vector Store.
6. The stored vectors can later be used for:

   * AI chatbots
   * Semantic search
   * RAG applications
   * Knowledge retrieval systems

## 🧩 Nodes Used

* Manual Trigger
* Get Document
* Default Data Loader
* OpenAI Embeddings
* Pinecone Vector Store

## 💡 Example Use Cases

* AI knowledge base creation
* RAG (Retrieval-Augmented Generation) systems
* Semantic document search
* Gmail attachment indexing
* Internal company documentation search
* AI customer support assistants
* Research document retrieval

## ⚙️ Tech Stack

* n8n
* OpenAI Embeddings
* Pinecone
* Vector Databases
* AI Retrieval Systems

## 📸 Workflow Preview

This workflow creates a semantic vector pipeline that converts documents into searchable embeddings stored inside Pinecone for AI-powered retrieval applications.

## 📝 License

MIT License

---

⭐ If you found this workflow useful, consider starring the repository and sharing it with the community.
