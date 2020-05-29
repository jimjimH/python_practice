# Fab: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(10))
# > 55

def fib(n):
    lst = []
    a, b = 0, 1
    for i in range(n):        
        lst.append(b)
        a, b = b, a+b
    print(lst)
    return lst[n-1]

print(fib(10))


