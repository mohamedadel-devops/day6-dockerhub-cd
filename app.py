from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "CI/CD to DockerHub Works!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
