from flask import Flask, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return {"response":"Hello"}  



if __name__ == "__main__":
    app.run()