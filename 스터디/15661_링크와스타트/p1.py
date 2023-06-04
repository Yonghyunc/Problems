# 시간 초과


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
member = list(range(0, n))

last_a = []
min_diff = 1e9


def split_team(n, k, s):
    global last_a, min_diff
    if k == 0:
        team_a = team[:]
        team_b = another_team(team_a)
        # if last_a == team_b:
        #     return
        # if len(team_a) == len(team_b):
        #     last_a = team_a[::-1]

        power_a = get_power(team_a)
        power_b = get_power(team_b)
        diff = abs(power_a - power_b)

        min_diff = min(min_diff, diff)
        return
    else:
        for i in range(s, n - k + 1):
            team[k - 1] = member[i]
            # print(team)
            split_team(n, k - 1, i + 1)


def another_team(team_a):
    team_b = member[:]
    for i in team:
        team_b.pop(i)
    return team_b


def get_power(team):
    power = 0
    for i in range(len(team)):
        for j in range(i + 1,  len(team)):
            power += (arr[team[i]][team[j]] + arr[team[j]][team[i]])
    return power


for num in range(1, n // 2 + 1):
    team = [0] * num
    split_team(n, num, 0)

print(min_diff)

