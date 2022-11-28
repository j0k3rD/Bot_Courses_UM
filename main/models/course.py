from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Course(db.Model):
    __tablename__ = 'courses'
    __id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    __url = db.Column('url', db.String(100), nullable = False)
    __title = db.Column('title', db.String(100), nullable = False)
    __count = db.Column('count', db.Integer, nullable = False)

    def __repr__(self):
        return f'< Course:  {self.__id} {self.__url} {self.__title}, {self.__count}>'

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
    def discord_id(self, url):
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


    #Convertir objeto a JSON
    def to_json(self):
        course_json = {
            'id': self.id,
            'url': self.url,
            'title': self.title,
            'count': self.count
        }
        return course_json

    @staticmethod
    #Convertir JSON a objeto
    def from_json(course_json):
        id = course_json.get('id')
        url = course_json.get('url')
        title = course_json.get('title')
        count = course_json.get('count')
        return Course(id=id, 
                      url=url, 
                      title=title, 
                      count=count)
