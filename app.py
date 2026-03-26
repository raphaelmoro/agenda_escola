from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadastro_aluno", methods=["GET", "POST"])
def cadastro_aluno():
    mensagem = ""

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        idioma = request.form.get("idioma")

        mensagem = f"Aluno {nome} cadastrado com sucesso!"

        return render_template(
            "cadastro_aluno.html",
            mensagem=mensagem,
            nome=nome,
            email=email,
            telefone=telefone,
            idioma=idioma
        )

    return render_template("cadastro_aluno.html", mensagem=mensagem)

@app.route("/agenda_aulas", methods=["GET", "POST"])
def agenda_aulas():
    mensagem = ""
    dados_aula = None

    if request.method == "POST":
        aluno = request.form.get("aluno")
        professor = request.form.get("professor")
        idioma = request.form.get("idioma")
        data = request.form.get("data")
        horario = request.form.get("horario")
        modalidade = request.form.get("modalidade")

        mensagem = "Aula agendada com sucesso!"
        dados_aula = {
            "aluno": aluno,
            "professor": professor,
            "idioma": idioma,
            "data": data,
            "horario": horario,
            "modalidade": modalidade
        }

    return render_template(
        "agenda_aulas.html",
        mensagem=mensagem,
        dados_aula=dados_aula
    )

if __name__ == "__main__":
    app.run(debug=True)
    