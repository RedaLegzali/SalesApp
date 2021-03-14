
from flask_restful import Resource
from abc import ABC , abstractmethod

class FinalMeta(type(ABC), type(Resource)):
    pass

class Api(ABC,Resource,metaclass=FinalMeta):

    def __init__(self):
        self.create_model()

    @abstractmethod
    def create_model(self):
        pass
