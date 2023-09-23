from flask import Flask, render_template, render_template_string
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return render_template('index.html')

class Hello(Resource):
    def get(self):
        return {"output":"Hello"}
api.add_resource(Hello,"/hello")

if __name__ == "__main__":
    app.run(debug = True, port=5000)