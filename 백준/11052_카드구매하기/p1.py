import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.insert(0, 0)
dp = [0] * (n + 1)

for num in range(1, n + 1):
    dp[num] = cards[num]
    half = num // 2 if num % 2 else num // 2 - 1
    for i in range(num, half, -1):
        dp[num] = max(dp[num], dp[i] + dp[num - i])

print(dp[-1])