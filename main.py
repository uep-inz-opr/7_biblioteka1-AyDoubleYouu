import ast as ast

class Biblioteka():
    
    def __init__(self,tytul,autor,rok): 
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.ewidencja = 1
        self.ksiazka = self.tytul,self.autor
        
    def __repr__(self):
        return "'"+self.autor +""+ "'," + str(self.ewidencja)
    

ksiazka_dane = {}
ilosc_ksiazek = int(input())
for ilosc in range(ilosc_ksiazek):
    ksiazka_wejsciowa = eval(input())
    tytul = ksiazka_wejsciowa[0].strip()
    autor = ksiazka_wejsciowa[1].strip()
    rok = ksiazka_wejsciowa[2]
    if tytul in ksiazka_dane:
        ksiazka_dane[tytul].ewidencja +=1
    else:
        ksiazka_dane[tytul] = Biblioteka(tytul,autor,rok)

posortowane_ksiazki_dane = sorted(ksiazka_dane.items())

for ksiazka in posortowane_ksiazki_dane:
    print(ksiazka)
