##  Exercício: 19.
##  Escreva um programa para excluir elementos duplicados em uma lista duplamente encadeada.

from Lists import DoublyLinkedList

def sem_duplicadas(lista):
    if lista.is_empty() or lista.size == 1:
        return 0
    
    valores_vistos = []
    atual = lista.head
    removidos = 0
    
    while atual is not None:
        proximo = atual.next
        
        if atual.data in valores_vistos:
            if atual == lista.head:
                lista.remove_first()
                removidos += 1
            elif atual == lista.tail:
                lista.remove_last()
                removidos += 1
            else:
                atual.prev.next = atual.next
                atual.next.prev = atual.prev
                lista.size -= 1
                removidos += 1
        else:
            valores_vistos.append(atual.data)
        
        atual = proximo
    
    return removidos


## exemplos
lista = DoublyLinkedList()

lista.append(1)
lista.append(1)
lista.append(2)
lista.append(2)
lista.append(3)
lista.append(3)

print('original:', lista)
print('quantos removidos:', sem_duplicadas(lista))
print('sem duplicados:', lista)