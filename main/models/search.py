from .. import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

class Search(db.Model):
    '''
        Clase que representa la entidad Search en la base de datos

        param:
            - db.Model: Clase de la cual hereda para mapear la entidad.
    '''
    __tablename__ = 'searchs'
    __id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    __keywords = db.Column('keywords', db.String(100), nullable = False)
    __date = db.Column('date',db.DateTime(),default=datetime.now(), nullable=False)
    __user_id = db.Column('user_id', db.ForeignKey('users.id'), nullable=False)

    #Relacion con User
    user = db.relationship('User', back_populates='search')
    #Relacion con Course
    course = db.relationship('Course', back_populates='search')

    def __repr__(self):
        return f'< User:  {self.__id} {self.__keywords} {self.__date}, {self.__user_id}>'

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
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords):
        self.__keywords = keywords

    @keywords.deleter
    def keywords(self):
        del self.__keywords

    @hybrid_property
    def date(self):
        return self.__date

    @date.setter
    def date(self,date):
        self.__date = date

    @date.deleter
    def date(self):
        del self.__date
    
    @hybrid_property
    def user_id(self):
        return self.__user_id
    
    @user_id.setter
    def user_id(self,user_id):
        self.__user_id = user_id
    
    @user_id.deleter
    def user_id(self):
        del self.__user_id