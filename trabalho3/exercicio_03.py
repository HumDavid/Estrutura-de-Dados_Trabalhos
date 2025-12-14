## Exercício: 3.
## Implemente a classe de árvores rubro-negras RedBlackTreeMap descrita na Seção 11.6.2.

from exercicio_02 import TreeMap

class RedBlackTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        __slots__ = '_red'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._red = True
        
    def _set_red(self, p):
        if p is not None:
            p._node._red = True
    def _set_black(self, p):
        if p is not None:
            p._node._red = False
    def _set_color(self, p, make_red):
        if p is not None:
            p._node._red = make_red
    def _is_red(self, p): return p is not None and p._node._red
    def _is_red_leaf(self, p): return self._is_red(p) and self.is_leaf(p)

    def _get_red_child(self, p):
        for child in (self.left(p), self.right(p)):
            if self._is_red(child):
                return child
        return None
    
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

    def _rotate(self, p):
        if p is None:
            return None
        node = p._node
        parent = node._parent
        if parent is None:
            return p
        if parent._left is node:
            new_root_node = self._rotate_right(parent)
        else:
            new_root_node = self._rotate_left(parent)
        return self._make_position(new_root_node)

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
    
    def _rebalance_insert(self, p):
        self._resolve_red(p)
    
    def _resolve_red(self, p):
        if p is None:
            return
        if self.is_root(p):
            self._set_black(p)
            return
        parent = self.parent(p)
        if not self._is_red(parent):
            return
        uncle = self.sibling(parent)
        if not self._is_red(uncle):
            middle = self._restructure(p)
            self._set_black(middle)
            self._set_red(self.left(middle))
            self._set_red(self.right(middle))
        else:
            grand = self.parent(parent)
            self._set_red(grand)
            self._set_black(self.left(grand))
            self._set_black(self.right(grand))
            self._resolve_red(grand)
    
    def _rebalance_delete(self, p):
        if len(self) == 1:
            self._set_black(self.root())
        elif p is not None:
            n = self.num_children(p)
            if n == 1:
                c = next(self.children(p))
                if not self._is_red_leaf(c):
                    self._fix_deficit(p, c)
            elif n == 2:
                if self._is_red_leaf(self.left(p)):
                    self._set_black(self.left(p))
                else:
                    self._set_black(self.right(p))
    
    def _fix_deficit(self, z, y):
        if not self._is_red(y):
            x = self._get_red_child(y)
            if x is not None:
                old_color = self._is_red(z)
                middle = self._restructure(x)
                self._set_color(middle, old_color)
                self._set_black(self.left(middle))
                self._set_black(self.right(middle))
            else:
                self._set_red(y)
                if self._is_red(z):
                    self._set_black(z)
                elif not self.is_root(z):
                    self._fix_deficit(self.parent(z), self.sibling(z))
        else:
            self._rotate(y)

            self._set_black(y)
            self._set_red(z)

            if z == self.right(y):
                self._fix_deficit(z, self.left(z))
            else:
                self._fix_deficit(z, self.right(z))

if __name__ == "__main__":
    rb = RedBlackTreeMap()
    
    rb[50] = "cinquenta"
    rb[30] = "trinta"
    rb[70] = "setenta"
    rb[20] = "vinte"
    rb[40] = "quarenta"
    rb[60] = "sessenta"
    rb[80] = "oitenta"
    
    print(f"rb[30] = {rb[30]}")
    
    rb[50] = "CINQUENTA"
    
    del rb[30]
    
    print("Chaves em ordem:", list(rb))
    
    print(f"Tamanho: {len(rb)}")
    
    print(f"Raiz é preta? {not rb._is_red(rb.root())}")