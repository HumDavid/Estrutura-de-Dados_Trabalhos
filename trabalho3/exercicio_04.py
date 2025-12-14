## Exercício: 4
## Insira, em uma árvore de busca binária vazia, entradas com as chaves 30, 40, 24, 58, 48, 26, 11, 13 (nesta ordem).
## Imprima a árvore após cada inserção.

from exercicio_01 import TreeMap

def print_tree(t):
    def _print(p, prefix="", is_left=True):
        if p is None:
            return

        connector = "└── " if is_left else "┌── "
        print(prefix + connector + str(p.key()))

        if is_left:
            new_prefix = prefix + "    "
        else:
            new_prefix = prefix + "│   "

        if t.right(p) is not None:
            _print(t.right(p), new_prefix, False)
        else:
            print(new_prefix + "┌── None")

        if t.left(p) is not None:
            _print(t.left(p), new_prefix, True)
        else:
            print(new_prefix + "└── None")

    if t.is_empty():
        print("<árvore vazia>")
    else:
        print("Árvore:")
        _print(t.root())
    print("-" * 50)

if __name__ == "__main__":
    tm = TreeMap()

    entradas = [30, 40, 24, 58, 48, 26, 11, 13]
    for k in entradas:
        tm[k] = str(k)
        print(f"Após inserir {k}:")
        print_tree(tm)