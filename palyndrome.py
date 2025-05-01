# Creazione di un metodo che verifica se una parola è palindroma (file Ricorsivo, slide 17)

def palindromaRicorsivo(parola):
    if len(parola) <= 1:
        return True
    else:
        return parola[0] == parola[-1] and palindromaRicorsivo(parola[1:-1]) # viene verificato che la prima e l'ultima
        # lettera siano uguali e viene richiamato il medesimo metodo ricorsivo per controllare le restanti lettere
        # della parola

def palindromaNonRicorsiva(parola):
    return parola == parola[::-1]

if __name__=="__main__":
    print(palindromaRicorsivo("casa"))
    print(palindromaRicorsivo("civic"))
    print(palindromaNonRicorsiva("casa"))
    print(palindromaNonRicorsiva("civic"))