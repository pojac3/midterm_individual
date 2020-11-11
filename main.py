from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')

def root():
    number=random.randint(-1000,1000)
    return (str(number))
if __name__ == "__main__":
    app.run(host='127.0.0.1',port='8080',debug=True)
