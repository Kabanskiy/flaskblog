from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return "zdarova"


@app.route('/about') # здесь отслеживаем переход на страницу
def about():
    return "O nas"

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page' + name + '-' + 'id'




if __name__ == '__main__':
    app.run(debug=True) #debug для проверки