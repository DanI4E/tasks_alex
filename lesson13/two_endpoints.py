from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Привет, рад видеть!"


@app.route('/age')
def your_age():
    b = 25
    return f"Уже много годочков, а еще не программист ;( Просто число: {b * 2}"


if __name__ == '__main__':
    app.run()