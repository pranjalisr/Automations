# 🤖 n8n AI Agents

> A growing collection of production-ready, AI-powered n8n workflows for real-world automation — covering email, messaging, research, RAG pipelines, job search, and more.

---

## 📌 About

This repository is a personal library of **n8n automation workflows** built using AI agents, LLMs, webhooks, vector databases, and third-party API integrations. Each workflow is self-contained, importable directly into n8n, and designed to solve a specific real-world use case.

Whether you want to automate your Gmail inbox, build a RAG chatbot over your documents, or set up a Telegram AI assistant — this repo has a ready-to-use workflow for you.

---

## 📁 Repository Structure

```
n8n-AI-Agents/
│
├── AI_research_agent/         # Autonomous AI research agent
├── FormResponse/              # AI-powered form response handler
├── Gmail_Assistant/           # Smart Gmail inbox automation
├── JobSearch/                 # Automated AI job search pipeline
├── MCP_Assistant/             # Model Context Protocol AI assistant
├── MailstoPinecone/           # Email ingestion into Pinecone vector DB
├── PineconeMailAgent/         # RAG agent over email data in Pinecone
├── Productivity_assistant/    # Personal productivity automation
├── RAG_bot/                   # RAG bot with vector store integration
├── RAG_chatbot/               # Conversational RAG chatbot
├── SponsorReply/              # Auto-reply for sponsorship emails
├── TelegramChatbot/           # AI chatbot via Telegram
├── Telegram_assistant/        # Full-featured Telegram AI assistant
├── chatwithnews/              # Chat with live news using AI
└── whatsappAI_assistant/      # WhatsApp AI assistant via webhook
```

---

## 🔧 Workflows

### 1. 🔍 AI Research Agent — `AI_research_agent/`
An autonomous AI agent that performs multi-step research tasks. Given a topic or query, it searches the web, summarizes findings, and returns structured results — all without manual intervention.

**Use case:** Automated research reports, competitive analysis, topic deep-dives.

---

### 2. 📋 Form Response Handler — `FormResponse/`
Processes form submissions using an AI agent that classifies, interprets, and routes responses. Automatically categorizes incoming form data and triggers appropriate follow-up actions.

**Use case:** Lead forms, feedback forms, survey automation.

---

### 3. 📧 Gmail Assistant — `Gmail_Assistant/`
An intelligent Gmail automation that reads incoming emails, classifies them (e.g. client, sponsor, newsletter), and sends appropriate AI-generated replies or labels them automatically.

**Use case:** Inbox zero automation, email triage, auto-replies.

---

### 4. 💼 Job Search Agent — `JobSearch/`
Automates job searching by scraping or querying job boards, filtering results based on custom criteria, and delivering curated job listings directly to you.

**Use case:** Automated daily job alerts, job filtering by skill/role/location.

---

### 5. 🧠 MCP Assistant — `MCP_Assistant/`
An AI assistant built on the **Model Context Protocol (MCP)**, enabling tool-augmented interactions. The assistant can call external tools and APIs dynamically based on user queries.

**Use case:** Tool-using AI assistants, agentic task execution with MCP servers.

---

### 6. 📬 Mails to Pinecone — `MailstoPinecone/`
A data pipeline that ingests emails, generates vector embeddings, and stores them in **Pinecone** vector database. Enables semantic search and retrieval over your email history.

**Use case:** Email knowledge base, semantic email search, building RAG-ready data.

---

### 7. 🗂️ Pinecone Mail Agent — `PineconeMailAgent/`
A RAG-powered agent that queries the Pinecone email vector store to answer user questions based on past email content. Works in tandem with the `MailstoPinecone` pipeline.

**Use case:** "Find all emails about X", intelligent email assistant with memory.

---

### 8. ✅ Productivity Assistant — `Productivity_assistant/`
A personal productivity automation that helps manage tasks, calendar events, and daily planning using AI. Can integrate with tools like Google Calendar, Notion, or task managers.

**Use case:** Daily briefings, task management, smart scheduling.

---

### 9. 🤖 RAG Bot — `RAG_bot/`
A Retrieval-Augmented Generation bot that connects to a vector store (e.g. Pinecone, Qdrant) and answers questions using your own documents as the knowledge source.

**Use case:** Document Q&A, internal knowledge bots, PDF chatbots.

---

### 10. 💬 RAG Chatbot — `RAG_chatbot/`
A conversational chatbot built on RAG architecture, designed for interactive multi-turn dialogue over a custom document corpus. Maintains conversation context across messages.

**Use case:** Customer support bots, knowledge-base assistants, document chat.

---

### 11. 💌 Sponsor Reply — `SponsorReply/`
Automatically detects incoming sponsorship or collaboration request emails and sends a personalized, AI-generated reply based on predefined templates or dynamic content.

**Use case:** Content creator inbox management, auto-response for sponsorship DMs/emails.

---

### 12. 📱 Telegram Chatbot — `TelegramChatbot/`
A simple but powerful AI chatbot connected to Telegram via bot API. Responds to user messages in real-time using an LLM backend.

**Use case:** Quick AI chat interface over Telegram, personal bot assistant.

---

### 13. 🤖 Telegram Assistant — `Telegram_assistant/`
A full-featured AI assistant delivered via Telegram. Goes beyond basic chat — can handle commands, perform web actions, manage tasks, and call external tools on behalf of the user.

**Use case:** All-in-one personal assistant on Telegram, multi-tool agentic bot.

---

### 14. 📰 Chat with News — `chatwithnews/`
Fetches the latest news articles, processes them with AI, and enables conversational interaction with current headlines. Users can ask questions about ongoing events and get AI-summarized answers.

**Use case:** News digest assistant, real-time Q&A over live news content.

---

### 15. 📲 WhatsApp AI Assistant — `whatsappAI_assistant/`
An AI assistant integrated with WhatsApp via webhook. Receives messages from WhatsApp, processes them through an AI agent, and sends intelligent replies back.

**Use case:** WhatsApp customer support bot, personal AI assistant on WhatsApp.

---

## 🚀 Getting Started

### Prerequisites

- [n8n](https://n8n.io) installed (self-hosted or cloud)
  - Self-host via Docker: `docker run -it --rm -p 5678:5678 n8nio/n8n`
  - Or use [n8n Cloud](https://app.n8n.cloud)
- API keys for relevant services (OpenAI, Pinecone, Telegram, etc.)

### How to Import a Workflow

1. **Clone this repository**
   ```bash
   git clone https://github.com/pranjalisr/n8n-AI-Agents.git
   cd n8n-AI-Agents
   ```

2. **Open your n8n instance** in the browser (default: `http://localhost:5678`)

3. **Import the workflow**
   - Go to **Workflows** → **Import from file**
   - Select the `.json` file from the desired workflow folder

4. **Configure credentials**
   - Go to **Settings** → **Credentials**
   - Add the required API keys (OpenAI, Gmail, Telegram Bot Token, Pinecone, etc.)

5. **Activate and run**
   - Enable the workflow toggle
   - Trigger manually or let it run on its schedule/webhook

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Automation Platform** | n8n |
| **AI / LLMs** | OpenAI (GPT-4), LangChain, AI Agents |
| **Vector Databases** | Pinecone |
| **Messaging** | Telegram Bot API, WhatsApp (via Webhook) |
| **Email** | Gmail API |
| **Protocols** | MCP (Model Context Protocol), Webhooks, REST APIs |
| **Data Pipelines** | RAG (Retrieval-Augmented Generation) |

---

## 📋 Credential Requirements by Workflow

| Workflow | Required Credentials |
|---|---|
| AI_research_agent | OpenAI API Key |
| FormResponse | OpenAI API Key |
| Gmail_Assistant | Gmail OAuth2, OpenAI API Key |
| JobSearch | OpenAI API Key, Job Board API (optional) |
| MCP_Assistant | OpenAI API Key, MCP Server URL |
| MailstoPinecone | Gmail OAuth2, Pinecone API Key, OpenAI API Key |
| PineconeMailAgent | Pinecone API Key, OpenAI API Key |
| Productivity_assistant | OpenAI API Key, Google Calendar OAuth2 (optional) |
| RAG_bot | Pinecone API Key, OpenAI API Key |
| RAG_chatbot | Pinecone API Key, OpenAI API Key |
| SponsorReply | Gmail OAuth2, OpenAI API Key |
| TelegramChatbot | Telegram Bot Token, OpenAI API Key |
| Telegram_assistant | Telegram Bot Token, OpenAI API Key |
| chatwithnews | OpenAI API Key, News API Key (optional) |
| whatsappAI_assistant | WhatsApp Webhook, OpenAI API Key |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👩‍💻 Author

**Pranjali Srivastava**

Built with ❤️ using n8n, AI agents, and a love for automation.

- GitHub: [@pranjalisr](https://github.com/pranjalisr)

---

> ⭐ If you find this useful, consider starring the repo — it helps others discover it!
