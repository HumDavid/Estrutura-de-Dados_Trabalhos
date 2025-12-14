## Exercício: 8.
## Dada uma árvore binária, substitua o valor de cada nó pela soma de todos os elementos
## presentes em suas subárvores esquerda e direita. Você pode assumir que o valor de um nó
## filho vazio é 0.

from exercicio_03 import LinkedBinaryTree

def print_binary_tree(T):
    def _print(p, path: list):
        if p is None:
            return
        
        path.append(p.element())
        
        if T.is_leaf(p):
            print(" -> ".join(map(str, path)))
        else:
            left_child = T.left(p)
            if left_child is not None:
                _print(left_child, path)
            
            right_child = T.right(p)
            if right_child is not None:
                _print(right_child, path)
        
        path.pop()
    
    if not T.is_empty():
        _print(T.root(), [])

def replace_with_subtree_sum(T: LinkedBinaryTree):
    def _postorder_sum(p):
        if p is None:
            return 0
        
        left_child = T.left(p)
        right_child = T.right(p)
        
        sum_left = _postorder_sum(left_child)
        sum_right = _postorder_sum(right_child)
        
        original_value = p.element()
        
        new_value = sum_left + sum_right
        
        T._replace(p, new_value)
        
        return original_value + sum_left + sum_right
    
    if not T.is_empty():
        _postorder_sum(T.root())

if __name__ == "__main__":
    T = LinkedBinaryTree()

    n1 = T._add_root(1)

    n2 = T._add_left(n1, 2)
    n3 = T._add_right(n1, 3)

    n4 = T._add_right(n2, 4)
    n5 = T._add_left(n3, 5)
    n6 = T._add_right(n3, 6)

    n7 = T._add_left(n5, 7)
    n8 = T._add_right(n5, 8)

    print("antes:")
    print_binary_tree(T)
    replace_with_subtree_sum(T)
    print("\ndepois:")
    print_binary_tree(T)