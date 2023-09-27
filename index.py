from flask import Flask
from flask_restful import Api
from resources.URLShortener import URLShortener

app = Flask(__name__)
api = Api(app)

api.add_resource(URLShortener, '/')

if __name__ == '__main__':
    app.run(debug=True)
