##  Exercício: 15.
##  Descreva um algoritmo recursivo que conta o número de nós em uma lista encadeada simples.

from Lists import LinkedList

def contador(node):
    if node is None:
        return 0
    
    return 1 + contador(node.next)



## exemplos
lista = LinkedList()

lista.append(10)
lista.append(100)
lista.append(1000)
lista.append(10000)
lista.append(100000)

print('número de nós:', contador(lista.head))