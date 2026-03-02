from flask import Flask, render_template, request, jsonify
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

PHONE_IP = "192.168.4.78"
BASE_URL = f"http://{PHONE_IP}"   # FORÇANDO HTTP
USERNAME = "admin"
PASSWORD = "majopar"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/call", methods=["POST"])
def call():
    number = request.form["number"]
    url = f"{BASE_URL}/cgi-bin/api-make_call?phonenumber={number}"

    try:
        r = requests.get(
            url,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=5
        )
        return jsonify({
            "status": r.status_code,
            "response": r.text
        })
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/hangup", methods=["POST"])
def hangup():
    url = f"{BASE_URL}/cgi-bin/api-hangup_call"

    try:
        r = requests.get(
            url,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=5
        )
        return jsonify({
            "status": r.status_code,
            "response": r.text
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)