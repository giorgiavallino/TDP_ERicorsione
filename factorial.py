# Creazione di un metodo che calcola il fattoriale di un numero (file Ricorsione, slide 12-13)

def factorialRicorsivo(n):
    if n <= 1:
        return 1
    else:
        return n * factorialRicorsivo(n-1)

if __name__ == "__main__":
    print(factorialRicorsivo(4))