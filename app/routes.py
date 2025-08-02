from app import app

@app.route("/")
def home():
    return "Bem-vind ao Flask Test 2025!"
