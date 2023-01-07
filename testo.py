def fun1(wiek,dane):
    wiek += 2
    dane.append('napis')
    
w = 20
d = ['imie','nawisko']

z = fun1(w,d)

print(w)
print(d)
print(z)

print(f'id_w= {id(w)}') # wskaznik + przypisanie 




def fun(wiek):
    
    print(" ")
    return wiek + 2

wt = 4

wt = fun(wt)
print(wt)
