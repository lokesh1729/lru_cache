from models.cache import Cache

class LRUCache(Cache):
    def get(self, key):
        if key not in self.cache:
            return -1
        result = self.cache[key]
        self.strategy.get_key(key)
        return result
    
    def put(self, key, value):
        if len(self.cache) == self.size:
            evict_key = self.strategy.evict()
            del self.cache[evict_key]
        self.cache[key] = value
        self.strategy.put_key(key)

    def show_cache(self):
        return self.cache
