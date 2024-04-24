from flask import Flask, render_template

app = Flask(__name__)


sentiments = {'Positive':50,'Neutral':10,'Negative':40}

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/sentiment")
def sentiment():
    return render_template('sentiment.html',sentiments=sentiments)



if __name__ == "__main__":
    app.run(debug=True)