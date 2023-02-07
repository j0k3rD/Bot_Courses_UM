from main.repositories.repository import Create, Delete, Read, Update
from main.models import SearchModel
from .. import db

class SearchRepository(Create, Read, Update):

    def __init__(self):
        self.__type_model = SearchModel
    
    def create(self, model: db.Model):
        #Verificar si la busqueda ya existe
        search_exist = db.session.query(self.__type_model).filter_by(name=model.name).first()
        if search_exist is None:
            db.session.add(model)
            db.session.commit()
            return model
        else:
            return search_exist

    def update(self, model: db.Model) -> db.Model:
         db.session.merge(model)
         db.session.commit() 
         return model  

    def find_all(self):
        return db.session.query(db.Model).all()

    def find_by_id(self, id: int) -> db.Model:
        return db.session.query(self.__type_model).filter_by(id=id).first() 