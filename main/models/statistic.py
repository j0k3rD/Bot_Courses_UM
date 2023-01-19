from .. import db
from sqlalchemy.ext.hybrid import hybrid_property


class Statistic(db.Model):
    __tablename__ = 'statistics'
    __id = db.Column('id', db.Integer, primary_key=True, nullable=False)

    __user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='statistics')
    __course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    course = db.relationship('Course', backref='statistics')

    def __repr__(self):
        return f'< User:  {self.__id} {self.__user_id} {self.__course_id}>'
    
    @hybrid_property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @hybrid_property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @user_id.deleter
    def user_id(self):
        del self.__user_id
    
    @hybrid_property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, course_id):
        self.__course_id = course_id

    @course_id.deleter
    def course_id(self):
        del self.__course_id