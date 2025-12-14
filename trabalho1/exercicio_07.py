##  Exercício: 7.
##  Execute a seguinte série de operações de deque, assumindo uma deque inicialmente vazia:
##      add first(4), add last(8), add last(9), add first(5), back(), delete first( ), delete last( )
##      add last(7), first( ), last( ), add last(6), delete first( ), delete first( ).

from trabalho1.exercicio_01 import ArrayDeque


deque = ArrayDeque()

deque.add_first(4)
deque.add_last(8)
deque.add_last(9)
deque.add_first(5)
print(deque.last())
deque.delete_first()
deque.delete_last()
deque.add_last(7)
print(deque.first())
print(deque.last())
deque.add_last(6)
deque.delete_first()
deque.delete_first()

print(deque)