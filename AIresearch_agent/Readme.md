# 🔎 AI Research Agent — n8n Automation

An AI-powered research assistant built with n8n that combines OpenAI reasoning with real-time search, Wikipedia knowledge retrieval, and Hacker News data.
This workflow is designed as a reusable sub-workflow that can be triggered by other automations for intelligent information retrieval and research tasks.

## 🚀 Features

* 🤖 OpenAI-powered AI Agent
* 🌐 Real-time web search using SerpAPI
* 📚 Wikipedia knowledge retrieval
* 📰 Hacker News integration
* 🔄 Executable as a reusable sub-workflow
* ⚡ Intelligent tool-calling agent architecture
* 🧠 Multi-source information gathering
* 🛠 Modular and extensible workflow design

## 🏗 Workflow Overview

1. The workflow is triggered by another n8n workflow.
2. The AI Agent receives the input query.
3. The agent uses:

   * OpenAI Chat Model for reasoning
   * Wikipedia for factual knowledge
   * SerpAPI for live web search
   * Hacker News for trending tech discussions
4. Information from multiple sources is analyzed and combined.
5. The workflow returns an AI-generated research response.

## 🧩 Nodes Used

* When Executed by Another Workflow
* AI Agent
* OpenAI Chat Model
* Wikipedia Tool
* Hacker News Tool
* SerpAPI Search Tool

## 💡 Example Use Cases

* AI research assistant
* Tech news aggregation
* Real-time information retrieval
* Startup and product research
* Developer news assistant
* AI-powered search workflows
* Knowledge augmentation for agents
* RAG-style automation systems

## ⚙️ Tech Stack

* n8n
* OpenAI
* SerpAPI
* Wikipedia API
* Hacker News API
* AI Agents

## 📸 Workflow Preview

This workflow acts as a modular AI research engine capable of combining web search, encyclopedic knowledge, and trending developer news into a single intelligent response pipeline.

## 🔧 Customization Ideas

* Add memory support
* Connect vector databases like Pinecone
* Add PDF/document search
* Integrate Google News or Reddit
* Add source citations
* Build multi-agent research systems
* Add summarization pipelines

## 📌 Future Improvements

* Long-term memory integration
* Multi-step reasoning chains
* Semantic vector retrieval


## 📝 License

MIT License

---

⭐ If you found this workflow useful, consider starring the repository and sharing it with the community.
