t = int(input())
dp = [0, 1, 2, 4]

for _ in range(t):
    n = int(input())
    dp_len = len(dp)
    if n >= dp_len:
        for i in range(dp_len, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    print(dp[n])