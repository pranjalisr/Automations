# 🤖 MCP AI Assistant — n8n Automation

An intelligent MCP-powered AI assistant built with n8n that connects productivity tools, vector search, spreadsheets, email, and calendar operations into a single automated workflow.

This workflow acts as a centralized AI operations assistant capable of reading data, storing context, scheduling events, sending emails, and interacting with vector databases using MCP architecture.

## 🚀 Features

* 🧠 MCP Server-based AI orchestration
* 📅 Google Calendar integration
* 📧 Gmail automation
* 📊 Google Sheets read/write support
* 🔎 Pinecone vector database integration
* 🔗 OpenAI embeddings support
* ➕ Spreadsheet row appending
* 🧮 Built-in calculator tool
* ⚡ Modular AI tool calling workflow

## 🏗 Workflow Overview

The workflow starts with an MCP Server Trigger that acts as the central orchestrator.

The AI assistant can dynamically use multiple connected tools:

* Create Google Calendar events
* Fetch calendar schedules
* Read data from Google Sheets
* Append rows into sheets
* Send Gmail messages
* Perform calculations
* Store and retrieve vector embeddings using Pinecone

OpenAI embeddings are used for semantic vector operations inside the Pinecone Vector Store.

## 🧩 Connected Tools

### 📅 Google Calendar

* Create events
* Fetch upcoming events
* Manage schedules

### 📊 Google Sheets

* Read spreadsheet rows
* Append new entries
* Use sheets as lightweight databases

### 📧 Gmail

* Send automated emails
* Trigger communication workflows

### 🔎 Pinecone Vector Store

* Semantic search
* AI memory/context storage
* Retrieval-augmented workflows

### 🧠 OpenAI Embeddings

* Generate embeddings for vector search
* Improve contextual AI retrieval

### 🧮 Calculator

* Perform mathematical computations dynamically

## 💡 Example Use Cases

* AI productivity assistant
* Smart scheduling system
* Automated CRM workflows
* AI-powered spreadsheet assistant
* Semantic document retrieval
* AI operations dashboard
* Personal executive assistant
* Business process automation

## ⚙️ Tech Stack

* n8n
* MCP Architecture
* OpenAI
* Pinecone
* Google Calendar API
* Google Sheets API
* Gmail API

## 📸 Workflow Preview

This automation demonstrates how MCP servers can coordinate multiple AI tools and external services inside a unified workflow architecture.

## 🔧 Customization Ideas

* Add Slack/Discord integrations
* Connect Notion or Airtable
* Add AI memory persistence
* Build RAG-based assistants
* Add authentication layer
* Integrate voice commands
* Add multi-agent orchestration

## 📌 Future Improvements

* Long-term conversational memory
* Autonomous AI task execution
* Multi-user support
* Knowledge base synchronization
* Real-time notifications
* AI analytics dashboard

## 📝 License

MIT License

---

⭐ If you found this workflow useful, consider starring the repository and sharing it with the community.
