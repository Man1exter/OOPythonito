

class Ulamek:
    
    
    counter = 0
    
    def __init__(self,licznik,mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        
        Ulamek.counter += 1
        
        
        # self.__mianownik = mianownik -> prywatny dostep..
        # print(u.ulamek__mianownik) -> wywolanie dostepu..
        
    @staticmethod
    def metoda_statyczna(self):
        print(self)
        print("GAHAGAHAG")
        
        
    #@property
    #def licznik(self):
    #   return self.licznik
    
    
    #@licznik.setter
    #def licznik(self,value):
    #   return self.licznik + value
        
    def suma(self, k):
        return self.licznik + self.mianownik + k
        
    def __repr__(self):
        return f'{self.licznik}/{self.mianownik}'
    
    def __str__(self):
        return f'{self.licznik}/{self.mianownik}'
    
    def __hash__(self):
        return self.licznik + self.mianownik #naprzyklad do ID klienta
    
    # def __del__(self): #destruktor
      # Ulamek.counter -= 1
        


x1 = Ulamek(4,7)
print(x1)

print(x1.suma(6)) # 6 jako przekazywane k

print(hash(x1)) # zawsze int


# x1.Licznik = 22

print(Ulamek.counter)
print(Ulamek.counter)
print(Ulamek.counter)

Ulamek.metoda_statyczna(1222)