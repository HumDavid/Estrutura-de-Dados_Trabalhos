## Exercício: 6
## Desenhe a árvore AVL resultante da remoção da entrada com a chave 62 da  ́arvore AVL da
## Figura 11.14b.

from exercicio_02 import AVLTreeMap
from exercicio_04 import print_tree

avl = AVLTreeMap()

for k in [44, 17, 62, 32, 50, 78, 48, 54, 88]:
    avl[k] = k

print("Antes de remover 62:")
print_tree(avl)

del avl[62]

print("Depois de remover 62:")
print_tree(avl)