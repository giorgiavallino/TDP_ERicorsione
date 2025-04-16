
def quadrato_magico(N):
    rimanenti = list(range(1,N*N+1))
    ricorsione([], rimanenti, N)

def ricorsione(parziale, rimanenti, N):
    #condizione terminale
    if len(parziale) == N*N:
        print(parziale)
    #caso non terminale
    else:
        for i in range(len(rimanenti)):
            numero = rimanenti[i]
            parziale.append(numero)
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione(parziale, nuovi_rimanenti, N)
            parziale.pop()


if __name__ == '__main__':
    quadrato_magico(3)