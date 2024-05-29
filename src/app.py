from flask import Flask, render_template, request
from nlps.sentiment import sentiment_analysis, named_entity

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


default_ner = "SpaceX is an aerospace manufacturer and space transport services company headquartered in California. It was founded in 2002 by entrepreneur and investor Elon Musk with the goal of reducing space transportation costs and enabling the colonization of Mars."
@app.route("/ner",methods=['GET', 'POST'])
def ner():
    text = request.form.get('ner-text')
    ner_response = named_entity(text)
    return render_template('ner.html',ner=ner_response.get('entities'),default_ner=default_ner)



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)