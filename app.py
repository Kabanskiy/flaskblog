from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

@app.route('/posts')
def posts():
    bazes = Baza.query.order_by(Baza.date).all()
    return render_template('posts.html', bazes=bazes)

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/create_baza', methods=['POST', 'GET'])
def create_baza():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        baza = Baza(title=title, intro = intro, text = text)
        try:
            db.session.add(baza)
            db.session.commit()
            return redirect('/')
        except:
            return 'При добавлении статьи произошла ошибка'
    else:
        return render_template('create_baza.html')


if __name__ == '__main__':
    app.run(debug=True) #debug для проверки