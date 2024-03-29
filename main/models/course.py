from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Course(db.Model):
    '''
        Clase que representa la entidad Course en la base de datos

        param:
            - db.Model: Clase de la cual hereda para mapear la entidad.
    '''
    __tablename__ = 'courses'
    __id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    __url = db.Column('url', db.String(100), nullable = False)
    __title = db.Column('title', db.String(100), nullable = False)
    __count = db.Column('count', db.Integer, default = 1, nullable = False)
    __search_id = db.Column('search_id', db.ForeignKey('searchs.id'), nullable=False)

    #Relacion con Search
    search = db.relationship('Search', back_populates='course')

    def __repr__(self):
        return f'< Course: {self.__id} {self.__url} {self.__title}, {self.__count}, {self.__search_id}>'

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
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @url.deleter
    def url(self):
        del self.__url

    @hybrid_property
    def title(self):
        return self.__title

    @title.setter
    def title(self,title):
        self.__title = title

    @title.deleter
    def title(self):
        del self.__title
    
    @hybrid_property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self,count):
        self.__count = count
    
    @count.deleter
    def count(self):
        del self.__count

    @hybrid_property
    def search_id(self):
        return self.__search_id
    
    @search_id.setter
    def search_id(self,search_id):
        self.__search_id = search_id
    
    @search_id.deleter
    def search_id(self):
        del self.__search_id