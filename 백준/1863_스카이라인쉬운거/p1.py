import sys
input = sys.stdin.readline

n = int(input())
skyline = [0]
building_cnt = 0
for _ in range(n):
    coord, height = map(int, input().split())
    if skyline[-1] == height:
        continue
    elif skyline[-1] < height:
        skyline.append(height)
    else:
        while skyline[-1] > height:
            skyline.pop()
            building_cnt += 1
        if skyline[-1] < height:
            skyline.append(height)
building_cnt += len(skyline) - 1
print(building_cnt)