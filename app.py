from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Tony!"

if __name__ == "__main__":
    # enable debug=True for auto-reload
    app.run(host="0.0.0.0", port=5000, debug=True)