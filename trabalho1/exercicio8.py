##  Exercício: 8.
##  Escreva um programa para verificar se em uma string contendo uma expressão aritmética, os
##  parênteses de abertura e fechamento estão bem formados ou não.

from exercicio1 import ArrayStack

def verify_parentheses(expression: str):
    pilha = ArrayStack()
    for s in expression:
        if s == '(':
            pilha.push('*')
        elif s == ')':
            if pilha.is_empty():
                return False
            pilha.pop()
    return pilha.is_empty()

## exemplos
expressions = ['(7+(2*5)/10)+2', '7+(2*5)/10)+2']
for e in expressions:
    print(e, '=> parênteses bem formados' if verify_parentheses(e) else '=> parênteses mal formados')