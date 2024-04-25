from flask import Flask, render_template, request
from nlps.sentiment import sentiment_analysis

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/sentiment",methods=['GET', 'POST'])
def sentiment():
    text = request.form.get('message')
    response = sentiment_analysis(text)
    return render_template('sentiment.html',sentiments=response.get('sentiment'))



if __name__ == "__main__":
    app.run(debug=True)