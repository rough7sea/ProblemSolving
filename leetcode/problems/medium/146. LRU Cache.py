from typing import Optional


class Node:
    def __init__(self, key: int, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.key_to_value = dict()
        self.key_to_node = dict()
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __remove_first(self) -> Node | None:
        if self.head:
            return self.__remove_node(self.head.key)
        return None

    def __remove_key(self, key):
        del self.key_to_value[key]
        del self.key_to_node[key]
        pass


    def __remove_node(self, key) -> Node:
        node: Node = self.key_to_node[key]

        if not node.prev:
            self.head = node.next
        else:
            node.prev.next = node.next

        if not node.next:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        return node

    def __add_to_tail(self, node: Node):
        if not self.tail:
            self.tail = node
            self.head = node
            return

        node.next = None
        self.tail.next = node
        node.prev = self.tail
        self.tail = node


    def get(self, key: int) -> int:
        if key not in self.key_to_value:
            return -1

        node = self.__remove_node(key)
        self.__add_to_tail(node)
        return self.key_to_value[key]


    def put(self, key: int, value: int) -> None:
        if key in self.key_to_value:
            self.__remove_node(key)
            self.size -= 1

        node = Node(key=key)
        self.__add_to_tail(node)
        self.key_to_value[key] = value
        self.key_to_node[key] = node

        if self.size >= self.capacity:
            node = self.__remove_first()
            if node:
                self.__remove_key(node.key)
        else:
            self.size += 1



cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))


# cache = LRUCache(2)
# cache.put(2, 1)
# cache.put(1, 1)
# cache.put(2, 3)
# cache.put(4, 1)
# print(cache.get(1))
# print(cache.get(2))