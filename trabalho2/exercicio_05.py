## Exercício: 5.
## Dada uma árvore binária, verifique se ela é uma árvore soma ou não. Em uma árvore soma, o
## valor de cada nó não folha  ́e igual à soma de todos os elementos presentes em suas subárvores
## esquerda e direita. O valor de um nó folha pode ser qualquer um e o valor de um nó filho
## vazio é considerado 0.

from exercicio_03 import LinkedBinaryTree

def is_sum_tree(T):
    def check(p):
        if p is None:
            return True, 0

        left_ok, left_sum = check(T.left(p))
        right_ok, right_sum = check(T.right(p))

        if T.left(p) is None and T.right(p) is None:
            return True, p.element()

        is_ok = (left_ok and right_ok and p.element() == left_sum + right_sum)

        return is_ok, left_sum + right_sum + p.element()

    if T.is_empty():
        return True

    ok, _ = check(T.root())
    return ok

if __name__ == "__main__":
    T = LinkedBinaryTree()

    r1 = T._add_root(44)

    rh1 = T._add_right(r1, 13)
    lt1 = T._add_left(r1, 9)

    rh2 = T._add_right(rh1, 7)
    lt3 = T._add_left(rh1, 6)

    lt2 = T._add_left(lt1, 4)
    rh3 = T._add_right(lt1, 5)

    print("É uma árvore soma?:", "sim" if is_sum_tree(T) else "não")