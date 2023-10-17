from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import pyttsx3
app=Flask("__name__")
@app.route("/")
def MainPage():
    return render_template("index.html")

@app.route('/speak',methods=["POST"])
def Speak():
    text=request.form.get("text")
    TextToSpeech(text)
    return redirect("/")

def TextToSpeech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.setProperty('rate',10)
    engine.runAndWait()

if __name__=="__main__":
    app.run(debug=True)