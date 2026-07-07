from flask import Flask, request, jsonify

app = Flask(__name__)

EMAIL = "apiintegration@Activitis.ua"
PASSWORD = "eZ1#tkF4@jnE5$waJ3_"

API_KEY = "vdtreSdiaRQ8Uh8TxKC14A0f1"
ACCOUNT_ID = "18"


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if data is None:
        return jsonify({
            "success": False,
            "message": "No JSON provided"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if email == EMAIL and password == PASSWORD:
        return jsonify({
            "success": True,
            "apikey": API_KEY,
            "account_id": ACCOUNT_ID
        })

    return jsonify({
        "success": False,
        "message": "Invalid email or password"
    }), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)