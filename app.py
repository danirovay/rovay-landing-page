from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

PHONE_IP = "192.168.4.78"
USERNAME = "admin"
PASSWORD = "majopar"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/call")
def call():
    numero = request.args.get("number")

    session = requests.Session()

    # 1️⃣ Fazer login web
    login_url = f"http://{PHONE_IP}/cgi-bin/dologin"
    login_data = {
        "username": USERNAME,
        "password": PASSWORD
    }

    login_response = session.post(login_url, data=login_data)

    print("LOGIN STATUS:", login_response.status_code)

    # 2️⃣ Fazer chamada usando mesma sessão
    call_url = f"http://{PHONE_IP}/cgi-bin/api-make_call?phonenumber={numero}"
    call_response = session.get(call_url)

    print("CALL STATUS:", call_response.status_code)
    print("CALL RESPONSE:", call_response.text)

    return jsonify({
        "login_status": login_response.status_code,
        "call_status": call_response.status_code,
        "call_response": call_response.text
    })

@app.route("/hangup")
def hangup():
    session = requests.Session()

    # login se você ainda estiver usando sessão
    session.post(
        f"http://{PHONE_IP}/cgi-bin/dologin",
        data={"username": USERNAME, "password": PASSWORD}
    )

    # tente o endpoint mais comum primeiro
    hangup_url = f"http://{PHONE_IP}/cgi-bin/api-hangup"
    r = session.get(hangup_url)

    print("HANGUP STATUS:", r.status_code)
    print("HANGUP RESPONSE:", r.text)

    return f"Hangup status: {r.status_code}"

if __name__ == "__main__":
    app.run(debug=True)