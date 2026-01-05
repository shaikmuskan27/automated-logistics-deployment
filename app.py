# Version 1.1
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "REALM CORE: System Online and Monitoring Last Mile Logistics."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)