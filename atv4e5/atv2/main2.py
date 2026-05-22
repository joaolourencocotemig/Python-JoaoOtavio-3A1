from flask import Flask, request, render_template, render_template_string

import json

def ler():
    with open("atv2/dados.json", "r", encoding="utf-8") as m:
        dados = json.load(m)
        return dados

dados = ler()

app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario = request.form.get('usuario')
    senha1 = request.form.get('senha')

    def funcao(lista):
        for nome, senha in lista.items():
            if usuario == nome and senha1 == senha:
                return True
                
        return False
        
    if funcao(dados) == True:
        return f"<h1>Bem-vindo, {usuario}!</h1>"
    else:
        return "<h1>Login inválido</h1>"


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)

# site de consulta https://flask.palletsprojects.com/en/stable/quickstart/#html-escaping