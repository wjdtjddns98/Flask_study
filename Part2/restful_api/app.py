from flask import Flask, request
from flask_restful import Api, Resource
from resources.item import Item
app = Flask(__name__)
api = Api(app)

items = [] # DB의 대체 역할 ( 간단한 DB )

api.add_resource(Item, '/item/<string:name>')

if __name__ == '__main__':
    app.run()