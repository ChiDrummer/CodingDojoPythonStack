from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_results', methods=['POST'])
def form_results():


     data = {
        "name": request.form['name'],
        "dojo_location": request.form['dojo_location'],
        "favorite_language": request.form["favorite_language"],
        "comment": request.form["comment"]
    }

    return render_template("results.html", form_data = data) 


app.run(debug=True)

