##  Exercício: 4.
##  Forneça um método recursivo para remover todos os elementos de uma pilha.

from exercicio1 import ArrayStack

def remove_all(stack):
    if stack.is_empty():
        return
    stack.pop()
    remove_all(stack)

s = ArrayStack()
s.push(2)
s.push(5)
s.push(6)

print('antes de remove_all():', s)
remove_all(s)
print('depois de remove_all():', s)