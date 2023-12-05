from flask import Flask, render_template, request
from weather import main as getWeather

app= Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route("/", methods=['GET', 'POST'])
def index():
    data = None
    if request.method== 'POST':
        city = request.form['searchBar']
        data = getWeather(city)
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
