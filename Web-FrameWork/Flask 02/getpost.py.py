from flask import Flask, render_template, request

# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return '<a href="/index">Click me</a>'  # Fixed the link path with a leading slash

@app.route("/index", methods=['GET'])  # 'Get' should be 'GET'
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Corrected the way to access form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return f'Hello {name}, your email is {email} and message is: {message}'
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
