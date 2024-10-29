from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Привет, рад видеть!"


@app.route('/<int:x>')
def your_age(x: int):
    return f"Уже много годочков, а еще не программист ;( Просто число: {x * 2}"


if __name__ == '__main__':
    app.run()