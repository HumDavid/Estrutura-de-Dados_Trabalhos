## Exercício: 7
## Considere a sequência de chaves (5,16,22,45,2,10,18,30,50,12,1). Desenhe o resultado da inserção
## de entradas com essas chaves (na ordem dada) em uma árvore rubro-negra inicialmente vazia.

from exercicio_03 import RedBlackTreeMap

def print_tree_rb(tree):
    def _print(node, prefix="", is_left=True):
        if node is not None:
            color = "R" if node._red else "B"
            connector = "└── " if is_left else "┌── "
            print(prefix + connector + f"{node._element._key}({color})")

            if node._right or node._left:
                if node._right:
                    _print(
                        node._right,
                        prefix + ("    " if is_left else "│   "),
                        False
                    )
                if node._left:
                    _print(
                        node._left,
                        prefix + ("    " if is_left else "│   "),
                        True
                    )

    if tree.is_empty():
        print("Árvore vazia")
    else:
        _print(tree._root)
        print("-" * 50)


avl = RedBlackTreeMap()
for k in [5,16,22,45,2,10,18,30,50,12,1]:
    avl[k] = k
print("Árvore:")
print_tree_rb(avl)