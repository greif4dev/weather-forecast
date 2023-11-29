import requests
from flask import Flask, render_template, request, send_from_directory

app= Flask(__name__, template_folder='../templates', static_folder='../static')

API_KEY = "40fc25677a830026dc3505d99e37020d"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/previsao", methods=['POST'])
def Previsao():
    cidadeUser = request.form['searchBar']
    URL = f"https://pro.openweathermap.org/data/2.5/weather?q={cidadeUser}&APPID={API_KEY}"
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
