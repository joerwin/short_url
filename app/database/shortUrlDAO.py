import abc

class ShortUrlDAO(object): 
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def find(self, encodedPath):
        """Retrieve data from the data store"""
        return
    
    @abc.abstractmethod
    def create(self, url):
        """Create a new entry for the url and return its id"""
        return

    @abc.abstractmethod
    def delete(self, url):
        pass


