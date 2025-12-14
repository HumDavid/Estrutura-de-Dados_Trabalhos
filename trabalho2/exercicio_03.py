## Exercício: 3.
## Implemente as funções Postorder, Inorder e Preorder Traversal (seção 8.4.4) para a
## classe LinkedBinaryTree.

from Trees import BinaryTree

class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    
    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
    
    def positions(self):
        return self.inorder()
    
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
    
    def _subtree_preorder(self, p):
        yield p
        for child in self.children(p):
            for other in self._subtree_preorder(child):
                yield other
    
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    
    def _subtree_inorder(self, p):
        left_child = self.left(p)
        if left_child is not None:
            for other in self._subtree_inorder(left_child):
                yield other
        
        yield p
        
        right_child = self.right(p)
        if right_child is not None:
            for other in self._subtree_inorder(right_child):
                yield other
    
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    
    def _subtree_postorder(self, p):
        for child in self.children(p):
            for other in self._subtree_postorder(child):
                yield other
        yield p
    
    def breadthfirst(self):
        if not self.is_empty():
            from collections import deque
            fringe = deque()
            fringe.append(self.root())
            while fringe:
                p = fringe.popleft()
                yield p
                for child in self.children(p):
                    fringe.append(child)
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None
    
    def __init__(self):
        self._root = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def root(self):
        return self._make_position(self._root)
    
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    def _add_root(self, e):
        if self._root is not None: 
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None: 
            raise ValueError('left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)
    
    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None: 
            raise ValueError('right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)
    
    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    
    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2: 
            raise ValueError('p had has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element
    
    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p): 
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

if __name__ == '__main__':
    print("=" * 50)
    print("="*16 + " LinkedBinaryTree " + "="*16)
    print("=" * 50)
    
    print("\n" + "-"*50)
    print("-"*20 + " ÁRVORE 1 " + "-"*20 + "\n")

    T = LinkedBinaryTree()
    
    root = T._add_root('A')
    B = T._add_left(root, 'B')
    C = T._add_right(root, 'C')
    D = T._add_left(B, 'D')
    E = T._add_right(B, 'E')
    F = T._add_left(C, 'F')
    G = T._add_right(C, 'G')
    H = T._add_left(D, 'H')
    
    print(f"Tamanho da árvore: {len(T)}")
    print(f"Altura da árvore: {T.height()}")
    
    print("\nPreorder: ", end="")
    for pos in T.preorder():
        print(pos.element(), end=" ")
    print()
    
    print("Inorder: ", end="")
    for pos in T.inorder():
        print(pos.element(), end=" ")
    print()
    
    print("Postorder: ", end="")
    for pos in T.postorder():
        print(pos.element(), end=" ")
    print()
    
    print("Breadth-first: ", end="")
    for pos in T.breadthfirst():
        print(pos.element(), end=" ")
    print()
    
    print("\n" + "-"*50)
    print("-"*20 + " ÁRVORE 2 " + "-"*20 + "\n")
    
    T2 = LinkedBinaryTree()

    r = T2._add_root(1)
    l = T2._add_left(r, 2)
    r2 = T2._add_right(r, 3)
    T2._add_left(l, 4)
    T2._add_right(l, 5)
    T2._add_left(r2, 6)
    T2._add_right(r2, 7)
    
    print(f"Tamanho da árvore: {len(T2)}")
    print(f"Altura da árvore: {T2.height()}")
    
    print("\nPreorder:  ", end="")
    for p in T2.preorder():
        print(p.element(), end=" ")
    
    print("\nInorder:   ", end="")
    for p in T2.inorder():
        print(p.element(), end=" ")
    
    print("\nPostorder: ", end="")
    for p in T2.postorder():
        print(p.element(), end=" ")
    
    print("\nBreadthfirst: ", end="")
    for p in T2.breadthfirst():
        print(p.element(), end=" ")
    print()