def faktorial(n):
    faktorialBilangan = 1
    while(n > 0):
        faktorialBilangan = faktorialBilangan * n
        n -= 1
    return faktorialBilangan

def kombinasi(a,b):
    c = a - b

    hasil = faktorial(a) / (faktorial(b) * (faktorial(c)))
    print(hasil)

def permutasi(a,b):
    c = a - b

    hasil = faktorial(a) / faktorial(c)
    print(hasil)

#kombinasi

a = 5
b = 3
kombinasi(a,b)

#permutasi

x = 10
y = 7
permutasi(x,y)
