#  Calendar Chatbot NLP

A simple chatbot built with Flask + NLP that can schedule and query calendar events using natural language. It supports both a RESTful API and a simple chat UI using Flask, SQLite, and NLP (via `dateparser`).

---

##  Features

- Add calendar events via chat using natural language
- Ask about events on specific dates
- Stores events using SQLite
- NLP for date & time recognition using `dateparser`
- RESTful API to access events (GET/POST)
- Simple Web Chat UI (Flask + HTML)

---

##  Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- dateparser (for NLP)
- spaCy (future NLP support)
- HTML (chat UI)
- Postman (for API testing)

---

##  Project Structure

calendar-chatbot-nlp/
|
|-- app.py    # Main Flask app
|-- models.py   # DB schema for events
|-- calendar_api.py   # API for GET/POST events
|-- chatbot.py   # Chatbot logic
|-- nlp_utils.py   # NLP utilities for date parsing
|-- requirements.txt
|
|-- templates/
|    |-- chat.html    # Frontend UI


##  Setup Instructions

### 1.  Clone the Repository

  VS Code Terminal ($Git Bash)

  git clone https://github.com/Priyapoojary11/calendar-chatbot-nlp.git
  cd calendar-chatbot-nlp

### 2. Create Virtual Environment

  python -m venv venv
  venv\Scripts\activate

### 3. Install Dependencies

  pip install -r requirements.txt

  If you run into issues with spaCy, run:
  - python -m spacy download en_core_web_sm

### 4. Run the App

  python app.py

### 5. Open URL in Browser

  http://127.0.0.1:5000/chat


### How to Use the Chatbot

Open the chat UI in your browser and try:

"Add event Team meeting on July 15 at 3 PM"

"Do I have anything scheduled this Friday?"

Bot will respond accordingly and save events in a local SQLite database.


# RESTful API Documentation

 ### POST /api/events

    - URL 
          POST http://127.0.0.1:5000/api/events

    - Headers
          Content-Type: application/json

    - Body(JSON)
          {
            "title": "Team Sync",
            "start": "2025-07-14T10:00:00",
            "end": "2025-07-14T11:00:00"
          }

    - Success Response
          {
            "status": "ok",
            "id": 1
          }
  ### GET /api/events

    - URL
        GET http://127.0.0.1:5000/api/events

    - Response
        [
          {
            "id": 1,
            "title": "Team Sync",
            "start": "2025-07-14T10:00:00",
            "end": "2025-07-14T11:00:00"
          }
        ]
