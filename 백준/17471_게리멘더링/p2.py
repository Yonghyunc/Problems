'''
조합 + BFS
'''

from collections import deque
from itertools import combinations

n = int(input())
regions = list(map(int, input().split()))
region_num = range(1, n + 1)
connect = [[] for _ in range(n + 1)]
not_connected = 0
for num in range(n):
    cnt, *region = map(int, input().split())
    if not cnt:
        not_connected += 1
    else:
        connect[num + 1] = region
min_diff = 1e9


def check_connection(arr):
    visited = [arr[0]]
    checking = deque([arr[0]])
    arr_sum = 0
    while checking:
        now = checking.popleft()
        arr_sum += regions[now - 1]
        for other in connect[now]:
            if other not in visited and other in arr:
                checking.append(other)
                visited.append(other)
    if len(visited) == len(arr):
        return arr_sum
    else:
        return 0


# 지역이 단 2개 뿐일 때는, 연결이 되어 있지 않아도 상관없음
if n > 2 and not_connected >= 2:
    print(-1)
else:
    for i in range(1, n // 2 + 1):
        for case in combinations(region_num, i):
            include = list(case)
            exclude = [num for num in region_num if num not in include]
            inc, exc = check_connection(include), check_connection(exclude)
            if inc and exc:
                min_diff = min(min_diff, abs(inc - exc))
    print(min_diff)
