# lambda - funkcja jednolinijkowa

fun = lambda a:a+1
print(fun(4))

# from ttictoc import tic,toc -> szybkosc wykonywania 1e4 = 10000,0 -> 1 do 4 notacja wykladnicza

fun = lambda a:a+1

def fun2(a):
    return a+1

N_ITER = int(1e4)

tic()
for i in range(N_ITER):
    fun(i)
print(toc())