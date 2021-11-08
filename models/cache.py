from abc import ABC

class Cache(ABC):
    def __init__(self, size, strategy) -> None:
        self.size = size
        self.strategy = strategy
        self.cache = {}
    
    def get(self, key):
        """
        Get value from cache or return -1
        """
        raise NotImplementedError()

    def put(self, key, value):
        """
        put 
        """
        raise NotImplementedError()
