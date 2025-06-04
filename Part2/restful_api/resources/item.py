from flask import Flask, request
from flask_restful import Api, Resource


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'error': 'item not found'}, 404

    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {'error': 'item already exists'}, 400

        data = request.get_json()

        new_item =  {'name': name, 'price': data['price']}
        items.append(new_item)

        return new_item

    def put(self, name):
        data = request.get_json()

        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return  item

        new_item = {'name': name, 'price': data['price']}
        items.append(new_item)

        return new_item


    def delete(self, name):
        global items

        items = [item for item in items if item['name'] != name]
        return {'message': 'item deleted'}, 200