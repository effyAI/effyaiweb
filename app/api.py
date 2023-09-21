from flask import Flask, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

class Hello(Resource):
    def get(self):
        return {"response":"Hello"}

api.add_resource(Hello,"/hello")        

if __name__ == "__main__":
    app.run()