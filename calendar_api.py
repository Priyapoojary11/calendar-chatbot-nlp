from flask import Blueprint, jsonify, request
from models import Event, db
from dateutil import parser

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/api/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{'id': e.id, 'title': e.title, 'start': e.start.isoformat(), 'end': e.end.isoformat()} for e in events])

@calendar_bp.route('/api/events', methods=['POST'])
def add_event():
    data = request.json
    e = Event(title=data['title'],
            start=parser.isoparse(data['start']),
            end=parser.isoparse(data['end']))
    db.session.add(e); db.session.commit()
    return jsonify({'status': 'ok', 'id': e.id})
