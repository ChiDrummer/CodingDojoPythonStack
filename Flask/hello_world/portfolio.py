from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def first_page():
    return render_template("welcome.html")

@app.route('/projects')
def second_page():
  return render_template('projects.html')

@app.route('/bio')
def third_page():
  return render_template('about_me.html')


app.run(debug=True)