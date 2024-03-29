def matryoshka(n):
    if n >= 1:
        print(f'Верх матрёшки вложености {n}')
        matryoshka(n - 1)
        print(f'Низ матрёшки вложеноости {n}')


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fibp(n):
    if n < 2:
        #print(n)
        return n
    a = fibp(n - 1) + fibp(n - 2)
    print(a)
    return a


def gdc(a, b):
    if a == b:
        return a
    return gdc(max(a, b) - min(a, b), min(a, b))


while True:
    try:
        matryoshka(int(input('Ведите количество матрёшек ')))
        print(fact(int(input('Ведите факториал '))))
        print(fib(int(input('Ведите номер последовательности фибоначчи '))))
        print(gdc(int(input('Ведите число для поиска НОД ')), int(input('Ведите число для поиска НОД '))))
    except Exception as s:
        print(s)
