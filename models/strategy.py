import abc

class CacheStrategy(abc.ABC):
    def get_key(self, key):
        raise NotImplementedError()
    
    def put_key(self, key, value):
        raise NotImplementedError()
    
    def evict(self):
        raise NotImplementedError()
