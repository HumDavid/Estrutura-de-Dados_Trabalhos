##  Exercício: 17.
##  Descreva um algoritmo recursivo rápido para reverter uma lista encadeada simples.

from Lists import LinkedList

def reverter(lista: LinkedList):
    if lista.is_empty():
        return LinkedList()
    
    def reverter_node(node):
        if node is None or node.next is None:
            return node
        
        nova_head = reverter_node(node.next)
        node.next.next = node
        node.next = None

        return nova_head
    
    lista_revertida = lista.copy()

    if lista_revertida.head:
        old_head = lista_revertida.head
        lista_revertida.head = reverter_node(lista_revertida.head)
        lista_revertida.tail = old_head
    
    return lista_revertida

## exemplos
lista = LinkedList()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)

print('original:', lista)
print('revertido:', reverter(lista))