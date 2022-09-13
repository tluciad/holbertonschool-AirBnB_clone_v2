from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, MetaData
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Private class attributes"""
    __engine = None
    __session = None

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        """Engine constructor"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        metadata = MetaData()
        if getenv('HBNB_ENV') == 'test':
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Public instance method all"""
        dict_new = {}

        if cls is None:
            for obj in self.__session.query(City, State, User, Place,
                                            Review, Amenity).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                dict_new[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, obj.id)
                dict_new[key] = obj
        return dict_new

    def new(self, obj):
        """Public instance method new"""
        self.__session.add(obj)

    def save(self):
        """Public instante method save"""
        self.__session.commit()

    def delete(self, obj=None):
        """public instance method delete"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Public instance method reload"""
        Base.metadata.create_all(self.__engine)
        session_new = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_new)
        self.__session = Session()

    def close(self):
        """method on the private session attribute"""
        self.__session.close()
