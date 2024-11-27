from abc import ABC, abstractmethod

class Repository(ABC):
    
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def update(self, id, data):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass
