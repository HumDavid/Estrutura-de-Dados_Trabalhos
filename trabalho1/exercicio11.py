##  Exercício: 11.
##  Crie um sistema usando uma pilha e uma fila para testar se uma determinada string  ́e um
##  palíndromo (ou seja, se os caracteressão lidos da mesma forma, tanto para a frente quanto
##  para trás).

from exercicio1 import ArrayStack, ArrayQueue
import os

def palindromo_verify(expression):
    stack = ArrayStack()
    queue = ArrayQueue()
    for c in expression:
        stack.push(c)
        queue.enqueue(c)
    while not stack.is_empty() and not queue.is_empty():
        if stack.pop() != queue.dequeue():
            return False
    return True


## exemplos
lista = ['abaa', 'aabaa', 'arara', 'bombom', '123321']
print('É PALÍNDROMO?')
for p in lista:
    print(f'{p}: {'sim' if palindromo_verify(p) else 'não'}')