from flask import Flask
import random

app = Flask(__name__)
points = [
    "Most people who suffer from technological addiction experience high levels of stress when they are outside network coverage or unable to use their devices.",

    "According to a study conducted in 2018, more than 50 percent of people between the ages of 18 and 34 consider themselves dependent on their smartphones.",

    "The study of technological dependence is one of the most relevant areas of modern scientific research.",

    "According to a 2019 study, more than 60 percent of people respond to work messages on their smartphones within 15 minutes after leaving work.",

    "One way to combat technological dependence is to seek activities that bring pleasure and improve mood.",

    "Elon Musk states that social media platforms are designed to keep users engaged for as long as possible, encouraging them to spend more time consuming content.",

    "Elon Musk also advocates for the regulation of social media and the protection of users' personal data. He claims that these platforms collect a vast amount of information, which can later be used to influence thoughts and behaviors.",

    "Social media has both positive and negative aspects, and users should be aware of both when using these platforms."
]

@app.route("/random_fact")
def hello_world():
    return f'<p>{random.choice(points)}</p>'

@app.route("/")
def rotting_beef():
    return '''
    <h1>Hi! You're now in my technological dependencies page!</h1>
    <a href="/random_fact">! Random fact</a><br>
    <a href="/all_facts">! See all facts</a>
    '''

@app.route("/all_facts")
def all_facts():
    html = "<h1>All Facts 🌸</h1><ul>"

    for fact in points:
        html += f"<li>{fact}</li>"

    html += "</ul><br><a href='/'>Go back</a>"

    return html

@app.route("/secret")
def secret():
    return '''
    <h1 style="color:#ff69b4; font-family: Comic Sans MS;">
         You found the secret! 
    </h1>

    <p>ok... how did you even get here? </p>

    <img src="https://img1.picmix.com/output/stamp/normal/2/1/0/7/2587012_19544.png" width="120">

    <br><br>
    <a href="/">go back</a>
    '''   
    

app.run(debug=True)
