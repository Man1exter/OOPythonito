
# produkcja audi (KLASA) wzór na tworzenie audi
class Audi:
    pass

# dwie inne audice, kazdy ma inna (INSTANCJA) wytworzone audi 
audi_szermana = Audi()
audi_kolegi = Audi()

print(audi_szermana)
print(audi_kolegi)
print(" ")

class Golf:
    
    def skrecaj(self):
        print("Skrecam se jojo")
        # self.gdzie_jadem("WOJCICE") -> wywolywanie w sobie funckji!
        
    def gdzie_jadem(self,miasto):
        print(f'Jade se do ',miasto)
        
    def ile_paliwa(self):
        return '25 litrow na styk'
    
    def __str__(self):
        return 'MARIANOITALIANO'  # umowa z pythonem do printowania! (magiczna metoda)
    
    def __init__(self):
        print("GOLFY NA TLOKI AUUU") # po zakomentowaniu wywolywania umowa zawarty z pythonem wywola printa (warunek to nie wywolywanie!)
        # self.ile_paliwa() - równiez zadziala ( warunek to na samej gorze init!)
        
        
miszki_golf = Golf() # stworzenie instancji

#miszki_golf.skrecaj() # wywolanie pustej funckji

#miszki_golf.gdzie_jadem("KOPALINY") # przekazanie funckji przez argument

#ile_ma_litrow = miszki_golf.ile_paliwa()
#print(ile_ma_litrow)  # przekazanie do zmiennej z klasy i wywolanie

#print(miszki_golf)


# SELF ZAWSZE W ARGUMENCIE INACZEJ BĘDZIE BŁĄD!!!