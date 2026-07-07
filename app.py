from flask import Flask, request, jsonify

app = Flask(__name__)

# Список пользователей
USERS = {
    "apiintegration@Activitis.ua": {
        "password": "eZ1#tkF4@jnE5$waJ3_",
        "apikey": "vdtreSdiaRQ8Uh8TxKC14A0f1",
        "account_id": "18",
        "filter_call_filter_data": "4"
    },

    # Пример второго пользователя
    "user2@test.com": {
        "password": "123456",
        "apikey": "AAAAAAAAAAAAAAAAAAAA",
        "account_id": "25",
        "filter_call_filter_data": "7"
    }
}


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Ontime API",
        "status": "online"
    })


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No JSON provided"
        }), 400

    email = data.get("email")
    password = data.get("password")

    user = USERS.get(email)

    if user and user["password"] == password:
        return jsonify({
            "success": True,
            "apikey": user["apikey"],
            "account_id": user["account_id"],
            "filter[call_filter_data]": user["filter_call_filter_data"]
        })

    return jsonify({
        "success": False,
        "message": "Invalid email or password"
    }), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
