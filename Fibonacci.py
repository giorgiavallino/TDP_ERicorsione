# Creazione di un metodo che calcoli la funzione di Fibonacci di un numero n (file Ricorsione, slide 38-39-40)

from time import time
from functools import lru_cache

class  Fibonacci:

    def __init__(self):
        self.cache = {0: 0, 1: 1}

    def calcolaFibonacciRicorsivo(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.calcolaFibonacciRicorsivo(n-1) + self.calcolaFibonacciRicorsivo(n-2)

    def calcolaFibonacciRicorsivoWithMemoization(self, n):
        if self.cache.get(n) is not None:
            return self.cache[n]
        else:
            self.cache[n] = (self.calcolaFibonacciRicorsivoWithMemoization(n-1) +
                             self.calcolaFibonacciRicorsivoWithMemoization(n-2))
            return self.cache[n]

    @lru_cache(maxsize=None)
    def calcolaFibonacciRicorsivoWithMemoizationLRU(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return (self.calcolaFibonacciRicorsivoWithMemoizationLRU(n-1) +
                    self.calcolaFibonacciRicorsivoWithMemoizationLRU(n-2))

if __name__ == '__main__':

    fib = Fibonacci()

    start_time_01 = time()
    print(fib.calcolaFibonacciRicorsivo(40))
    end_time_01 = time()
    print(f"Elapsed time: {end_time_01-start_time_01}")

    start_time_02 = time()
    print(fib.calcolaFibonacciRicorsivoWithMemoization(40))
    end_time_02 = time()
    print(f"Elapsed time: {end_time_02 - start_time_02}")

    start_time_03 = time()
    print(fib.calcolaFibonacciRicorsivoWithMemoizationLRU(40))
    end_time_03 = time()
    print(f"Elapsed time: {end_time_03 - start_time_03}")