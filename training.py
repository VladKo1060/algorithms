def zadanie_1(n):
    return 1 if n == 1 else 3 if n == 2 else zadanie_1(n - 1) * n + zadanie_1(n - 2) * (n - 1)


def zadanie_3(n):
    return n if n <= 2 else zadanie_3(n - 1) - zadanie_3(n - 2) + 2 * n


def zadanie_5(n):
    return n if n == 1 else n + zadanie_5(n - 2) if n % 2 != 0 else n * zadanie_5(n - 1)


def zadanie_7(n):
    if n < 3:
        return 1

    count = 0
    for i in range(1, n):
        count += zadanie_7(i)
    return count


def zadanie_9(n):
    if n >= 1000:
        return 1000
    elif n % 2 == 0:
        return n * (zadanie_9(n + 1) / 2)
    return n * zadanie_9(n + 1)

list_zadanie_10 = [0]
def zadanie_10(n):
    if n >= len(list_zadanie_10):
        for i in range(len(list_zadanie_10), n + 1):
            if n % 2 == 0:
                list_zadanie_10.append(zadanie_10(n // 10) + n % 10)
            else:
                list_zadanie_10.append(zadanie_10(n // 10))
    # print(list_zadanie_10)
    return list_zadanie_10[n]


count = 0
for k in range(100):  #10 ** 9, 2 * 10 ** 9
    a = zadanie_10(k)
    print(k, a)
    if a == 0:
        count += 1

# print(count)
