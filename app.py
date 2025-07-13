from flask import Flask
from models import db
from calendar_api import calendar_bp
from chatbot import chat_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)
app.register_blueprint(calendar_bp)
app.register_blueprint(chat_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
