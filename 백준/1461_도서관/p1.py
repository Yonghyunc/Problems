def counting(arr):
    step = 0
    for i in range(0, len(arr), m):
        step += arr[i] * 2
    return step


n, m = map(int, input().split())
books = list(map(int, input().split()))
plus, minus = [], []
for book in books:
    if book > 0:
        plus.append(book)
    else:
        minus.append(-book)
plus.sort(reverse=True)
minus.sort(reverse=True)

last = max(plus[0] if plus else 0, minus[0] if minus else 0)

answer = counting(plus) + counting(minus) - last
print(answer)