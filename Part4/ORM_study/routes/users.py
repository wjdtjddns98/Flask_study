from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import User
from sqlalchemy.sql.functions import user

users_blp = Blueprint('Users', 'users', description='유저 테이블 설정란 입니',url_prefix='/users')

@users_blp.route('/')
class UsersList(MethodView):
    def get(self):
        users = User.query.all()

        user_data = [
            {'id':user.id,
             'name':user.name,
             'email':user.email}
            for user in users
        ]
        return jsonify(user_data), 200

    def post(self):
        data = request.get_json()

        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'msg':'success'}), 201


@users_blp.route('/<int:user_id>')
class UserResource(MethodView):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        print(type(user))

        return jsonify({'name':user.name,
                        'email':user.email})

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.name = data['name']
        user.email = data['email']
        db.session.commit()
        return jsonify({'msg':'success'}), 200

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'msg':'success'}), 204
