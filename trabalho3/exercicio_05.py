## Exercício: 5
## Desenhe a árvore AVL resultante da inserção de uma entrada com a chave 52 na árvore AVL da
## Figura 11.14b.

from exercicio_02 import AVLTreeMap
from exercicio_04 import print_tree

avl = AVLTreeMap()

for k in [44, 17, 62, 32, 50, 78, 48, 54, 88]:
    avl[k] = k

print("Árvore antes de inserir 52:")
print_tree(avl)

avl[52] = 52

print("Árvore depois de inserir 52:")
print_tree(avl)