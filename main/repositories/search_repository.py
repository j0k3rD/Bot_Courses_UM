from main.repositories.repository import Create, Delete, Read, Update
from main.models import SearchModel
from .. import db

class SearchRepository(Create, Read, Update):

    def __init__(self):
        self.__type_model = SearchModel
    
    def create(self, model: db.Model):
        db.session.add(model)
        db.session.commit()
        return model

    def update(self, model: db.Model) -> db.Model:
         db.session.merge(model)
         db.session.commit() 
         return model  

    def find_all(self):
        model = db.session.query(self.__type_model).all()
        return model

    def find_by_id(self, id: int) -> db.Model:
        model = db.session.query(self.__type_model).filter_by(id=id).first() 
        return model

    def find_by_user_id(self, user_id: int) -> db.Model:
        model = db.session.query(self.__type_model).filter(self.__type_model.user_id == user_id).last()
        return model