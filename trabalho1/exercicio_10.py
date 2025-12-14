##  Exercício: 10.
##  Implemente uma calculadora aritmética de inteiros usando pilhas.

from trabalho1.exercicio_01 import ArrayStack

def operators():
    return {
        '+': (1, lambda a, b: a + b),
        '-': (1, lambda a, b: a - b),
        '*': (2, lambda a, b: a * b),
        '/': (2, lambda a, b: a // b if b != 0 else None),
        '^': (3, lambda a, b: a ** b)
    }
    
def is_operator(token):
    return token in operators()
    
def get_precedence(operator):
    return operators()[operator][0] if operator in operators() else 0
    
def apply_operator(operator, a, b):
    if operator in operators():
        return operators()[operator][1](a, b)
    return None
    
def infix_to_postfix(expression):
    output = []
    stack = ArrayStack()
    
    import re
    expression = re.sub(r'([+-/*^()])', r' \1 ', expression)
        
    for token in expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            output.append(int(token))
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.top() != '(':
                output.append(stack.pop())
            stack.pop()
        elif is_operator(token):
            while (not stack.is_empty() and stack.top() != '(' and 
                   get_precedence(stack.top()) >= get_precedence(token)):
                output.append(stack.pop())
            stack.push(token)
        
    while not stack.is_empty():
        output.append(stack.pop())
        
    return output
    
def evaluate_postfix(postfix):
    stack = ArrayStack()
        
    for token in postfix:
        if isinstance(token, int):
            stack.push(token)
        elif is_operator(token):
            if stack.__len__() < 2:
                return "Erro: Expressão inválida  aaaa"
                
            b = stack.pop()
            a = stack.pop()
            result = apply_operator(token, a, b)
                
            if result is None:
                return "Erro: Divisão por zero"
                
            stack.push(result)
        
    if stack.__len__() != 1:
        return "Erro: Expressão inválida bbbbbbb"
        
    return stack.pop()
    
def calculator(expression):
    try:
        postfix = infix_to_postfix(expression)
        return evaluate_postfix(postfix)
    except Exception:
        return f"Erro: Expressão inválida: {postfix}"


## exemplos
expressions = ['(70/10)*3+9-15', '5+4-3*2/1']
for e in expressions:
    print(f'{e} = {calculator(e)}')