import math

def log(x,n = 10,k = 2):
    df = math.log(x**2 + 5,n) * (k + 1) * x
    return df

print(log(6))
    

    