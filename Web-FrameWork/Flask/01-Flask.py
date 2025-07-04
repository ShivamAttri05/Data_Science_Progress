from flask import Flask, render_template

# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome Back"

@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)