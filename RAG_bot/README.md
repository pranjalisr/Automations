# 🤖 RAG Chatbot with Pinecone — n8n Workflow

An AI-powered Retrieval-Augmented Generation (RAG) chatbot built with n8n using OpenAI and Pinecone Vector Store.
This workflow enables intelligent conversational AI that retrieves relevant information from a vector database before generating responses.

The chatbot combines semantic search, conversational memory, and AI reasoning to provide context-aware answers from custom knowledge sources.

## 🚀 Features

* 💬 AI-powered chat interface
* 🧠 Retrieval-Augmented Generation (RAG)
* 🔎 Pinecone vector database integration
* 🤖 OpenAI Chat Model support
* 📚 Semantic document retrieval
* 🧩 OpenAI embeddings integration
* 🗂 Context-aware responses
* 🛠 Conversational memory support
* ⚡ Real-time vector search

## 🏗 Workflow Overview

1. A user sends a chat message.
2. The AI Agent receives the query.
3. The agent uses:

   * OpenAI Chat Model for reasoning
   * Simple Memory for maintaining conversation history
   * Pinecone Vector Store for semantic retrieval
4. Relevant knowledge chunks are fetched from Pinecone.
5. The AI combines retrieved context with the user query.
6. A grounded and context-aware response is generated.

## 🧩 Nodes Used

* When Chat Message Received
* AI Agent
* OpenAI Chat Model
* Simple Memory
* Answer Questions with Vector Store
* Pinecone Vector Store
* OpenAI Embeddings

## 💡 Example Use Cases

* AI knowledge base chatbot
* Customer support assistant
* Internal documentation assistant
* FAQ retrieval bot
* Research assistant
* AI learning assistant
* Company knowledge search
* Semantic Q&A system

## ⚙️ Tech Stack

* n8n
* OpenAI
* Pinecone
* OpenAI Embeddings
* Vector Databases
* AI Agents
* RAG Architecture

## 📸 Workflow Preview

This workflow demonstrates a complete RAG pipeline where conversational AI retrieves relevant context from Pinecone before generating intelligent responses.


## 📝 License

MIT License

---

⭐ If you found this workflow useful, consider starring the repository and sharing it with the community.
