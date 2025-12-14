##  Exercício: 18.
##  Uma lista encadeada contém alguns números positivos e alguns números negativos. Usando
##  essa lista encadeada, escreva um programa para criar duas novas listas encadeadas, uma
##  contendo todos os números positivos e a outra contendo todos os números negativos.

from Lists import LinkedList

def separar(lista_original):
    lista_positivos = LinkedList()
    lista_negativos = LinkedList()
    
    if lista_original.is_empty():
        return lista_positivos, lista_negativos
    
    atual = lista_original.head
    
    while atual is not None:
        valor = atual.data
        
        if isinstance(valor, (int, float)):
            if valor >= 0:
                lista_positivos.append(valor)
            else:
                lista_negativos.append(valor)
        else:
            print(f"Aviso: Valor '{valor}' não é numérico e será ignorado.")
        
        atual = atual.next
    
    return lista_positivos, lista_negativos


## exemplos
lista = LinkedList()

lista.append(1)
lista.append(-1)
lista.append(2)
lista.append(-2)
lista.append(3)
lista.append(-3)

positivo, negativo = separar(lista)
print('original:', lista)
print('positivos:', positivo)
print('negativos:', negativo)