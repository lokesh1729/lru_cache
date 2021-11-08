from cache.lru_cache import LRUCache
from cache.lru_strategy import LRUStrategy

obj = LRUCache(3, LRUStrategy())
obj.put('a', 1)
obj.put('b', 2)
obj.put('c', 3)
# b c a
# d a b
print(obj.get('b'))
print(obj.get('a'))
obj.put('d', 4)
obj.put('c', 10)
obj.put('e', 50)
print(obj.show_cache())
