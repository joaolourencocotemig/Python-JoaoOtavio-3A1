from flask import Flask, request, render_template
import calculadora

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return calculadora.calcular()
    return render_template("calculadora.html")

if __name__ == "__main__":
    app.run(debug=True)
