from main.repositories.repository import Create, Delete, Read, Update
from main.models import SearchModel
from .. import db


class SearchRepository(Create, Read, Update, Delete):

    def __init__(self):
        self.__type_model = SearchModel

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

    def delete(self, model: db.Model):
         db.session.delete(model) 
         db.session.commit() 

    def delete_by_id(self, id: int):
        db.session.query(self.type_model).filter_by(id=id).delete() 
        db.session.commit() 

    def find_all(self):
        return db.session.query(db.Model).all()

    def find_by_id(self, id: int) -> db.Model:
        return db.session.query(self.type_model).filter_by(id=id).first() 