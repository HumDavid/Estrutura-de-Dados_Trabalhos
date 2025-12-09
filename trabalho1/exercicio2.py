##  Exercício: 2.
##  Execute a seguinte s ́erie de opera ̧c ̃oes de pilha, assumindo uma pilha inicialmente vazia:
##      push(5), push(3), pop(), push(2), push(8), pop(), pop(), push(9), push(1), pop(), push(7),
##      push(6), pop(), pop(), push(4), pop(), pop().

from exercicio1 import ArrayStack

pilha = ArrayStack()


pilha.push(5)
pilha.push(3)
pilha.pop()
pilha.push(2)
pilha.push(8)
pilha.pop()
pilha.pop()
pilha.push(9)
pilha.push(1)
pilha.pop()
pilha.push(7)
pilha.push(6)
pilha.pop()
pilha.pop()
pilha.push(4)
pilha.pop() #
pilha.pop()

print(pilha)