##  Exercício: 3.
##  Implemente uma função com assinatura transfer(S, T) que transfira todos os elementos da
##  pilha S para a pilha T, de modo que o elemento que come ̧ca no topo de S seja o primeiro a
##  ser inserido em T, e o elemento na parte inferior de S termine no topo de T.

from exercicio1 import ArrayStack

def Transfer(S, T):
    while S:
        T.push(S.pop())

S, T = ArrayStack(), ArrayStack()

S.push(3)
S.push(5)
S.push(6)

Transfer(S, T)
print(S, T)