## Exercício: 6.
## Dada uma árvore binária, escreva um algoritmo eficiente para imprimir todos os caminhos
## do nó raiz até cada nó folha.

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

if __name__ == "__main__":
    T = LinkedBinaryTree()

    r1 = T._add_root(1)

    rh1 = T._add_right(r1, 3)
    lt1 = T._add_left(r1, 2)

    rh2 = T._add_right(rh1, 7)
    lt2 = T._add_left(rh1, 6)
    
    T._add_right(lt1, 5)
    T._add_left(lt1, 4)

    rh3 = T._add_right(rh2, 9)

    lt3 = T._add_left(lt2, 8)

    print_binary_tree(T)