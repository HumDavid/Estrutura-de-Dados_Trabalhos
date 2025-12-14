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
        
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        
        child_index = None
        left_idx = 2 * index + 1
        right_idx = 2 * index + 2
        
        if left_idx < len(self._data) and self._data[left_idx] is not None:
            child_index = left_idx
        elif right_idx < len(self._data) and self._data[right_idx] is not None:
            child_index = right_idx
        
        element = self._data[index]
        self._data[index] = None
        self._size -= 1
        
        if child_index is not None:
            self._delete_subtree(child_index)
        
        return element
    
    def _delete_subtree(self, index):
        if index >= len(self._data) or self._data[index] is None:
            return
        
        self._data[index] = None
        self._size -= 1
        
        self._delete_subtree(2 * index + 1)
        self._delete_subtree(2 * index + 2)
    
    def _attach(self, p, t1, t2):
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        
        index = self._validate(p)
        
        if not t1.is_empty():
            self._attach_tree(t1, 2 * index + 1)
        
        if not t2.is_empty():
            self._attach_tree(t2, 2 * index + 2)
    
    def _attach_tree(self, tree, index):
        if tree.is_empty():
            return
        
        from collections import deque
        
        queue = deque()
        queue.append((0, index))
        
        while queue:
            src_idx, dst_idx = queue.popleft()
            
            self._resize_to_index(dst_idx)
            
            if src_idx < len(tree._data) and tree._data[src_idx] is not None:
                self._data[dst_idx] = tree._data[src_idx]
                self._size += 1
                
                queue.append((2 * src_idx + 1, 2 * dst_idx + 1))
                queue.append((2 * src_idx + 2, 2 * dst_idx + 2))
    
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
    print("="*85)
    print("="*34 + " ArrayBinaryTree " + "="*34)
    print("="*85)
    
    print("\n" + "-"*85 + "\n")
    T = ArrayBinaryTree()
    print("T = ArrayBinaryTree()")
    root = T._add_root('A')
    print("root = T._add_root('A')")

    print(f"\nRaiz em índice {0}: {root.element()}\n")
    
    B = T._add_left(root, 'B')
    print("B = T._add_left(root, 'B')")
    C = T._add_right(root, 'C')
    print("C = T._add_right(root, 'C')")

    print(f"\nFilho esquerdo de A em índice 1: {B.element()}")
    print(f"Filho direito de A em índice 2: {C.element()}\n")
    
    D = T._add_left(B, 'D')
    print("D = T._add_left(B, 'D')")
    E = T._add_right(B, 'E')
    print("E = T._add_right(B, 'E')")

    print(f"\nFilho esquerdo de B em índice 3: {D.element()}")
    print(f"Filho direito de B em índice 4: {E.element()}\n")
    
    F = T._add_left(C, 'F')
    print("F = T._add_left(C, 'F')")
    G = T._add_right(C, 'G')
    print("G = T._add_right(C, 'G')")

    print(f"\nFilho esquerdo de C em índice 5: {F.element()}")
    print(f"Filho direito de C em índice 6: {G.element()}\n")
    
    H = T._add_left(E, 'H')
    print("H = T._add_left(E, 'H')")

    print(f"\nFilho esquerdo de E em índice 9: {H.element()}\n")
    
    print("Estado do array (com buracos nos índices 7 e 8):")
    T.print_array()
    
    print("\n" + "-"*85 + "\n")
    print(f"Pai de H (índice 9): {(9-1)//2} -> {T.parent(H).element() if T.parent(H) else None}")
    print(f"Filho esquerdo de C (índice 2): {2*2+1} -> {T.left(C).element() if T.left(C) else None}")
    print(f"Filho direito de C (índice 2): {2*2+2} -> {T.right(C).element() if T.right(C) else None}")
    
    print("\n" + "-"*85 + "\n")
    print("Elementos em ordem: ", end="")
    for pos in T.inorder():
        print(pos.element(), end=" ")
    print()
    
    print("\n" + "-"*85 + "\n")
    old = T._replace(H, 'Z')
    print("old = T._replace(H, 'Z')")

    print(f"Substituído {old} por {H.element()} em H")
    
    print("\n" + "-"*85 + "\n")
    print(f"Profundidade de H: {T.depth(H)}")
    print(f"Altura da árvore: {T.height()}")
    print(f"Altura de B: {T.height(B)}")
    
    print("\n" + "-"*85 + "\n")
    print(f"Tamanho antes de deletar D: {len(T)}")

    T._delete(D)
    print("T._delete(D)")

    print(f"Tamanho após deletar D: {len(T)}")
    print("Array após deletar D:")
    T.print_array()