from .. import db
from main.models import UserModel
from main.map import UserSchema
from .command import Command, Task
from flask import request


user_schema = UserSchema()


class UserService:

    def add_user(self):
        user = user_schema.load(request.get_json())
        if self.register_user(user):
            db.session.add(user)
            db.session.commit()
            print('Return user')
            return user
        return False  

    def get_users(self):
        user = db.session.query(UserModel).all()
        return user

    def register_user(self, user):
        task = Task()
        task.execute(user)

    
class SaveUser(Command):

    def execute(self, user):
        try:
            db.session.add(user)
            db.session.commit()
            return user.to_json(), 201
        except:
            return '', 404