# 시간초과

t = int(input())


def zero(n):
    return 1 if n == 0 else 0 if n == 1 else zero(n - 1) + zero(n - 2)


def one(n):
    return 0 if n == 0 else 1 if n == 1 else one(n - 1) + one(n - 2)


for _ in range(t):
    n = int(input())
    print(zero(n), one(n))
