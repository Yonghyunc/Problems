# 백준 1463. 1로 만들기
# 틀린 코드...

def find(num):
    if dp[num] != 0:
        return dp[num]
    if num % 3 == 0:
        dp[num] = 1 + find(num // 3)
    elif num % 2 == 0:
        dp[num] = min(1 + find(num // 2), 1 + find(num - 1))
    else:
        dp[num] = 1 + find(num - 1)
    return dp[num]


n = int(input())

if n == 1:
    print(0)

elif n == 2 or n == 3:
    print(1)
else:
    dp = [0] * (n + 1)
    dp[2], dp[3] = 1, 1

    find(n)
    print(dp[n])


