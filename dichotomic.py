# Creazione di un metodo che implementa la ricerca dicotomica di un numero in una lista ordinata
# (file Ricorsione, slide 49-50-51-52-53-54)

def ricercaDicotomicaRicorsivo(lista, valore):
    if len(lista) <= 1:
        if lista[0] == valore:
            return True
        else:
            return False
    else:
        index = len(lista)//2
        return (ricercaDicotomicaRicorsivo(lista[:index], valore) or
                ricercaDicotomicaRicorsivo(lista[index:], valore))

if __name__ == '__main__':
    sequenza = [1,2,3,4,5,6,7,8,9,10] # deve essere ordinata!
    print(ricercaDicotomicaRicorsivo(sequenza, 2))
    print(ricercaDicotomicaRicorsivo(sequenza, 11))

# Il metodo sopra implementato non è molto efficiente: è possibile apportare dei miglioramenti al codice scritto --> ad
# esempio, si potrebbe evitare di andare a controllare entrambe le sottoliste nel costrutto "else" ma se ne potrebbe
# controllare solo una delle due imponendo un ciclo if ed else nel quale viene verificata la prima sottolista se
# il valore è inferiore al pivot e la seconda nel caso contrario