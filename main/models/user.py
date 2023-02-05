from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):
    __tablename__ = 'users'
    __id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    __discord_id = db.Column('discord_id', db.Integer, nullable=False)
    __name = db.Column('name', db.String(100), nullable=False)

    def __repr__(self):
        return f'< User:  {self.__id} {self.__discord_id} {self.__name}>'


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
    def discord_id(self):
        return self.__discord_id

    @discord_id.setter
    def discord_id(self, discord_id):
        self.__discord_id = discord_id

    @discord_id.deleter
    def discord_id(self):
        del self.__discord_id

    @hybrid_property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name