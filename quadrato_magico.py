# Creazione di un metodo ricorsivo che crea un quadrato magico con i rispettivi valori al suo interno

def quadrato_magico(N):
    rimanenti = list(range(1,N*N+1))
    ricorsione([], rimanenti, N)

def ricorsione(soluzione_parziale, rimanenti, N):
    # Condizione terminale --> se la griglia è costituita da N*N elementi, allora la griglia è stata completata (al
    # posto di visualizzare una griglia, nel caso proposto essa sarà rappresentata da una lista)
    if len(soluzione_parziale) == N*N:
        print(soluzione_parziale)
    # Caso non terminale / ricorsivo
    else:
        for i in range(len(rimanenti)):
            numero = rimanenti[i]
            soluzione_parziale.append(numero)
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione(soluzione_parziale, nuovi_rimanenti, N)
            soluzione_parziale.pop()

if __name__ == '__main__':
    quadrato_magico(3)