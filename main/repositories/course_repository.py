from botCursos_UM.main.models.course import Course
from main.repositories.irepository import Create, Delete, Read, Update
from .. import db

class CourseRepository(Create, Read, Update, Delete):
    def __init__(self,):
        self.type_model = Course

    def create(self, model: db.Model):
        db.session.add(model) # Agrega el modelo a la sesión
        db.session.commit() # Guarda los cambios en la base de datos
        return model # Retorna el modelo

    def update(self, model: db.Model) -> db.Model:
        db.session.merge(model) # Actualiza el modelo en la sesión
        db.session.commit() # Guarda los cambios en la base de datos
        return model # Retorna el modelo si existe, de lo contrario retorna None

    def delete(self, model: db.Model):
        db.session.delete(model) # Elimina el modelo de la sesión
        db.session.commit() # Guarda los cambios en la base de datos

    def delete_by_id(self, id: int):
        db.session.query(self.type_model).filter_by(id=id).delete() # Elimina el modelo de la sesión
        db.session.commit() 

    def find_all(self):
        return db.session.query(db.Model).all()

    def find_by_id(self, id: int) -> db.Model:
        return db.session.query(self.type_model).filter_by(id=id).first() # Retorna el modelo si existe, de lo contrario retorna None
