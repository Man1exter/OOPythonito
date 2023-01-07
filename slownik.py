def f(**kwargs):
    for k in kwargs:
        print(f'{kwargs[k]}')
        
slownik = {'a':4,'b':3}

f(**slownik)