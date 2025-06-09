from flask import request, jsonify
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from Part4.db import db
from Part4.models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards' ,url_prefix='/board')

## api List

## 전체 게시글 불러 오기 ( GET )
## 게시글 작성 ( POST )
@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()
        print(boards)
    def post(self):
        pass

## 하나의 게시글 불러 오기 ( GET )
## 특정 게시글 수정 하기 ( PUT )
## 특정 게시글 삭제 하기 ( DELETE )
