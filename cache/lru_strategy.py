from models.strategy import CacheStrategy
from models.node import Node


class LRUStrategy(CacheStrategy):
    def __init__(self) -> None:
        super().__init__()
        head = Node(None, None, None)
        tail = Node(None, head, None)
        head.next = tail
        self.head = head
        self.tail = tail
        self.key_to_node = {}
    
    def __add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def __remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def get_key(self, key):
        node = self.key_to_node[key]
        self.__remove_node(node)
        self.__add_node(node)
    
    def put_key(self, key):
        node = Node(key)
        self.__add_node(node)
        self.key_to_node[key] = node

    def evict(self):
        prev_tail = self.tail.prev
        self.__remove_node(prev_tail)
        del self.key_to_node[prev_tail.value]
        return prev_tail.value
