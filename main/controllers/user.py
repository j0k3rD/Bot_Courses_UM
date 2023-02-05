from flask_restful import Resource
from flask import request
# from main.services import CourseService
from main.map import UserSchema
from main.models import UserModel
from .. import db

user_schema = UserSchema()
# service = CourseService

class User(Resource):

    def get(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        return user_schema.dump(user), 201

    # ! This method is not totally necessary.            
    def delete(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        try:
            db.session.delete(user)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    # ! This method is not totally necessary.
    def put(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(user, key, value)
        try:
            db.session.add(user)
            db.session.commit()
            return user_schema.dump(user), 201
        except:
            return '', 404


class Users(Resource):

    def get(self):
        users = db.session.query(UserModel).all()
        return user_schema.dump(users, many=True)
        
    def post(self):
        user = user_schema.load(request.get_json())
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201