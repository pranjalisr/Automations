# 📧 AI Mail Agent with Pinecone — n8n Workflow

An AI-powered mail assistant built with n8n that can answer questions using a Pinecone vector store and send emails through an automated mail tool.

This workflow combines conversational AI, vector-based knowledge retrieval, OpenAI embeddings, and email automation into one intelligent assistant.

## 🚀 Features

* 💬 Chat-based AI mail assistant
* 🤖 OpenAI-powered AI Agent
* 🔎 Pinecone vector store retrieval
* 🧠 Answers questions from stored knowledge
* 🧩 OpenAI embeddings support
* 📧 Automated email sending
* ⚡ Tool-calling agent architecture
* 🛠 Modular and customizable setup

## 🏗 Workflow Overview

1. A chat message is received.
2. The message is passed to the AI Agent.
3. The AI Agent uses:

   * OpenAI Chat Model for reasoning
   * Pinecone Vector Store for knowledge retrieval
   * OpenAI Embeddings for semantic search
   * Mail tool for sending emails
4. The agent searches relevant context from Pinecone.
5. It generates an accurate response or sends an email when requested.

## 🧩 Nodes Used

* When Chat Message Received
* AI Agent
* OpenAI Chat Model
* Pinecone Vector Store
* OpenAI Embeddings
* Vector Store Question Answering Tool
* Send Mail Tool

## 💡 Example Use Cases

* AI email assistant
* RAG-based mail agent
* Knowledge-base Q&A assistant
* Customer support email automation
* Internal company FAQ bot
* Smart email drafting assistant
* Lead response assistant

## ⚙️ Tech Stack

* n8n
* OpenAI
* Pinecone
* OpenAI Embeddings
* AI Agents
* Email automation


## 📝 License

MIT License

---

⭐ If you found this useful, consider starring the repository.
