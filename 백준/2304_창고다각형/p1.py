# https://www.acmicpc.net/problem/2304


n = int(input())
pillar = []

for _ in range(n):
    l, h = map(int, input().split())
    pillar.append([l, h])

pillar.sort()

max_pillar = max(pillar, key=lambda x: x[1])
max_idx = pillar.index(max_pillar)

result = max_pillar[1]
left = pillar[:max_idx + 1]
right = pillar[max_idx:]

bl, bh = left[0][0], left[0][1]
for nl, nh in left:
    if nh > bh:
        result += bh * (nl - bl)
        bl, bh = nl, nh


bl, bh = right[-1][0], right[-1][1]
for nl, nh in right[::-1]:
    if nh >= bh:
        result += bh * (bl - nl)
        bl, bh = nl, nh

print(result)


