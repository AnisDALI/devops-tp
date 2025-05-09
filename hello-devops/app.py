from flask import Flask

app = Flask(__name__)

@app.route('/status')
def status():
    return "Status: OK"

def hello():
    return "Hello, CI/CD!"

if __name__ == "__main__":
    app.run()
