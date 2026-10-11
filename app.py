
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head><title>DevOps Demo</title></head>
      <body style="font-family:Arial;text-align:center;
                   margin-top:100px;background:#eef4ff">
        <h1>My DevOps Pipeline</h1>
        <h2>Application is Running!</h2>
        <p>CI/CD, Docker and monitoring demonstration</p>
        <a href="/health">Check Application Health</a>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
