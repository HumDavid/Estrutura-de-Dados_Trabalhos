##  Exercício: 12.
##  Implemente as classes LinkedStack, LinkedQueue, CircularQueue e LinkedDeque.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop de pilha vazia")
        
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek de pilha vazia")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return "Topo -> " + " -> ".join(items) + " -> Fim"
   
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue(self, item):
        new_node = Node(item)
        
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        
        self.rear = new_node
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue de fila vazia")
        
        item = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        self.size -= 1
        return item
    
    def first(self):
        if self.is_empty():
            raise IndexError("First de fila vazia")
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next
        return "Frente -> " + " -> ".join(items) + " -> Trás"

class CircularQueue:
    def __init__(self):
        self.tail = None
        self.size = 0
    
    def enqueue(self, item):
        new_node = Node(item)
        
        if self.is_empty():
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue de fila circular vazia")
        
        head = self.tail.next
        
        if head == self.tail:
            self.tail = None
        else:
            self.tail.next = head.next
        
        self.size -= 1
        return head.data
    
    def first(self):
        if self.is_empty():
            raise IndexError("First de fila circular vazia")
        return self.tail.next.data
    
    def is_empty(self):
        return self.tail is None
    
    def rotate(self):
        if not self.is_empty():
            self.tail = self.tail.next
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.is_empty():
            return "Fila Circular: []"
        
        items = []
        current = self.tail.next
        first = self.tail.next
        
        while True:
            items.append(str(current.data))
            current = current.next
            if current == first:
                break
        
        return "Circular -> " + " -> ".join(items) + " -> ..."

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def add_first(self, item):
        new_node = DoublyNode(item)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        
        self.size += 1
    
    def add_last(self, item):
        new_node = DoublyNode(item)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
    
    def remove_first(self):
        if self.is_empty():
            raise IndexError("Remove_first de deque vazio")
        
        item = self.front.data
        
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        
        self.size -= 1
        return item
    
    def remove_last(self):
        if self.is_empty():
            raise IndexError("Remove_last de deque vazio")
        
        item = self.rear.data
        
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        
        self.size -= 1
        return item
    
    def first(self):
        if self.is_empty():
            raise IndexError("First de deque vazio")
        return self.front.data
    
    def last(self):
        if self.is_empty():
            raise IndexError("Last de deque vazio")
        return self.rear.data
    
    def is_empty(self):
        return self.front is None
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next
        return "Frente <- " + " <-> ".join(items) + " <- Trás"


## exemplos
if __name__ == '__main__':
    print('===================== linked stack =====================')
    lstack = LinkedStack()
    print('vazio?:', lstack.is_empty())
    for i in range(5):
        lstack.push(i+1)
        print(f'lstack.push({i+1})')
    print('peek:', lstack.peek())
    print(lstack)
    print('pop():', lstack.pop())
    print(lstack)
    print('len():', lstack.__len__())
    print('vazio?:', lstack.is_empty())

    print('===================== linked queue =====================')
    lqueue = LinkedQueue()
    print('vazio?:', lqueue.is_empty())
    for i in range(5):
        lqueue.enqueue(i+1)
        print(f'lqueue.enqueue({i+1})')
    print('first:', lqueue.first())
    print(lqueue)
    print('dequeue():', lqueue.dequeue())
    print(lqueue)
    print('len():', lqueue.__len__())
    print('vazio?:', lqueue.is_empty())

    print('==================== circular queue ====================')
    cqueue = CircularQueue()
    print('vazio?:', cqueue.is_empty())
    for i in range(5):
        cqueue.enqueue(i+1)
        print(f'cqueue.enqueue({i+1})')
    print('first:', cqueue.first())
    print(cqueue)
    print('dequeue():', cqueue.dequeue())
    print(cqueue)
    print('len():', cqueue.__len__())
    print('vazio?:', cqueue.is_empty())


    print('===================== linked deque =====================')
    ldeque = LinkedDeque()
    print('vazio?:', ldeque.is_empty())
    for i in range(2):
        ldeque.add_first(2-i)
        print(f'ldeque.add_first({2-i})')
        ldeque.add_last(2+i+1)
        print(f'ldeque.add_last({2+i+1})')
    print('first:', ldeque.first())
    print('last:', ldeque.last())
    print('len():', ldeque.__len__())
    print(ldeque)
    print('remove_first():', ldeque.remove_first())
    print('remove_last():', ldeque.remove_last())
    print(ldeque)
    print('vazio?:', ldeque.is_empty())