from main.repositories.irepository import Create, Read
from .. import db
class StatisticRepository(Create, Read):

    def create(self, model: db.Model):
        db.session.add(model) 
        db.session.commit() 
        return model 


    def find_all(self):
        return db.session.query(db.Model).all()

    def find_by_id(self):
        return db.session.query(self.type_model).filter_by(id=id).first()