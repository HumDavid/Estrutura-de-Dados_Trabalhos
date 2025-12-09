##  Exercício: 14.
##  Descreva um bom algoritmo para concatenar duas listas encadeadas simples L e M, dadas
##  apenas referências ao primeiro nó de cada lista, em uma única lista L que contém todos os
##  nós de L seguidos por todos os nós de M.

from Lists import LinkedList

def concatenar(head_L, head_M):
    if head_L is None:
        return head_M
    
    if head_M is None:
        return head_L
    
    atual = head_L
    while atual.next is not None:
        atual = atual.next
    
    atual.next = head_M
    
    return head_L


## exemplos
lista1 = LinkedList()
lista2 = LinkedList()

lista1.append(1)
lista1.append(2)
lista2.append(3)
lista2.append(4)

print('lista 1:', lista1)
print('lista 2:', lista2)

concatenar(lista1.head, lista2.head)

print('concatenação:', lista1)