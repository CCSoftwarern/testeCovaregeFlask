from app import app

@app.route("/")
def home():
    return "Bem-vindo ao Flask Test 2025!"
