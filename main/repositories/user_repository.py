from main.repositories.irepository import Create, Delete, Read, Update 
from .. import db

class UserRepository(Create, Read, Update, Delete):

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