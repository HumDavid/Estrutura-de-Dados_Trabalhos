##  Exercício: 5.
##  Implemente uma função que inverte uma lista de elementos colocando-os em uma pilha em
##  uma ordem e escrevendo-os de volta na lista na ordem inversa.

from trabalho1.exercicio_01 import ArrayStack

def invert_stack(stack: ArrayStack):
    temp1 = ArrayStack()
    temp2 = ArrayStack()

    while not stack.is_empty():
        temp1.push(stack.pop())

    while not temp1.is_empty():
        temp2.push(temp1.pop())

    while not temp2.is_empty():
        stack.push(temp2.pop())

s = ArrayStack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)

print('lista original:', s)
invert_stack(s)
print('lista invertida:', s)