from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", phrase="HELLOOOOOOO!!!!!!!!", times=5)
app.run(debug=True)   
