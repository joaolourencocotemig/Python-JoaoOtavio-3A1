import os
from functools import wraps

import requests
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from database import get_db_connection, init_db

app = Flask(__name__)


app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "troque-esta-chave-em-producao")
DEBUG = os.environ.get("FLASK_DEBUG", "True") == "True" 

STATUS_VALIDOS = {"Pendente", "Em andamento", "Concluída"}


def login_requerido(f):
    @wraps(f)
    def decorada(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Você precisa fazer login para acessar essa página.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorada


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form["nome"].strip()
        email = request.form["email"].strip().lower()
        senha = request.form["senha"]

        if not nome or not email or not senha:
            flash("Preencha todos os campos.", "danger")
            return redirect(url_for("registro"))

        senha_hash = generate_password_hash(senha)  

        conn = get_db_connection()
        try:
            conn.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                (nome, email, senha_hash),
            )
            conn.commit()
            flash("Cadastro realizado com sucesso! Faça login.", "success")
            return redirect(url_for("login"))
        except conn.IntegrityError:
            flash("Esse e-mail já está cadastrado.", "danger")
        finally:
            conn.close()

    return render_template("registro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        senha = request.form["senha"]

        conn = get_db_connection()
        usuario = conn.execute(
            "SELECT * FROM usuarios WHERE email = ?", (email,)
        ).fetchone()
        conn.close()

        if usuario and check_password_hash(usuario["senha"], senha):
            session["usuario_id"] = usuario["id"]
            session["usuario_nome"] = usuario["nome"]
            flash(f"Bem-vindo(a), {usuario['nome']}!", "success")
            return redirect(url_for("dashboard"))

        flash("E-mail ou senha inválidos.", "danger")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("login"))


def buscar_frase_motivacional():
    """Consome a API pública advice slip. Retorna None se falhar (não trava a página)."""
    try:
        resposta = requests.get("https://api.adviceslip.com/advice", timeout=3)
        resposta.raise_for_status()
        return resposta.json()["slip"]["advice"]
    except Exception:
        return "Continue firme nos estudos, cada linha de código conta!"


@app.route("/")
def index():
    if "usuario_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_requerido
def dashboard():
    
    frase = buscar_frase_motivacional()
    return render_template("dashboard.html", frase=frase)

@app.route("/nova_tarefa", methods=["GET", "POST"])
@login_requerido
def nova_tarefa():
    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        descricao = request.form.get("descricao", "").strip()
        status = request.form.get("status", "Pendente")

        if not titulo:
            flash("O título da tarefa é obrigatório.", "danger")
            return redirect(url_for("nova_tarefa"))
        if status not in STATUS_VALIDOS:
            status = "Pendente"

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO tarefas (titulo, descricao, status, usuario_id) VALUES (?, ?, ?, ?)",
            (titulo, descricao, status, session["usuario_id"]),
        )
        conn.commit()
        conn.close()
        flash("Tarefa criada com sucesso!", "success")
        return redirect(url_for("dashboard"))

    return render_template("nova_tarefa.html")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
@login_requerido
def editar(id):
    conn = get_db_connection()
    tarefa = conn.execute(
        "SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?",
        (id, session["usuario_id"]),
    ).fetchone()

    if tarefa is None:
        conn.close()
        flash("Tarefa não encontrada.", "danger")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        descricao = request.form.get("descricao", "").strip()
        status = request.form.get("status", "Pendente")

        if not titulo:
            flash("O título da tarefa é obrigatório.", "danger")
            return redirect(url_for("editar", id=id))
        if status not in STATUS_VALIDOS:
            status = "Pendente"

        conn.execute(
            "UPDATE tarefas SET titulo = ?, descricao = ?, status = ? WHERE id = ? AND usuario_id = ?",
            (titulo, descricao, status, id, session["usuario_id"]),
        )
        conn.commit()
        conn.close()
        flash("Tarefa atualizada com sucesso!", "success")
        return redirect(url_for("dashboard"))

    conn.close()
    return render_template("editar_tarefa.html", tarefa=tarefa)


@app.route("/excluir/<int:id>")
@login_requerido
def excluir(id):
    conn = get_db_connection()
    conn.execute(
        "DELETE FROM tarefas WHERE id = ? AND usuario_id = ?",
        (id, session["usuario_id"]),
    )
    conn.commit()
    conn.close()
    flash("Tarefa excluída.", "info")
    return redirect(url_for("dashboard"))


def tarefa_para_dict(tarefa):
    return {
        "id": tarefa["id"],
        "titulo": tarefa["titulo"],
        "descricao": tarefa["descricao"],
        "status": tarefa["status"],
    }


@app.route("/api/tarefas", methods=["GET"])
@login_requerido
def api_listar_tarefas():
    """Retorna as tarefas do usuário em JSON. Aceita ?status=Pendente|Em andamento|Concluída."""
    status = request.args.get("status", "Todas")
    conn = get_db_connection()

    if status == "Todas":
        tarefas = conn.execute(
            "SELECT * FROM tarefas WHERE usuario_id = ? ORDER BY id DESC",
            (session["usuario_id"],),
        ).fetchall()
    else:
        tarefas = conn.execute(
            "SELECT * FROM tarefas WHERE usuario_id = ? AND status = ? ORDER BY id DESC",
            (session["usuario_id"], status),
        ).fetchall()
    conn.close()

    return jsonify([tarefa_para_dict(t) for t in tarefas])


@app.route("/api/tarefas", methods=["POST"])
@login_requerido
def api_criar_tarefa():
    """Cria uma tarefa recebendo JSON: {titulo, descricao, status}."""
    dados = request.get_json(silent=True) or {}
    titulo = (dados.get("titulo") or "").strip()
    descricao = (dados.get("descricao") or "").strip()
    status = dados.get("status", "Pendente")

    if not titulo:
        return jsonify({"erro": "O título é obrigatório."}), 400
    if status not in STATUS_VALIDOS:
        status = "Pendente"

    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO tarefas (titulo, descricao, status, usuario_id) VALUES (?, ?, ?, ?)",
        (titulo, descricao, status, session["usuario_id"]),
    )
    conn.commit()
    nova = conn.execute("SELECT * FROM tarefas WHERE id = ?", (cursor.lastrowid,)).fetchone()
    conn.close()
    return jsonify(tarefa_para_dict(nova)), 201


@app.route("/api/tarefas/<int:id>", methods=["PUT"])
@login_requerido
def api_editar_tarefa(id):
    """Atualiza uma tarefa recebendo JSON: {titulo, descricao, status}."""
    conn = get_db_connection()
    tarefa = conn.execute(
        "SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?", (id, session["usuario_id"])
    ).fetchone()
    if tarefa is None:
        conn.close()
        return jsonify({"erro": "Tarefa não encontrada."}), 404

    dados = request.get_json(silent=True) or {}
    titulo = (dados.get("titulo") or tarefa["titulo"]).strip()
    descricao = dados.get("descricao", tarefa["descricao"])
    status = dados.get("status", tarefa["status"])
    if status not in STATUS_VALIDOS:
        status = tarefa["status"]

    conn.execute(
        "UPDATE tarefas SET titulo = ?, descricao = ?, status = ? WHERE id = ? AND usuario_id = ?",
        (titulo, descricao, status, id, session["usuario_id"]),
    )
    conn.commit()
    atualizada = conn.execute("SELECT * FROM tarefas WHERE id = ?", (id,)).fetchone()
    conn.close()
    return jsonify(tarefa_para_dict(atualizada))


@app.route("/api/tarefas/<int:id>", methods=["DELETE"])
@login_requerido
def api_excluir_tarefa(id):
    conn = get_db_connection()
    tarefa = conn.execute(
        "SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?", (id, session["usuario_id"])
    ).fetchone()
    if tarefa is None:
        conn.close()
        return jsonify({"erro": "Tarefa não encontrada."}), 404

    conn.execute("DELETE FROM tarefas WHERE id = ? AND usuario_id = ?", (id, session["usuario_id"]))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Tarefa excluída com sucesso."})


@app.route("/api/progresso")
@login_requerido
def api_progresso():
    """Retorna a contagem de tarefas por status, usada pelo gráfico Chart.js."""
    conn = get_db_connection()
    dados = {}
    for status in STATUS_VALIDOS:
        dados[status] = conn.execute(
            "SELECT COUNT(*) FROM tarefas WHERE usuario_id = ? AND status = ?",
            (session["usuario_id"], status),
        ).fetchone()[0]
    conn.close()
    return jsonify(dados)



if __name__ == "__main__":
    init_db() 
    app.run(debug=DEBUG)  
