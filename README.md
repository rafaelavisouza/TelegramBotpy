# Telegram Bot with Python 🤖

A modular and interactive Telegram Bot built with Python. This project was developed to automate interactions, process user inputs, and manage user-specific data using JSON files.

## 📌 Project Overview

This repository contains the source code for a custom Telegram Bot. The architecture is modularized to separate the core bot logic, API integration, data processing, and user data management. 

Key features include:
* **Automated Interaction:** Handles incoming messages and replies based on custom logic.
* **Input Recognition:** Processes user inputs for specific commands or patterns (handled in `reconhecimento.py`).
* **Local Data Storage:** Uses `.json` files to store and retrieve specific user data and states.

## 📁 Repository Structure

* `main.py`: The entry point of the application.
* `telegram.py` / `chatbot.py`: Core logic for the Telegram API integration and message handling.
* `reconhecimento.py`: Module dedicated to input processing and recognition.
* `funcoes.py`: Helper functions and utilities to keep the code DRY (Don't Repeat Yourself).
* `*.json`: User-specific data storage (e.g., `Felipe.json`, `Vitoriamar.json`).

## 🚀 Technologies Used
* Python 3.x
* telepot (Telegram Bot API framework)
* JSON module for data manipulation

