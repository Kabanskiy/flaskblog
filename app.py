from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Baza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(250), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

app.app_context().push()

def __repr__(self):
    return '<Baza %r>' %self.id

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about') # здесь отслеживаем переход на страницу
def about():
    return render_template('about.html')

@app.route('/create_baza') # здесь отслеживаем переход на страницу
def create_baza():
    return render_template('create_baza.html')


if __name__ == '__main__':
    app.run(debug=True) #debug для проверки