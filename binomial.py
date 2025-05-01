# Creazione di una funzione che calcoli il binomiale di due numeri n e m (file Ricorsione, slide 14)

def binomialRicorsivo(n, m):
    if m == n or m == 0:
        return 1
    else:
        return binomialRicorsivo(n-1, m-1) + binomialRicorsivo(n-1, m)

if __name__=="__main__":
    print(binomialRicorsivo(5, 3))
    # per controllare che il risultato del binomiale sia corretto, si può usare la libreria scientifica scipy -->
    # --> scipy.special.binom(5, 3)