# 🤖 Telegram AI Productivity Assistant — n8n Automation

An AI-powered Telegram assistant built with n8n that supports text and voice conversations while integrating Gmail and Google Calendar automation.
This workflow acts as a personal productivity copilot capable of summarizing emails, sending messages, managing schedules, and responding intelligently inside Telegram.

## 🚀 Features

* 💬 Telegram AI chatbot
* 🎤 Voice message transcription
* 🧠 Conversational memory support
* 📧 Gmail integration

  * Email summaries
  * Send emails directly
* 📅 Google Calendar integration

  * Create calendar events
  * Fetch schedules/events
* 🤖 OpenAI-powered AI Agent
* 🔀 Automatic handling of text and audio inputs
* ⚡ Real-time conversational automation

## 🏗 Workflow Overview

1. A user sends a text or voice message on Telegram.
2. The workflow detects the message type using a Switch node.
3. For voice inputs:

   * The audio file is downloaded
   * OpenAI transcription converts speech to text
4. The input is passed to the AI Agent.
5. The AI Agent uses:

   * OpenAI Chat Model
   * Simple Memory
   * Gmail tools
   * Google Calendar tools
6. Based on user requests, the AI can:

   * Summarize Gmail messages
   * Send emails
   * Create calendar events
   * Fetch calendar schedules
7. The final response is sent back to Telegram.

## 🧩 Nodes Used

* Telegram Trigger
* Switch
* Edit Fields
* Get File
* OpenAI Transcription
* AI Agent
* OpenAI Chat Model
* Simple Memory
* Gmail Summary
* Gmail Send Message
* Google Calendar Create Event
* Google Calendar Get Events
* Telegram Send Message

## 💡 Example Use Cases

* Personal AI assistant
* Telegram productivity bot
* Voice-enabled scheduling assistant
* AI email management
* Smart calendar automation
* Daily productivity copilot
* AI executive assistant

## ⚙️ Tech Stack

* n8n
* Telegram Bot API
* OpenAI
* Gmail API
* Google Calendar API
* AI Agents
* Whisper Transcription
* Memory Nodes

## 📸 Workflow Preview

This workflow combines conversational AI, voice transcription, email automation, and calendar management into a single Telegram-based assistant.

## 🔧 Customization Ideas

* Add Notion or Slack integration
* Add Pinecone vector memory
* Enable AI task reminders
* Add multi-language support
* Connect Google Tasks/Todoist
* Add weather/news tools
* Add document summarization

## 📌 Future Improvements

* Long-term memory storage
* Autonomous AI scheduling
* Voice reply generation
* Smart task planning
* RAG-based personal knowledge assistant
* Multi-agent collaboration

## 📝 License

MIT License

---

⭐ If you found this workflow useful, consider starring the repository and sharing it with the community.
