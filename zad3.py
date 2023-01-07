def fun(*args):
    
    x = 0
    
    for i in args:
        if isinstance(i,int):
            x += i
            
    return x

print(fun(5,'a',3,2,'g'))