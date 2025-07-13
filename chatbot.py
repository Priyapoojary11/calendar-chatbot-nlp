from flask import Blueprint, request, render_template, jsonify
from nlp_utils import extract_datetime
from models import Event, db
from dateutil import parser
from datetime import datetime
import re


chat_bp = Blueprint('chat', __name__)

def extract_event_title(message, date_matches):
    text = message.lower()
    text = re.sub(r"(add|schedule|create)( an| a)? (event|meeting|call|lunch)?", '', text)
    for dt in date_matches:
        
        # Remove date components from the text
        text = text.replace(dt.strftime("%A").lower(), '')
        text = text.replace(dt.strftime("%B").lower(), '')
        text = text.replace(str(dt.day), '')
    text = re.sub(r'\b(on|at|the)\b', '', text)
    title = re.sub(r'\s+', ' ', text).strip().title()
    return title or "Untitled Event"

@chat_bp.route('/chat', methods=['GET'])
def chat_ui():
    return render_template('chat.html')

@chat_bp.route('/chat', methods=['POST'])
def chat_api():
    user = request.json.get('message', '')
    user_lower = user.lower()
    dates = extract_datetime(user)

    if not dates:
        return jsonify({'reply': "¿?  I couldn't recognize the date/time format."})

    dt = dates[0]
    title = extract_event_title(user, dates)

    if any(kw in user_lower for kw in ["add", "schedule", "create"]):
        existing = Event.query.filter_by(title=title, start=dt).first()
        if existing:
            return jsonify({'reply': f"⚠️ Event '{title}' at {dt.strftime('%Y-%m-%d %I:%M %p')} already exists."})
        db.session.add(Event(title=title, start=dt, end=dt))
        db.session.commit()
        return jsonify({'reply': f"✅ Added event '{title}' at {dt.strftime('%Y-%m-%d %I:%M %p')}"})

    if any(kw in user_lower for kw in ["what", "calendar", "planned", "do i have", "anything"]):
        start = dt.replace(hour=0, minute=0)
        end = dt.replace(hour=23, minute=59)
        events = Event.query.filter(Event.start >= start, Event.start <= end).all()
        if events:
            return jsonify({'reply': f"📅‼️ You have {len(events)} event(s) on {dt.date()}: " + ", ".join(e.title for e in events)})
        return jsonify({'reply': f"📅 You have no events on {dt.date()}."})

    return jsonify({'reply': "🤖 I didn't understand. Try 'Schedule meeting on Friday at 2 PM' or 'What's on my calendar on July 13?'."})
