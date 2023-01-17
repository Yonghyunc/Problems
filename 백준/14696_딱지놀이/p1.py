# https://www.acmicpc.net/problem/14696

n = int(input())

for _ in range(n):
    a = input().split()
    na, la = a[0], a[1:]
    b = input().split()
    # b = list(map(int, input().split()))
    nb, lb = b[0], b[1:]
    result = 0
    for i in ['4', '3', '2', '1']:
        if la.count(i) > lb.count(i):
            result = 'A'
        elif la.count(i) < lb.count(i):
            result = 'B'
        if result:
            break
    else:
        if result == 0:
            result = 'D'

    print(result)