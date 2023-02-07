from main.repositories.repository import Create, Delete, Read, Update
from main.models import CourseModel
from .. import db

class CourseRepository(Create, Read, Update, Delete):
    
    def __init__(self,):
        self.__type_model = CourseModel

    def create(self, model: db.Model):
        #Verificar si el curso ya existe
        course_exist = db.session.query(self.__type_model).filter_by(name=model.name).first()
        if course_exist is None:
            db.session.add(model)
            db.session.commit()
            return model
        else:
            return course_exist

    def update(self, model: db.Model) -> db.Model:
        db.session.merge(model)
        db.session.commit()
        return model 

    def delete(self, model: db.Model):
        db.session.delete(model)
        db.session.commit()

    def delete_by_id(self, id: int):
        db.session.query(self.__type_model).filter_by(id=id).delete()
        db.session.commit() 

    def find_all(self):
        return db.session.query(db.Model).all()

    def find_by_id(self, id: int) -> db.Model:
        return db.session.query(self.__type_model).filter_by(id=id).first()