from app import app

@app.route("/")
def home():
    return "Bem-vindo ao Flask 444"
