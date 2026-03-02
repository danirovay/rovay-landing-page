from flask import Flask, render_template, request, redirect
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

# CONFIGURAÇÕES DO SEU TELEFONE
PHONE_IP = "192.168.4.78"
USERNAME = "admin"
PASSWORD = "majopar"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/call", methods=["POST"])
def call():
    number = request.form["number"]
    url = f"http://{PHONE_IP}/cgi-bin/api-make_call?phonenumber={number}"

    try:
        requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), timeout=5)
    except Exception as e:
        print("Erro ao ligar:", e)

    return redirect("/")

@app.route("/hangup", methods=["POST"])
def hangup():
    url = f"http://{PHONE_IP}/cgi-bin/api-hangup_call"

    try:
        requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), timeout=5)
    except Exception as e:
        print("Erro ao desligar:", e)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)