def z1(n: int, x: int) -> int:
    if n == x:
        return 1
    if n > x:
        return 0
    return z1(n + 1, x) + z1(n * 2, x) + z1(n + 3, x)


def z2(n: int, x: int) -> int:
    if n == x:
        return 1
    if n > x:
        return 0
    return z2(n + 1, x) + z2(n + 2, x) + z2(n * 3, x)


def z3(n: int, x: int) -> int:
    if n == x:
        return 1
    if n > x:
        return 0
    return z3(n + 2, x) + z3(n + 4, x)


def z4(n: int, x: int, i: bool = 0) -> int:
    if n == x:
        return 1
    if n > x + 1:
        return 0
    if i == 0:
        return z4(n - 1, x, 1) + z4(n + 3, x) + z4(n * 2, x)
    return z4(n + 3, x) + z4(n * 2, x)


def z5(n: int, x: int) -> int:
    if n == x:
        return 1
    if n > x:
        return 0
    return z5(n + 1, x) + z5(n * 4, x)


def z6(n: int, x: int) -> int:
    if n == x:
        return 1
    if n > x:
        return 0
    return z6(n + 1, x) + z6(n * 2, x)


def z7(n: int, x: int) -> int:
    if n == x:
        return 1
    if n > x:
        return 0
    return z7(n + 1, x) + z7(n + 2, x) + z7(n * 3, x)


def z8(n: int, x: int) -> int:
    if n > x or n == 6 or n == 12:
        return 0
    if n == x:
        return 1
    return z8(n + 1, x) + z8(n * 2, x) + z8(n + 3, x)


def z9(n: int, x: int) -> int:
    if n == x:
        return 1
    if n > x:
        return 0
    return z9(n + 1, x) + z9(n * 2, x) + z9(n * 3, x)


def z10(n: int, x: int) -> int:
    if n > x or n == 59:
        return 0
    if n == x:
        return 1
    return z10(n + 1, x) + z10(n * 2, x)


print('Задание 1', z1(3, 12) * z1(12, 16))
print('Задание 2', z2(3, 10) * z2(10, 25) - z2(3, 10) * z2(10, 17) * z2(17, 25))
print('Задание 3', z3(4, 22))
print('Задание 4', z4(4, 14))
print('Задание 5', z5(1, 29))
print('Задание 6', z6(2, 11) * z6(11, 25) * z6(25, 50))
print('Задание 7', z7(1, 10) * z7(10, 15))
print('Задание 8', z8(3, 16))
print('Задание 9', z9(1, 13))
print('Задание 10', z10(3, 14) * z10(14, 62))
