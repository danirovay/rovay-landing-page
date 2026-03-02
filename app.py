from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

PHONE_IP = "192.168.4.78"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/call", methods=["POST"])
def call():
    number = request.form["number"]
    url = f"http://{PHONE_IP}/cgi-bin/api-make_call?phonenumber={number}"

    try:
        r = requests.get(url, timeout=5)
        return jsonify({"status": "ok", "response": r.text})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/hangup", methods=["POST"])
def hangup():
    url = f"http://{PHONE_IP}/cgi-bin/api-hangup_call"

    try:
        r = requests.get(url, timeout=5)
        return jsonify({"status": "ok", "response": r.text})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)