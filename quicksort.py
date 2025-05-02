# Creazione di un metodo Quicksort che ordini una lista di numeri (file Ricorsione, slide 45-46-47-48)

def quicksortRicorsivo(sequenza):
    if len(sequenza) <= 1:
        return sequenza
    else:
        # 1. determinare un pivot
        pivot = sequenza[0] # scelto casualmente dato che non si hanno informazioni sui dati
        # 2. dividere la sequenza in sotto-sequenze
        sequenza_smaller = []
        sequenza_larger = []
        sequenza_pivot = []
        for i in sequenza:
            if i < pivot:
                sequenza_smaller.append(i)
            elif i > pivot:
                sequenza_larger.append(i)
            else:
                sequenza_pivot.append(i)
        return quicksortRicorsivo(sequenza_smaller) + sequenza_pivot + quicksortRicorsivo(sequenza_larger)

if __name__ == '__main__':
    sequenza = [3, 5, 2, 9, 11, 4, 7]
    print(quicksortRicorsivo(sequenza))