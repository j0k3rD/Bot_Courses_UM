from main.repositories.repository import Create, Delete, Read, Update 
from main.models import UserModel
from .. import db

class UserRepository(Create, Read, Update):

    def __init__(self):
        self.__type_model = UserModel

    @property
    def type_model(self):
        return self.__type_model
    
    def create(self, model: db.Model):
        db.session.add(model)
        db.session.commit()
        return model

    def update(self, model: db.Model) -> db.Model:
         db.session.merge(model)
         db.session.commit() 
         return model 

    def find_all(self):
        model = db.session.query(self.type_model).all()
        return model

    def find_by_id(self, id: int) -> db.Model:
        model = db.session.query(self.type_model).filter_by(id=id).first() 
        return model

    def find_by_discord_id(self, discord_id: int) -> db.Model:
        model = db.session.query(self.type_model).filter(self.type_model.discord_id == discord_id).first()
        return model