## Exercício: 7.
## Dada uma árvore binária, encontre todos os ancestrais de um nó específico nela.

from exercicio_03 import LinkedBinaryTree

def find_ancestors(tree, p):
    ancestors = []
    current = tree.parent(p)
    
    while current is not None:
        ancestors.append(current.element())
        current = tree.parent(current)
    
    return ancestors

if __name__ == "__main__":
    T = LinkedBinaryTree()

    n1 = T._add_root(1)

    n2 = T._add_left(n1, 2)
    n3 = T._add_right(n1, 3)

    n4 = T._add_left(n2, 4)
    n5 = T._add_right(n2, 5)
    n6 = T._add_left(n3, 6)
    n7 = T._add_right(n3, 7)

    n8 = T._add_left(n6, 8)
    n9 = T._add_right(n7, 9)

    print("Os ancestrais do nó 9 são", find_ancestors(T, n9))
    print("Os ancestrais do nó 6 são", find_ancestors(T, n6))
    print("Os ancestrais do nó 5 são", find_ancestors(T, n5))