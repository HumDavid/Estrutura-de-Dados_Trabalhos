## Exercício: 4.
## Escreva um algoritmo eficiente para verificar se duas árvores binárias são idênticas ou não.
## Duas árvores binárias são idênticas se tiverem a mesma estrutura e o mesmo conteúdo.

from exercicio_03 import LinkedBinaryTree

def are_identical(t1, t2):

    def identical(p1, p2):
        if p1 is None or p2 is None:
            return p1 is p2

        return (
            p1.element() == p2.element() and
            identical(t1.left(p1),  t2.left(p2)) and
            identical(t1.right(p1), t2.right(p2))
        )

    if t1.is_empty() or t2.is_empty():
        return t1.is_empty() and t2.is_empty()

    return identical(t1.root(), t2.root())

if __name__ == "__main__":
    T1 = LinkedBinaryTree()
    r1 = T1._add_root(5)
    rl1 = T1._add_left(r1, 4)
    rr1 = T1._add_right(r1, 6)
    
    T2 = LinkedBinaryTree()
    r2 = T2._add_root(5)
    rl2 = T2._add_left(r2, 4)
    rr2 = T2._add_right(r2, 6)
    
    T3 = LinkedBinaryTree()
    r3 = T3._add_root(5)
    rl3 = T3._add_left(r3, 4)
    rr3 = T3._add_right(r3, 7)
    
    print(f"T1 == T2?: {are_identical(T1, T2)}")
    print(f"T1 == T3?: {are_identical(T1, T3)}")