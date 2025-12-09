##  Exercício: 13.
##  Forneça um algoritmo para encontrar o penúltimo nó em uma lista encadeada simples na
##  qual o último nó é indicado por uma próxima referência de None.

from Lists import LinkedList

def penultimate(head):
    if head is None or head.next is None:
        return None
    
    current = head
    while current.next.next is not None:
        current = current.next
    
    return current

## exemplos

lista = LinkedList()
lista.append(1)
lista.append(2)
lista.append(3)
print(lista)
print('penúltimo:', penultimate(lista.head))
lista.remove_last()
print(lista)
print('penúltimo:', penultimate(lista.head))