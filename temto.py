

def fun_new(ar1,ar2,ar3,ar4,ar5=5):
    print(ar5)
    print(ar4)
    return

fun_new(1,2,3,4,5666)

# fun_new(ar5=5555,ar1=4444) -> kolejnosc losowa..add()

#def nu(a1,b2,c3,d4,e5):
    #print(a1)
    #print(b2)
    #print(c3)
    #print(d4)
    #print(e5)
    #return

#nu(e5=555,a1=222)

def mm(a1,a2,a3,a4,dzialanie='dodaj'):
    result = 0
    if dzialanie:
     if dzialanie == 'dodaj':
        result = a1 + a2 + a3 + a4
     elif dzialanie == 'pomnoz':
        result = a1 * a2 * a3 * a4
     else:
        raise ValueError('blad arg nr 5')
        
        
    return result

print(mm(1,2,3,4))