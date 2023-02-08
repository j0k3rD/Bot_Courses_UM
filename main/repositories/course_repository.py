from main.repositories.repository import Create, Delete, Read, Update
from main.models import CourseModel
from .. import db

class CourseRepository(Create, Read, Update):
    
    def __init__(self,):
        self.__type_model = CourseModel

    def create(self, model: db.Model):
        db.session.add(model)
        db.session.commit()
        return model

    def update(self, model: db.Model) -> db.Model:
        db.session.merge(model)
        db.session.commit()
        return model 
    
    # def delete(self, model: db.Model):
    #     db.session.delete(model)
    #     db.session.commit()

    # def delete_by_id(self, id: int):
    #     db.session.query(self.__type_model).filter_by(id=id).delete()
    #     db.session.commit() 

    def find_all(self):
        model = db.session.query(self.__type_model).all()
        return model

    def find_by_id(self, id: int) -> db.Model:
        model = db.session.query(self.__type_model).filter_by(id=id).first()
        return model

    def find_course_by_url(self, course_url: str) -> db.Model:
        model = db.session.query(self.__type_model).filter(self.__type_model.url == course_url).first()
        return model

    def add_count(self, id: int) -> db.Model:
        model = self.find_by_id(id)
        model.count += 1
        db.session.commit()
        return model

    def find_top_courses(self, limit: int) -> db.Model:
        model = db.session.query(self.__type_model).order_by(self.__type_model.count.desc()).limit(limit).all()
        return model