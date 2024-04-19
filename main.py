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
        # print(n)
        return n
    a = fibp(n - 1) + fibp(n - 2)
    print(a)
    return a


list_fib = [0, 1]
def fib_dynamic(n):
    if n >= len(list_fib):
        for i in range(len(list_fib), n + 1):
            list_fib.append(fib_dynamic(n - 1) + fib_dynamic(n - 2))
    return list_fib[n]


def gdc(a, b):
    if a == b:
        return a
    return gdc(max(a, b) - min(a, b), min(a, b))


def gdcs1(a, b):
    return a if a == b else gdcs1(max(a, b) - min(a, b), min(a, b))


def gdcd(a, b):
    # if a == b:
    #     return a
    if max(a, b) % min(a, b) == 0:
        return min(a, b)
    return gdcd(max(a, b) % min(a, b), min(a, b))


def gdcds1(a, b):
    return min(a, b) if max(a, b) % min(a, b) == 0 else gdcds1(max(a, b) % min(a, b), min(a, b))


def pow1(a, n):
    return 1 if n == 0 else a * pow1(a, n - 1)


def pow2(a, n):
    if n == 0:
        return 1
    if n % 2 != 0:
        return a * pow2(a, n - 1)
    return pow2(a * a, n // 2)


while True:
    try:
        # matryoshka(int(input('Ведите количество матрёшек ')))
        # print(fact(int(input('Ведите факториал '))))
        # print(fibp(int(input('Ведите номер последовательности фибоначчи '))))
        # print(gdcds1(int(input('Ведите число для поиска НОД ')), int(input('Ведите число для поиска НОД '))))
        # print(gdc(int(input('Ведите число для поиска НОД ')), int(input('Ведите число для поиска НОД '))))
        # print(pow1(int(input('Ведите число основание ')), int(input('Ведите число степени '))))
        # print(pow2(int(input('Ведите число основание ')), int(input('Ведите число степени '))))
        for i in range(int(input('Введите до какого считать фибоначи '))):
            print(i, fib_dynamic(i))
    except Exception as s:
        print(s)
