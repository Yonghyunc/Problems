n = int(input())
sugar = [-1] * (n + 1)

for num in range(3, n + 1):
    if num in [3, 5]:
        sugar[num] = 1
    else:
        if sugar[num - 3] == -1 and sugar[num - 5] == -1:
            sugar[num] = -1
        else:
            if sugar[num - 3] != -1 and sugar[num - 5] != -1:
                sugar[num] = min(sugar[num - 3] + 1, sugar[num - 5] + 1)
            elif sugar[num - 3] != -1 or sugar[num - 5] != -1:
                sugar[num] = max(sugar[num - 3] + 1, sugar[num - 5] + 1)

print(sugar[-1])