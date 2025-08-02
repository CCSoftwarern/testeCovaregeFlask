from app import app

# esse teste verifica se a rota home que está dentro de app/routes.py está funcionando corretamente
def test_home():
    client = app.test_client() # simula um navegador
    response = client.get('/')  # requisita a rota home
    assert response.status_code == 200 # verifica se o status da resposta é 200 (OK)
    assert b"Bem-vindo" in response.data # verifica se a resposta contém o texto "Bem-vindo"