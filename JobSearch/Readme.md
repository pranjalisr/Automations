# 🤖 AI Job Search & Resume Matching Automation — n8n Workflow

An AI-powered job discovery and resume matching automation built with n8n that automatically searches LinkedIn jobs, analyzes resumes, evaluates job relevance using AI, updates Google Sheets, and sends personalized email notifications.

This workflow acts as a fully automated AI job hunting assistant for tracking and filtering relevant opportunities.

## 🚀 Features

* 📄 Resume PDF parsing
* 🔍 Automated LinkedIn job search
* 🤖 AI-powered job relevance analysis
* 📊 Google Sheets integration
* 📧 Automated email notifications
* 🧠 Gemini-powered AI evaluation
* 🔄 Scheduled recurring automation
* ⚡ End-to-end job tracking pipeline

## 🏗 Workflow Overview

### 1️⃣ Scheduled Trigger

The workflow starts automatically on a schedule.

### 2️⃣ Resume Processing

* Downloads a resume file from Google Drive
* Extracts resume text from PDF
* Reads job preferences/keywords from Google Sheets

### 3️⃣ LinkedIn Job Search

* Dynamically generates LinkedIn search URLs
* Fetches job listings from LinkedIn
* Extracts job details from HTML pages
* Splits jobs into individual records

### 4️⃣ AI Job Analysis

Using Google Gemini AI:

* Evaluates job relevance
* Matches skills against the resume
* Filters high-quality opportunities
* Scores or summarizes job suitability

### 5️⃣ Data Storage

* Appends or updates job entries in Google Sheets
* Maintains structured tracking data

### 6️⃣ Notification System

* Loops through selected jobs
* Sends automated email notifications via Gmail

## 🧩 Nodes Used

* Schedule Trigger
* Google Drive Download File
* Extract From PDF
* Google Sheets Read Rows
* LinkedIn Search URL Generator
* HTTP Request
* HTML Extraction
* Split Out
* AI Agent (Gemini)
* Edit Fields
* Append or Update Row
* Loop Over Items
* Gmail Send Message
* Wait Node

## 💡 Example Use Cases

* AI-powered job hunting assistant
* Internship/job tracking automation
* Resume-job matching system
* Automated LinkedIn scraper workflow
* Personalized opportunity alerts
* Career search automation
* Daily AI job digest system

## ⚙️ Tech Stack

* n8n
* Google Gemini AI
* LinkedIn Search
* Google Sheets API
* Gmail API
* Google Drive API
* HTML Parsing
* PDF Extraction

## 📸 Workflow Preview

This workflow automates the entire job search pipeline — from extracting resume skills to discovering relevant jobs and sending intelligent AI-filtered notifications.

## 🔧 Customization Ideas

* Add ATS score analysis
* Connect Notion or Airtable
* Add Telegram/Discord notifications
* Use OpenAI instead of Gemini
* Add multi-platform job search
* Include salary filtering
* Add vector database memory
* Generate AI-tailored resumes

## 📌 Future Improvements

* AI-generated cover letters
* Interview preparation assistant
* Personalized career analytics
* Semantic resume matching
* Multi-agent hiring assistant
* Real-time job monitoring

## 📝 License

MIT License

---

⭐ If you found this workflow useful, consider starring the repository and sharing it with the community.
