t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0 if n % 6 else 1
    answer += 6 * sum(range((n // 6) + 1)) + (n % 6) * ((n // 6) + 1)
    print(answer)

