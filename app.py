from flask import Flask, request, jsonify

app = Flask(__name__)

# ===========================
# Пользователи
# ===========================

USERS = {
    "apiintegration@Activitis.ua": {
        "password": "eZ1#tkF4@jnE5$waJ3_",
        "apikey": "vdtreSdiaRQ8Uh8TxKC14A0f1",
        "account_id": "18",
        "company_id": "10639",
        "filter_call_filter_data": "4"
    },

    "apiintegration@sloncredit.ua": {
        "password": "jZkpY0*omM9@iiB3#u",
        "apikey": "olCxrKcxWUEKHjUNdWZTSk0hB",
        "account_id": "10",
        "company_id": "2148",
        "filter_call_filter_data": "47"
    }
}


# ===========================
# Главная страница
# ===========================

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Ontime API",
        "status": "online"
    })


# ===========================
# Авторизация
# ===========================

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
            "company_id": user["company_id"],
            "filter[call_filter_data]": user["filter_call_filter_data"]
        })

    return jsonify({
        "success": False,
        "message": "Invalid email or password"
    }), 401


# ===========================
# Запуск приложения
# ===========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
