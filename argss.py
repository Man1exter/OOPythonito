

def fun5(*args):  #args + zestaw argumentow => zamiana na tuple
    print(args)
    
print(fun5(1,2,3))


def mm1(*args):
    for a in args:
        print(a)
        
mm1(1,2,'abc')