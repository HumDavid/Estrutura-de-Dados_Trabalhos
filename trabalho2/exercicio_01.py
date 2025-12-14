## Exercício: 1.
## Implemente a classe de árvores binárias LinkedBinaryTree usando uma
## estrutura encadeada conforme descrito na Se ̧cão 8.3.1.

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
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
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
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None: raise ValueError('left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)
    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None: raise ValueError('right child exists')
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
        if self.num_children(p) == 2: raise ValueError('p had has two children')
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
        if not self.is_leaf(p): raise ValueError('position must be leaf')
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


## exemplos

if __name__ == '__main__':
    print("=" * 50)
    print("="*16 + " LinkedBinaryTree " + "="*16)
    print("=" * 50)
    
    print("\n" + "-"*50 + "\n")
    T = LinkedBinaryTree()
    print("tree = LinkedBinaryTree()\n")

    print(f"Árvore vazia? {T.is_empty()}")
    print(f"Tamanho: {len(T)}")
    
    print("\n" + "-"*50 + "\n")
    try:
        root = T._add_root('A')
        print("root = tree._add_root('A')\n")    

        print(f"Raiz adicionada: {root.element()}")
        print(f"Tamanho: {len(T)}")
        print(f"Árvore vazia? {T.is_empty()}")
        print(f"É raiz? {T.is_root(root)}")
        print(f"É folha? {T.is_leaf(root)}")
    except Exception as e:
        print(f"Erro ao adicionar raiz: {e}")

    
    print("\n" + "-"*50 + "\n")
    try:
        left_child = T._add_left(root, 'B')
        print("left_child = tree._add_left(root, 'B')")
        right_child = T._add_right(root, 'C')
        print("right_child = tree._add_right(root, 'B')\n")

        print(f"Filho esquerdo de {root.element()}: {left_child.element()}")
        print(f"Filho direito de {root.element()}: {right_child.element()}")
        print(f"Tamanho: {len(T)}")
        print(f"É folha (raiz)? {T.is_leaf(root)}")
        print(f"É folha (B)? {T.is_leaf(left_child)}")
        print(f"É folha (C)? {T.is_leaf(right_child)}")
    except Exception as e:
        print(f"Erro ao adicionar filhos: {e}")
    
    
    print("\n" + "-"*50 + "\n")
    try:
        print(f"Pai de B: {T.parent(left_child).element()}")
        print(f"Pai de C: {T.parent(right_child).element()}")
        print(f"Irmão de B: {T.sibling(left_child).element()}")
        print(f"Irmão de C: {T.sibling(right_child).element()}")
        print(f"Número de filhos de A: {T.num_children(root)}")
        print(f"Número de filhos de B: {T.num_children(left_child)}")
    except Exception as e:
        print(f"Erro em relações familiares: {e}")
    
    print("\n" + "-"*50 + "\n")
    try:
        D = T._add_left(left_child, 'D')
        print("D = tree._add_left(left_child, 'D')\n")

        print(f"Profundidade de A: {T.depth(root)}")
        print(f"Profundidade de B: {T.depth(left_child)}")
        print(f"Profundidade de D: {T.depth(D)}")
        print(f"Altura da árvore: {T.height()}")
        print(f"Altura de B: {T.height(left_child)}")
        print(f"Altura de D: {T.height(D)}")
    except Exception as e:
        print(f"Erro em profundidade/altura: {e}")
    
    print("\n" + "-"*50 + "\n")
    try:
        old = T._replace(right_child, 'X')
        print("old = tree._replace(right_child, 'X')\n")

        print(f"Substituído em C: {old} por {right_child.element()}")
        
        print("Travessia inorder: ", end="")
        for pos in T.inorder():
            print(pos.element(), end=" ")
        print()
    except Exception as e:
        print(f"Erro em substituição/travessia: {e}")
    
    print("\n" + "-"*50 + "\n")
    try:
        removed = T._delete(D)
        print("removed = tree._delete(D)\n")

        print(f"Removido: {removed}")
        print(f"Tamanho após remoção: {len(T)}")
        print(f"B é folha agora? {T.is_leaf(left_child)}")
    except Exception as e:
        print(f"Erro em remoção: {e}")
    
    print("\n" + "-"*50 + "\n")
    try:
        T1 = LinkedBinaryTree()
        print("T1 = LinkedBinaryTree()")
        r1 = T1._add_root('Y')
        print("r1 = T1._add_root('Y')")
        T1._add_left(r1, 'Z')
        print("T1._add_left(r1, 'Z')\n")
        
        T2 = LinkedBinaryTree()
        print("T2 = LinkedBinaryTree()")
        r2 = T2._add_root('W')
        print("r2 = T2._add_root('W')\n")
        
        T._attach(left_child, T1, T2)
        print("tree._attach(left_child, T1, T2)\n")

        print(f"Tamanho após anexação: {len(T)}")
        print(f"T1 está vazia? {T1.is_empty()}")
        print(f"T2 está vazia? {T2.is_empty()}")
    except Exception as e:
        print(f"Erro em anexação: {e}")
    
    print("\n" + "-"*50 + "\n")
    try:
        T._add_left(root, 'Já existe')
    except ValueError as e:
        print(f"Erro esperado ao adicionar filho onde já existe: {e}")
    
    try:
        T._add_root('Nova raiz')
    except ValueError as e:
        print(f"Erro esperado ao adicionar segunda raiz: {e}")
    