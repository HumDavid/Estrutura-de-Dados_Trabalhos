## Exercício: 2.
## Implemente a classe de árvores AVL AVLTreeMap descrita na Seção 11.3.2.

from exercicio_01 import TreeMap

class AVLTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        __slots__ = '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0
        
        def left_height(self):
            return self._left._height if self._left is not None else 0
        
        def right_height(self):
            return self._right._height if self._right is not None else 0
    
    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _isbalanced(self, p):
        return abs(p._node.left_height() - p._node.right_height()) <= 1
    
    def _tall_child(self, p, favorleft=False):
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)
    
    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)
    
    def _rotate_left(self, z_node):
        y = z_node._right
        if y is None:
            return z_node
        z_node._right = y._left
        if y._left is not None:
            y._left._parent = z_node
        y._parent = z_node._parent
        if z_node is self._root:
            self._root = y
        else:
            parent = z_node._parent
            if parent._left is z_node:
                parent._left = y
            else:
                parent._right = y
        y._left = z_node
        z_node._parent = y
        return y

    def _rotate_right(self, z_node):
        y = z_node._left
        if y is None:
            return z_node
        z_node._left = y._right
        if y._right is not None:
            y._right._parent = z_node
        y._parent = z_node._parent
        if z_node is self._root:
            self._root = y
        else:
            parent = z_node._parent
            if parent._left is z_node:
                parent._left = y
            else:
                parent._right = y
        y._right = z_node
        z_node._parent = y
        return y

    def _restructure(self, x):
        y = self.parent(x)
        z = self.parent(y)
        
        if (x == self.left(y)) == (y == self.left(z)):
            if y == self.left(z):
                new_root_node = self._rotate_right(z._node)
            else:
                new_root_node = self._rotate_left(z._node)
            return self._make_position(new_root_node)
        else:
            if x == self.right(y) and y == self.left(z):
                self._rotate_left(y._node)
                new_root_node = self._rotate_right(z._node)
                return self._make_position(new_root_node)
            else:
                self._rotate_right(y._node)
                new_root_node = self._rotate_left(z._node)
                return self._make_position(new_root_node)
    
    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height
            if not self._isbalanced(p):
                p = self._restructure(self._tall_grandchild(p))
                leftp = self.left(p)
                rightp = self.right(p)
                if leftp is not None:
                    self._recompute_height(leftp)
                if rightp is not None:
                    self._recompute_height(rightp)
            self._recompute_height(p)
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent(p)
    
    def _rebalance_insert(self, p):
        self._rebalance(p)
    
    def _rebalance_delete(self, p):
        self._rebalance(p)


if __name__ == "__main__":
    avl = AVLTreeMap()
    avl[1] = "um"
    avl[2] = "dois"
    avl[3] = "três"
    print(f"Tamanho: {len(avl)}")