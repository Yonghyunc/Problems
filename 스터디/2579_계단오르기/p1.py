# 백준 2579. 계단 오르기

n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

dp = [0] * n

if n == 1:
    print(stairs[0])
else:
    dp[0], dp[1] = stairs[0], stairs[0] + stairs[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i-1] + stairs[i])

    print(dp[-1])















# scores = [[0, 0] for _ in range(n)]
# print(scores)
#
#
# def step(now, score, one):
#     if now < 0:
#         return
#     print(now, score, one)
#     print(score + stairs[now])
#     print(scores)
#     if score + stairs[now] >= scores[now][one]:
#         scores[now][one] = score + stairs[now]
#         if one < 1:
#             step(now - 1, scores[now][one], one + 1)
#         step(now - 2, scores[now][one], 0)
#     else:
#         return
#
#
# step(n - 2, stairs[n - 1], 0)
# print(scores[0:2])


