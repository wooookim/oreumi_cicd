from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '파이썬 배포 테스트'

if __name__ == '__main__':
    app.run()
