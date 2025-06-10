from flask import request, jsonify
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards' ,url_prefix='/board')

## api List

## 전체 게시글 불러 오기 ( GET )
## 게시글 작성 ( POST )
@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()

        # for board in boards:
        #     print('id', board.id)
        #     print('title', board.title)
        #     print('content', board.content)
        #     print('author', board.author)
        #     print('user_id', board.user_id)

        return jsonify([{"id":board.id,
                         "title":board.title,
                         "content":board.content,
                         "author_name":board.author.name,
                         "author_email":board.author.email}
                        for board in boards])

    def post(self):
        data = request.json
        new_board = Board(title=data['title'],content=data['content'],user_id=data['user_id'])
        db.session.add(new_board)
        db.session.commit()

        return jsonify({"msg":'success'}), 201

@board_blp.route('/<int:board_id>')
class BoardResource(MethodView):
    def get(self, board_id):
        board = Board.query.get_or_404(board_id)
        #board_id 가 존재하면 get을 ,그렇지 않으면 not foud 404를 get

        return jsonify({"id":board.id,
                        "title":board.title,
                        "content":board.content,
                        "author_email":board.author.name
                        })


    def put(self, board_id):
        board = Board.query.get_or_404(board_id)
        data = request.json

        board.title = data['title']
        board.content = data['content']

        db.session.commit()

        return jsonify({"msg":'success'}), 201

    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()
        return jsonify({"msg":'success'}), 204
