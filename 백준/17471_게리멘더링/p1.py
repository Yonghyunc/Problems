'''
상황을 구분하려 했는데, 모든 지역이 연결된 경우를 어떻게 해야할 지 모르겠어서 코드 포기
'''

from collections import deque

n = int(input())
regions = list(map(int, input().split()))
connect = [[] for _ in range(n + 1)]
not_connected = 0
not_connected_list = []
for num in range(n):
    cnt, *region = map(int, input().split())
    if not cnt:
        not_connected += 1
        not_connected_list.append(num)
    else:
        connect[num + 1] = region
print(regions, connect)

if not_connected >= 2:
    print(-1)
# elif not_connected == 1:
#     visited = [0] * n
#
#     # 여기서도 구역이 3개 이상으로 쪼개지는지 확인해야 함
#     print(sum(regions) - 2 * regions[not_connected_list[0]])
else:
    # 1번 노드를 기준으로 나눠봤음
    visited = [0] * (n + 1)
    numbers = deque([1])
    visited[1] += 1
    include = []            # 1번 노드를 포함하는 리스트
    include_val = 0
    while numbers:
        now = numbers.popleft()
        include.append(now)
        include_val += regions[now - 1]
        for other in connect[now]:
            if not visited[other]:
                visited[other] += 1
                numbers.append(other)
    print(include)

    if len(include) == n:
        print('ㅋㅋㅋㅋㅋㅋㅋ 다 연결됨')

    else:
        exclude = [node for node in range(1, n + 1) if node not in include]
        print(exclude)
        print("1번 노드 포함 안 하는 모임이 연결되는지 확인")
        numbers = deque([exclude[0]])
        visited[exclude[0]] += 1
        exclude_val = 0
        while numbers:
            now = numbers.popleft()
            exclude_val += regions[now - 1]
            for other in connect[now]:
                if not visited[other]:
                    visited[other] += 1
                    numbers.append(other)
        if 0 in visited[1:]:
            print(-1)
        else:
            print('여기임?')
            print(abs(include_val - exclude_val))