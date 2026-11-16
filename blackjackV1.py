import random
mazzo = [1,2,3,4,5,6,7,8,9,10,11]*4
# i valori [1,11] sono definiti come numeri diversi, da implementare il duplice valore occasionale dell'asso

def start() :
    global mano
    mano = [random.choice(mazzo),random.choice(mazzo)]
    global banco
    banco = [random.choice(mazzo),random.choice(mazzo)]
    # vengono create le 2 carte di inizio per il player e il banco
    print("la mano del player vale:", valori(mano))
    print("il banco ha:", valori(banco))

def azione():
    #@return: boole
    risposta = input("Vuoi pescare una carta (y/n)? ")
    if risposta == "y" :
        return True
    elif risposta == "n":
        return False
    
def pescare(x):
    #@param x: sequence (mano,banco); @return: sequence
    x = x + [random.choice(mazzo)]
    return x

def valori(x):
    #@param x: sequence (mano/banco); @return: int
    # vengono stabiliti i valori delle mani di player e banco
    count= 0
    for carta in x:
        count = count + carta
    return count    

def again():
    wantPlay = input("vuoi rigiocare (y/n)?")
    if wantPlay == "y" :
        bj()
    #dopo again() va messo return per terminare l'intera funzione bj() in caso di input != y
    

def bj():
    global mano, banco
    start()
    while azione() :
        mano = pescare(mano)
        print("la mano del player vale:", valori(mano))
        if valori(mano) == 21:
            print("il player ha fatto BLACKJACK")
            break
        if valori(mano) > 21:
            print("il player ha sballato, hai perso!")
            again()
            return
    # ^^parte del programma di gioco del player^^
    while valori(banco) < 17 :
        banco = pescare(banco)
        print("il banco ha:", valori(banco))
        if valori(banco) > 21 :
            print("il banco ha sballato")
            print("Il player ha vinto!")
            again()
            return
    # ^^gioco del banco^^
    if valori(mano) > valori(banco) :
        print("Complimenti, hai vinto la partita")
        again()
        return
    elif valori(mano) == valori(banco) :
        print("PAREGGIO!")
        again()
        return
    else:
        print("Purtroppo hai perso!")
        again()
        return
    # ^^controllo finale^^
       
        
bj()