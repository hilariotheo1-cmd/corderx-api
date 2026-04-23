from flask import Flask, request, jsonify
from flask_cors import CORS
import random, string, os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API ONLINE ✅"

@app.route("/gerar", methods=["POST"])
def gerar():
    key = "CORDERX-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return jsonify({"key": key})

# 🔥 IMPORTANTE PRA RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)