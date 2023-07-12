import sys
input = sys.stdin.readline
from collections import deque

n, w, l = map(int, input().split())
truck = deque(list(map(int, input().split())))
bridge = deque([0] * w)

time = 0
weight = 0
while truck:
    weight -= bridge.popleft()
    if weight + truck[0] <= l:
        next_truck = truck.popleft()
        bridge.append(next_truck)
        weight += next_truck
    else:
        bridge.append(0)
    time += 1

if weight:
    time += w

print(time)