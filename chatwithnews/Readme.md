



# 📰 Chat With News — n8n AI Automation

An AI-powered news assistant built with n8n that lets users chat with live news sources in real time.
This workflow combines OpenAI Agents, memory, and multiple RSS feeds to create an interactive conversational news experience.

## 🚀 Features

* 💬 Chat-based news interaction
* 🤖 AI Agent powered by OpenAI
* 🧠 Memory support for contextual conversations
* 🌍 Fetches latest updates from:

  * BBC News
  * The Verge
  * Hacker News
* ⚡ Real-time RSS feed integration
* 🔄 Multi-source news aggregation
* 🛠 Fully customizable inside n8n

## 🏗 Workflow Overview

The workflow works as follows:

1. A user sends a chat message.
2. The AI Agent receives the query.
3. The agent uses:

   * OpenAI Model for reasoning and responses
   * Simple Memory for conversation history
   * RSS tools for fetching live news
4. The AI analyzes articles from multiple news sources.
5. A summarized and conversational response is returned to the user.

## 🧩 Nodes Used

* **When Chat Message Received**
* **AI Agent**
* **OpenAI Model**
* **Simple Memory**
* **RSS Feed Reader (BBC News)**
* **RSS Feed Reader (The Verge)**
* **RSS Feed Reader (Hacker News)**

## 💡 Example Use Cases

* “What are today’s top AI headlines?”
* “Summarize the latest tech news.”
* “What’s trending on Hacker News?”
* “Compare BBC and The Verge coverage on AI.”
* “Give me startup news from today.”

## ⚙️ Tech Stack

* n8n
* OpenAI
* RSS Feeds
* AI Agent Tools
* Memory Nodes

## 📸 Workflow Preview

This automation connects multiple RSS news sources directly to an AI agent for intelligent news conversations.

## 🔧 Customization Ideas

* Add more RSS feeds
* Connect Telegram/Discord/Slack
* Add sentiment analysis
* Save news history to database
* Generate daily AI news digests
* Add multilingual support

## 📌 Future Improvements

* Vector database memory
* Personalized news recommendations
* Voice-based news assistant
* Topic-specific filtering
* AI-generated newsletters

## 📝 License

MIT License

---

⭐ If you found this useful, consider starring the repository and sharing it with others.
