# Creazione di un metodo che data una lista calcoli quante stringhe essa contiene (file Ricorsione, slide 31-32-33-34-35)

def countLeafNodesRicorsivo(lista):
    if len(lista) == 0:
        return 0
    else:
        counter = 0
        for elemento in lista:
            if type(elemento) == list:
                counter = counter + countLeafNodesRicorsivo(elemento)
            else:
                counter = counter + 1
        return counter

if  __name__ == '__main__':
    names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(countLeafNodesRicorsivo(names))