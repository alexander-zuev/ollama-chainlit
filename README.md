# 🌐 **Ollama Chainlit Chatbot**

This project is a **locally-run chatbot** built with **Chainlit**, **LangChain**, and the **Ollama Llama 3.1 model**. It supports real-time **streaming responses** and **conversation history**, providing an intelligent, context-aware conversation experience—all on your local machine. 🖥️

## 🚀 **Features**
- **Locally run**: No external services required, everything runs on your machine.
- ⚡ **Streaming responses**: Token-by-token responses for faster, more interactive chats.
- 💬 **Conversation history**: The bot remembers your previous messages for more coherent replies.

## ⚙️ **Setup**

1. **Install dependencies**:
   ```bash
   poetry install
   ```

2. **Start Ollama**:
   Make sure you have the Ollama model ready to serve:
   ```bash
   ollama pull llama3.1:8b
   ollama serve
   ```

3. **Run the Chainlit app**:
   ```bash
   poetry run chainlit run app.py
   ```

4. **Access the chatbot**:
   Visit `http://localhost:8000` in your browser to start chatting with the bot. 🌍

## 🛠️ **Technologies Used**
- **Chainlit** for the user interface.
- **LangChain** to handle conversation logic and memory.
- **Ollama Llama 3.1** as the language model backend.

## 🎯 **Purpose**
This chatbot is ideal for testing and running advanced LLM models locally, offering real-time feedback and the ability to maintain conversation context. Perfect for experimenting with **LLMs** and **local AI solutions** without relying on cloud-based services.