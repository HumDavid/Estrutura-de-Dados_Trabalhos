##  Exercício: 9.
##  Escreva um programa para converter uma expressão aritmética na forma prefixada para
##  formas infixas e pós-fixadas equivalentes.

from exercicio1 import ArrayStack
import os

def prefixa_to_infixa(expression):
    pilha = ArrayStack()
    operators = '+-/*'

    for c in reversed(expression):
        if c not in operators:
            pilha.push(c)
        else:
            a = pilha.pop()
            b = pilha.pop()
            pilha.push(f'({a}{c}{b})')
    return pilha.pop()

def prefixa_to_posfixa(expression):
    pilha = ArrayStack()
    operators = '+-/*'

    for c in reversed(expression):
        if c not in operators:
            pilha.push(c)
        else:
            a = pilha.pop()
            b = pilha.pop()
            pilha.push(f"{a}{b}{c}")
    return pilha.pop()


## exemplos
expressions = ['*+234', '-*+ABC*-DE+FG']
for i in range(len(expressions)):
    print(f'========================== exemplo {i+1} ==========================')
    print('préfixa:', expressions[i])
    print('pósfixa:', prefixa_to_posfixa(expressions[i]))
    print('infixa:', prefixa_to_infixa(expressions[i]))