# 🤖 Telegram AI Assistant — n8n Automation

An AI-powered Telegram assistant built with n8n that supports both text and voice conversations using OpenAI.
The workflow intelligently detects message types, transcribes audio messages, maintains conversational memory, and responds directly inside Telegram.

## 🚀 Features

* 💬 Telegram chatbot integration
* 🎤 Voice message transcription
* 🧠 Conversational AI with memory
* 🤖 OpenAI-powered responses
* 🔀 Automatic routing for text and audio
* 📨 Sends AI-generated replies back to Telegram
* ⚡ Real-time message processing
* 🛠 Modular and extensible workflow

## 🏗 Workflow Overview

1. A message is received through the Telegram Trigger.
2. The workflow uses a Switch node to detect:

   * Text messages
   * Audio/voice messages
3. For voice messages:

   * The file is fetched from Telegram
   * OpenAI transcription converts speech to text
4. The processed input is sent to the AI Agent.
5. The AI Agent uses:

   * OpenAI Chat Model
   * Simple Memory for context retention
   * Additional sub-workflows/tools
6. The AI-generated response is sent back to Telegram automatically.

## 🧩 Nodes Used

* Telegram Trigger
* Switch
* Edit Fields
* Get File
* OpenAI Transcription
* AI Agent
* OpenAI Chat Model
* Simple Memory
* Telegram Send Message

## 💡 Example Use Cases

* AI personal assistant on Telegram
* Voice-enabled chatbot
* Customer support automation
* AI Q&A assistant
* Productivity assistant
* Multimodal conversational AI

## ⚙️ Tech Stack

* n8n
* Telegram Bot API
* OpenAI
* Whisper / Audio Transcription
* AI Agents
* Memory Nodes

## 📸 Workflow Preview

This workflow enables seamless AI conversations on Telegram with support for both typed and spoken interactions.

## 🔧 Customization Ideas

* Add image understanding
* Connect Google Calendar or Gmail
* Add Pinecone vector memory
* Support multiple languages
* Add sentiment analysis
* Connect databases or CRMs
* Add tool-calling agents

## 📌 Future Improvements

* Long-term AI memory
* Voice response generation
* RAG-based knowledge assistant
* Multi-user personalization
* Autonomous task execution
* Smart workflow chaining

## 📝 License

MIT License

---

⭐ If you found this workflow useful, consider starring the repository and sharing it with the community.
