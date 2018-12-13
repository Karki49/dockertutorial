from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "hello says hi"

@app.route('/docker')
def dock():
    return "Docker is bae!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)