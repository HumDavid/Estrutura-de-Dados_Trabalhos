from exercicio12 import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        # add no fim da lista
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        
    def prepend(self, data):
        # add no início da lista
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.size += 1
        
    def insert_at(self, position, data):
        # add em pos específica
        if position < 0 or position > self.size:
            raise IndexError(f"Posição {position} fora dos limites [0, {self.size}]")
        
        if position == 0:
            self.prepend(data)
        elif position == self.size:
            self.append(data)
        else:
            new_node = Node(data)
            current = self.head
            
            for _ in range(position - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            self.size += 1
    
    def remove_first(self):
        if self.is_empty():
            raise IndexError("Remoção de lista vazia")
        
        removed_data = self.head.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        
        self.size -= 1
        return removed_data
    
    def remove_last(self):
        if self.is_empty():
            raise IndexError("Remoção de lista vazia")
        
        removed_data = self.tail.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            # PENULTIMO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            while current.next != self.tail:
                current = current.next
            
            current.next = None
            self.tail = current
        
        self.size -= 1
        return removed_data
    
    def remove_at(self, position):
        if position < 0 or position >= self.size:
            raise IndexError(f"Posição {position} fora dos limites [0, {self.size-1}]")
        
        if position == 0:
            return self.remove_first()
        elif position == self.size - 1:
            return self.remove_last()
        else:
            current = self.head
            
            for _ in range(position - 1):
                current = current.next
            
            node_to_remove = current.next
            removed_data = node_to_remove.data
            
            current.next = node_to_remove.next
            
            self.size -= 1
            return removed_data
    
    def remove_value(self, value):
        if self.is_empty():
            return False
        
        if self.head.data == value:
            self.remove_first()
            return True
        
        current = self.head
        while current.next is not None and current.next.data != value:
            current = current.next
        
        if current.next is None:
            return False
        
        node_to_remove = current.next
        
        if node_to_remove == self.tail:
            self.tail = current
        
        current.next = node_to_remove.next
        self.size -= 1
        return True
    
    def search(self, value):
        current = self.head
        position = 0
        
        while current is not None:
            if current.data == value:
                return True, position
            current = current.next
            position += 1
        
        return False, -1
    
    def get_at(self, position):
        if position < 0 or position >= self.size:
            raise IndexError(f"Posição {position} fora dos limites [0, {self.size-1}]")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        return current.data
    
    def update_at(self, position, new_value):
        if position < 0 or position >= self.size:
            raise IndexError(f"Posição {position} fora dos limites [0, {self.size-1}]")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        current.data = new_value
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.is_empty():
            return "LinkedList: []"
        
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        
        return f"LinkedList: [{' -> '.join(elements)}]"
    
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next
    
    def reverse(self):
        if self.size <= 1:
            return
        
        prev = None
        current = self.head
        self.tail = self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def copy(self):
        new_list = LinkedList()
        current = self.head
        while current is not None:
            new_list.append(current.data)
            current = current.next
        return new_list
    
    def count(self, value):
        count = 0
        current = self.head
        while current is not None:
            if current.data == value:
                count += 1
            current = current.next
        return count
    
    def index(self, value):
        current = self.head
        position = 0
        while current is not None:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1

class CircularList:
    def __init__(self):
        self.tail = None
        self.size = 0
        
    def is_empty(self):
        return self.tail is None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        
    def prepend(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
        
        self.size += 1
        
    def insert_at(self, position, data):
        if position < 0 or position > self.size:
            raise IndexError(f"Posição {position} fora dos limites [0, {self.size}]")
        
        if position == 0:
            self.prepend(data)
        elif position == self.size:
            self.append(data)
        else:
            new_node = Node(data)
            
            current = self.tail.next
            for _ in range(position - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            self.size += 1
    
    def remove_first(self):
        if self.is_empty():
            raise IndexError("Remoção de lista vazia")
        
        first_node = self.tail.next
        removed_data = first_node.data
        
        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = first_node.next
        
        self.size -= 1
        return removed_data
    
    def remove_last(self):
        if self.is_empty():
            raise IndexError("Remoção de lista vazia")
        
        if self.size == 1:
            removed_data = self.tail.data
            self.tail = None
            self.size = 0
            return removed_data
        
        current = self.tail.next
        while current.next != self.tail:
            current = current.next
        
        removed_data = self.tail.data
        current.next = self.tail.next
        self.tail = current
        
        self.size -= 1
        return removed_data
    
    def remove_at(self, position):
        if position < 0 or position >= self.size:
            raise IndexError(f"Posição {position} fora dos limites [0, {self.size-1}]")
        
        if position == 0:
            return self.remove_first()
        elif position == self.size - 1:
            return self.remove_last()
        else:
            current = self.tail.next
            
            for _ in range(position - 1):
                current = current.next
            
            node_to_remove = current.next
            removed_data = node_to_remove.data
            
            current.next = node_to_remove.next
            
            self.size -= 1
            return removed_data
    
    def remove_value(self, value):
        if self.is_empty():
            return False
        
        if self.tail.next.data == value:
            self.remove_first()
            return True
        
        current = self.tail.next
        while True:
            next_node = current.next
            
            if next_node.data == value:
                if next_node == self.tail:
                    self.tail = current
                
                current.next = next_node.next
                self.size -= 1
                return True
            
            current = next_node
            
            if current == self.tail.next:
                break
        
        return False
    
    def search(self, value):
        if self.is_empty():
            return False, -1
        
        current = self.tail.next
        position = 0
        
        while True:
            if current.data == value:
                return True, position
            
            current = current.next
            position += 1
            
            if current == self.tail.next:
                break
        
        return False, -1
    
    def get_at(self, position):
        if position < 0 or position >= self.size:
            raise IndexError(f"Posição {position} fora dos limites [0, {self.size-1}]")
        
        current = self.tail.next
        for _ in range(position):
            current = current.next
        
        return current.data
    
    def update_at(self, position, new_value):
        if position < 0 or position >= self.size:
            raise IndexError(f"Posição {position} fora dos limites [0, {self.size-1}]")
        
        current = self.tail.next
        for _ in range(position):
            current = current.next
        
        current.data = new_value
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.is_empty():
            return "CircularList: []"
        
        elements = []
        current = self.tail.next
        first = current
        
        while True:
            elements.append(str(current.data))
            current = current.next
            
            if current == first:
                break
        
        return f"CircularList: [{' → '.join(elements)} → ...]"
    
    def display(self, num_elements=None):
        if self.is_empty():
            print("Lista circular vazia")
            return
        
        elements = []
        current = self.tail.next
        count = 0
        
        while True:
            elements.append(str(current.data))
            current = current.next
            count += 1
            
            if current == self.tail.next:
                break
            
            if num_elements is not None and count >= num_elements:
                elements.append("...")
                break
        
        print(f"Circular List: {' → '.join(elements)} → ...")
    
    def rotate(self, steps=1):
        if self.is_empty() or self.size == 1:
            return
        
        for _ in range(steps):
            self.tail = self.tail.next
    
    def get_first(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        
        return self.tail.next.data
    
    def get_last(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        
        return self.tail.data
    
    def clear(self):
        self.tail = None
        self.size = 0
    
    def copy(self):
        new_list = CircularList()
        
        if self.is_empty():
            return new_list
        
        current = self.tail.next
        first = current
        
        while True:
            new_list.append(current.data)
            current = current.next
            
            if current == first:
                break
        
        return new_list
    
    def count(self, value):
        if self.is_empty():
            return 0
        
        count = 0
        current = self.tail.next
        first = current
        
        while True:
            if current.data == value:
                count += 1
            
            current = current.next
            
            if current == first:
                break
        
        return count
    
    def index(self, value):
        if self.is_empty():
            return -1
        
        current = self.tail.next
        position = 0
        first = current
        
        while True:
            if current.data == value:
                return position
            
            current = current.next
            position += 1
            
            if current == first:
                break
        
        return -1
    
    def to_list(self):
        if self.is_empty():
            return []
        
        result = []
        current = self.tail.next
        first = current
        
        while True:
            result.append(current.data)
            current = current.next
            
            if current == first:
                break
        
        return result
    
    def reverse(self):
        if self.size <= 1:
            return
        
        prev = self.tail
        current = self.tail.next
        first = current
        
        while True:
            next_node = current.next
            current.next = prev
            
            prev = current
            current = next_node
            
            if current == first:
                break
        
        self.tail = first
    
    def josephus_problem(self, k):
        if self.is_empty():
            return -1
        
        temp_list = self.copy()
        
        current = temp_list.tail.next
        
        while temp_list.size > 1:
            for _ in range(k - 1):
                current = current.next
            
            next_person = current.next
            
            temp_list.remove_value(current.data)
            
            current = next_person
        
        survivor = temp_list.get_first()
        return self.index(survivor)

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = DoublyNode(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        
    def prepend(self, data):
        new_node = DoublyNode(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
        
    def insert_at(self, position, data):
        if position < 0 or position > self.size:
            raise IndexError(f"Posição {position} fora dos limites [0, {self.size}]")
        
        if position == 0:
            self.prepend(data)
        elif position == self.size:
            self.append(data)
        else:
            new_node = DoublyNode(data)
            
            if position < self.size // 2:
                current = self.head
                for _ in range(position - 1):
                    current = current.next
                
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node
            else:
                current = self.tail
                steps_from_end = self.size - position
                
                for _ in range(steps_from_end):
                    current = current.prev
                
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node
            
            self.size += 1
    
    def remove_first(self):
        if self.is_empty():
            raise IndexError("Remoção de lista vazia")
        
        removed_data = self.head.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.size -= 1
        return removed_data
    
    def remove_last(self):
        if self.is_empty():
            raise IndexError("Remoção de lista vazia")
        
        removed_data = self.tail.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size -= 1
        return removed_data
    
    def remove_at(self, position):
        if position < 0 or position >= self.size:
            raise IndexError(f"Posição {position} fora dos limites [0, {self.size-1}]")
        
        if position == 0:
            return self.remove_first()
        elif position == self.size - 1:
            return self.remove_last()
        else:
            if position < self.size // 2:
                current = self.head
                for _ in range(position):
                    current = current.next
            else:
                current = self.tail
                steps_from_end = self.size - position - 1
                
                for _ in range(steps_from_end):
                    current = current.prev
            
            removed_data = current.data
            
            current.prev.next = current.next
            current.next.prev = current.prev
            
            self.size -= 1
            return removed_data
    
    def remove_value(self, value):
        if self.is_empty():
            return False
        
        current = self.head
        while current is not None:
            if current.data == value:
                if current == self.head:
                    self.remove_first()
                elif current == self.tail:
                    self.remove_last()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.next
                    self.size -= 1
                return True
            
            current = current.next
        
        return False
    
    def search(self, value):
        current = self.head
        position = 0
        
        while current is not None:
            if current.data == value:
                return True, position
            
            current = current.next
            position += 1
        
        return False, -1
    
    def search_from_end(self, value):
        current = self.tail
        position_from_end = 0
        
        while current is not None:
            if current.data == value:
                return True, position_from_end
            
            current = current.prev
            position_from_end += 1
        
        return False, -1
    
    def get_at(self, position):
        if position < 0 or position >= self.size:
            raise IndexError(f"Posição {position} fora dos limites [0, {self.size-1}]")
        
        if position < self.size // 2:
            current = self.head
            for _ in range(position):
                current = current.next
        else:
            current = self.tail
            steps_from_end = self.size - position - 1
            
            for _ in range(steps_from_end):
                current = current.prev
        
        return current.data
    
    def update_at(self, position, new_value):
        if position < 0 or position >= self.size:
            raise IndexError(f"Posição {position} fora dos limites [0, {self.size-1}]")
        
        if position < self.size // 2:
            current = self.head
            for _ in range(position):
                current = current.next
        else:
            current = self.tail
            steps_from_end = self.size - position - 1
            
            for _ in range(steps_from_end):
                current = current.prev
        
        current.data = new_value
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.is_empty():
            return "DoublyLinkedList: []"
        
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        
        return f"DoublyLinkedList: [{' <-> '.join(elements)}]"
    
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next
    
    def reverse(self):
        if self.size <= 1:
            return
        
        current = self.head
        self.head = self.tail
        self.tail = current
        
        while current is not None:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            
            current = next_node
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def copy(self):
        new_list = DoublyLinkedList()
        current = self.head
        while current is not None:
            new_list.append(current.data)
            current = current.next
        return new_list
    
    def count(self, value):
        count = 0
        current = self.head
        while current is not None:
            if current.data == value:
                count += 1
            current = current.next
        return count
    
    def index(self, value):
        current = self.head
        position = 0
        while current is not None:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1
    
    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result