##  Exercício: 16.
##  Implemente uma função que conta o número de nós em uma lista circularmente encadeada.

from Lists import CircularList

def contar(node):
    if node is None:
        return 0
    count = 1
    current = node.next
    while current != node:
        count += 1
        current = current.next
    return count



## exemplos
c_lista = CircularList()

c_lista.append(10000)
c_lista.append(1000)
c_lista.append(100)
c_lista.append(10)
c_lista.append(1)

print(c_lista)
print('número de nós:', contar(c_lista.tail))