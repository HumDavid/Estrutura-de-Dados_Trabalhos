## Exercício: 2.
## Implemente a classe de árvore binária ArrayBinaryTree usando a representação baseada
## em array descrita na Seção 8.3.2. Implemente as mesmas funções presentes na classe Linked-
## BinaryTree.

from Trees import BinaryTree

class ArrayBinaryTree(BinaryTree):
    class Position(BinaryTree.Position):
        def __init__(self, container, index):
            self._container = container
            self._index = index
        
        def element(self):
            return self._container._data[self._index]
        
        def __eq__(self, other):
            return (type(other) is type(self) and 
                   other._container is self._container and
                   other._index == self._index)
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be of type Position')
        if p._container is not self:
            raise ValueError('p does not belong in this container')
        if p._index < 0 or p._index >= len(self._data):
            raise ValueError('invalid index')
        if self._data[p._index] is None:
            raise ValueError('p is not a valid position')
        return p._index
    
    def _make_position(self, index):
        if 0 <= index < len(self._data) and self._data[index] is not None:
            return self.Position(self, index)
        return None
    
    def __init__(self):
        self._data = []
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def _resize_to_index(self, index):
        if index >= len(self._data):
            new_length = index + 1
            self._data.extend([None] * (new_length - len(self._data)))
    
    def root(self):
        if self.is_empty():
            return None
        return self._make_position(0)
    
    def parent(self, p):
        index = self._validate(p)
        if index == 0:
            return None
        parent_idx = (index - 1) // 2
        return self._make_position(parent_idx)
    
    def left(self, p):
        index = self._validate(p)
        left_idx = 2 * index + 1
        return self._make_position(left_idx)
    
    def right(self, p):
        index = self._validate(p)
        right_idx = 2 * index + 2
        return self._make_position(right_idx)
    
    def num_children(self, p):
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1
        return count
    
    def _add_root(self, e):
        if not self.is_empty():
            raise ValueError('Root already exists')
        
        if len(self._data) == 0:
            self._data.append(e)
        else:
            self._data[0] = e
        
        self._size = 1
        return self._make_position(0)
    
    def _add_left(self, p, e):
        index = self._validate(p)
        left_idx = 2 * index + 1
        
        if left_idx < len(self._data) and self._data[left_idx] is not None:
            raise ValueError('Left child already exists')
        
        self._resize_to_index(left_idx)
        
        self._data[left_idx] = e
        self._size += 1
        return self._make_position(left_idx)
    
    def _add_right(self, p, e):
        index = self._validate(p)
        right_idx = 2 * index + 2
        
        if right_idx < len(self._data) and self._data[right_idx] is not None:
            raise ValueError('Right child already exists')
        
        self._resize_to_index(right_idx)
        
        self._data[right_idx] = e
        self._size += 1
        return self._make_position(right_idx)
    
    def _replace(self, p, e):
        index = self._validate(p)
        old = self._data[index]
        self._data[index] = e
        return old
    
    def _delete(self, p):
        index = self._validate(p)
        old = self._data[index]
        
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(self._data) and self._data[left] is not None:
            self._data[index] = self._data[left]
            self._data[left] = None
        elif right < len(self._data) and self._data[right] is not None:
            self._data[index] = self._data[right]
            self._data[right] = None
        else:
            self._data[index] = None
        
        self._size -= 1
        return old
    
    def _delete_subtree(self, index):
        if index >= len(self._data) or self._data[index] is None:
            return
        
        self._data[index] = None
        self._size -= 1
        
        self._delete_subtree(2 * index + 1)
        self._delete_subtree(2 * index + 2)
    
    def positions(self):
        return self.inorder()
    
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    
    def _subtree_inorder(self, p):
        left = self.left(p)
        if left is not None:
            for other in self._subtree_inorder(left):
                yield other
        
        yield p
        
        right = self.right(p)
        if right is not None:
            for other in self._subtree_inorder(right):
                yield other
    
    def print_array(self):
        print("Array:", end=" ")
        for i, val in enumerate(self._data):
            if val is None:
                print(f"[{i}: None]", end=" ")
            else:
                print(f"[{i}: {val}]", end=" ")
        print()

if __name__ == '__main__':
    T = ArrayBinaryTree()
    r = T._add_root('A')
    T._add_left(r, 'B')
    T._add_right(r, 'C')

    for p in T.inorder():
        print(p.element(), end=' ')