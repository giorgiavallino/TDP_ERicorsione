# Creazione di un countdown (file Ricorsione, slide 11)

from time import sleep

def countdownNonRicorsivo(n):
    while (n>=0):
        print(n)
        sleep(0.5)
        n = n - 1

def countdownRicorsivo(n):
    if n <= 0:
        print("Stop")
    else:
        print(n)
        sleep(0.5)
        n = n - 1
        countdownRicorsivo(n)

if __name__ == "__main__":
    countdownNonRicorsivo(10)
    countdownRicorsivo(10)