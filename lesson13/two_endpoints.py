from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Привет, рад видеть!"


@app.route('/age')
def your_age():
    return "Уже много годочков, а еще не программист ;("


if __name__ == '__main__':
    app.run()