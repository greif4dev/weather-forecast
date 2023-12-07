from flask import Flask, render_template, request
from weather import main as getWeather

app= Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route("/home", methods=['GET', 'POST'])
def index():
    data = None
    vento = ''
    previa = 'Pesquise para os dados serem visualizados'
    if request.method== 'POST':
        city = request.form['searchBar']
        data = getWeather(city)
        vento = 'Vento'
        previa = ''
    return render_template("index.html", data=data, vento=vento, previa=previa)

@app.route("/")
def login():
    return render_template("tela-login.html")

@app.route("/redefinir")
def redefinir():
    return render_template("redefinirSenha.html")

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

if __name__ == '__main__':
    app.run(debug=True)
