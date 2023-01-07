class Osoba:
    def __init__(self,pesel,imie,nazwisko,rok_urodzenia,wzrost =0.0,waga=0.0):
        self.__pesel = pesel
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__wzrost = wzrost
        self.__waga = waga
        self.__rok_urodzenia = rok_urodzenia
        
    def __hash__(self): #np pod ID - unikatowy
        return self.__pesel
    
    def __str__(self):
        s = f'{self.__pesel} {self.__imie} {self.__nazwisko}'
        return s
    
    def __repr__(self): #reprezentacja
        s = f'{self.__pesel} {self.__imie} {self.__nazwisko}'
        return s
    
    @property
    def imie(self):
        return self.__imie
    
    @property
    def nazwisko(self):
        return self.__nazwisko
    
    @imie.setter
    def imie(self,imie):
        self.__imie = imie
        
    @nazwisko.setter
    def nazwisko(self,nazwisko):
        self.__nazwisko = nazwisko
        

b = Osoba(5907594646,'Jan','Kowal',2022,3556,6666)

print(b)
print(b.__repr__())

b.imie = 'Mariusz'
print(b)