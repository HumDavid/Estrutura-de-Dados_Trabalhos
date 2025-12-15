##  Exercício: 20.
##  Modifique a classe DoublyLinkedBase para incluir um método reverse que inverte a ordem
##  da lista, mas sem criar ou destruir nenhum nó.

class _Node:
    __slots__ = '_element', '_prev', '_next'
    
    def __init__(self, element, prev=None, next=None):
        self._element = element
        self._prev = prev
        self._next = next
    
    def __str__(self):
        return str(self._element)

class DoublyLinkedBase:
    def __init__(self):
        self._header = _Node(None)
        self._trailer = _Node(None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, element, predecessor, successor):
        newest = _Node(element, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
    
    def reverse(self):
        if self._size <= 1:
            return
        
        current = self._header._next
        
        while current != self._trailer:
            temp = current._prev
            current._prev = current._next
            current._next = temp
            current = current._prev
        
        temp = self._header._next
        self._header._next = self._trailer._prev
        self._trailer._prev = temp
        
        if self._header._next:
            self._header._next._prev = self._header
        if self._trailer._prev:
            self._trailer._prev._next = self._trailer

if __name__ == "__main__":
    dll = DoublyLinkedBase()
    dll._insert_between(1, dll._header, dll._trailer)
    dll._insert_between(2, dll._header._next, dll._trailer)
    dll._insert_between(3, dll._header._next._next, dll._trailer)

    dll.reverse()