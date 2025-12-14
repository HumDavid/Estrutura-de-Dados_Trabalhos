##  Exercício: 1.
##  Implemente as classes ArrayStack, ArrayQueue e ArrayDeque.

class ArrayStack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

    def is_empty(self):
        return len(self.stack) == 0
    
    def top(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.stack[-1]
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.stack.pop()
    
    def push(self, obj):
        self.stack.append(obj)
    
class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.queue = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def __str__(self):
        result = []
        index = self.front
        for _ in range(self.size):
            result.append(self.queue[index])
            index = (index + 1) % len(self.queue)
        return str(result)
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.queue[self.front]
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        answer = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)
        self.size -= 1
        return answer

    def enqueue(self, e):
        if self.size == len(self.queue):
            self.resize(2 * len(self.queue))
        avail = (self.front + self.size) % len(self.queue)
        self.queue[avail] = e
        self.size += 1
    
    def resize(self, cap):
        old = self.queue
        self.queue = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.queue[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0

class ArrayDeque:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.deque = [None] * ArrayDeque.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0
    
    def __str__(self):
        result = []
        index = self.front
        for _ in range(self.size):
            result.append(self.deque[index])
            index = (index + 1) % len(self.deque)
        return str(result)
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def add_first(self, e):
        if self.size == len(self.deque):
            self.resize(2 * len(self.deque))
        self.front = (self.front - 1) % len(self.deque)
        self.deque[self.front] = e
        self.size += 1

    def add_last(self, e):
        if self.size == len(self.deque):
            self.resize(2 * len(self.deque))
        avail = (self.front + self.size) % len(self.deque)
        self.deque[avail] = e
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        answer = self.deque[self.front]
        self.deque[self.front] = None
        self.front = (self.front + 1) % len(self.deque)
        self.size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            raise IndexError('Deuqe is empty')
        back_index = (self.front + self.size - 1) % len(self.deque)
        answer = self.deque[back_index]
        self.deque[back_index] = None
        self.size -= 1
        return answer

    def first(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        return self.deque[self.front]

    def last(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        return self.deque[(self.front + self.size - 1) % len(self.deque)]
    
    def resize(self, cap):
        old = self.deque
        self.deque = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.deque[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0
    


if __name__ == '__main__':
    ## exemplos
    print('============ stack ============')
    stack = ArrayStack()

    print('vazio?:', stack.is_empty())

    stack.push(5)
    print('stack.push(5)')

    print('top():', stack.top())

    stack.push(7)
    print('stack.push(7)')
    stack.push(10)
    print('stack.push(10)')

    print('len():', stack.__len__())

    print('pop()', stack.pop())
    print('stack:', stack)

    stack.push(11)
    print('stack.push(11)')
    stack.push(12)
    print('stack.push(12)')
    stack.push(15)
    print('stack.push(15)')
    
    print('len():', stack.__len__())

    print('stack:', stack)

    print('vazio?:', stack.is_empty())

    # queue
    print('============ queue ============')
    queue = ArrayQueue()

    print('vazio?:', queue.is_empty())

    queue.enqueue(5)
    print('queue.enqueue(5)')

    print('top():', queue.dequeue())

    queue.enqueue(7)
    print('queue.enqueue(7)')
    queue.enqueue(10)
    print('queue.enqueue(10)')

    print('len():', queue.__len__())

    print('pop()', queue.dequeue())
    print('queue:', queue)

    queue.enqueue(11)
    print('queue.enqueue(11)')
    queue.enqueue(12)
    print('queue.enqueue(12)')
    queue.enqueue(15)
    print('queue.enqueue(15)')
    
    print('len():', queue.__len__())

    print('queue:', queue)

    print('vazio?:', queue.is_empty())

    # deque
    print('============ deque ============')
    deque = ArrayDeque()

    print('vazio?:', deque.is_empty())

    deque.add_first(3)
    print('deque.add_first(3)')
    deque.add_last(4)
    print('deque.add_last(4)')
    deque.add_first(2)
    print('deque.add_first(2)')
    deque.add_last(5)
    print('deque.add_last(5)')
    deque.add_first(1)
    print('deque.add_first(1)')

    print('len():', deque.__len__())

    print('first:', deque.first())
    print('last:', deque.last())

    print('deque:', deque)

    deque.delete_first()
    print('deque.delete_first()')
    print('deque:', deque)

    deque.delete_last()
    print('deque.delete_last()')
    print('deque:', deque)

    print('len():', deque.__len__())

    print('vazio?:', deque.is_empty())