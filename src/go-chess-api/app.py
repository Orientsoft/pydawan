from flask import Flask
from flask_restful import Api
from handlers.hello import HelloWorld

app = Flask(__name__)

# Register api handlers
api = Api(app)
api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
