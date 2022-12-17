# https://www.acmicpc.net/problem/1244

def boy(k):
    r = k
    while r <= n:
        switch[r] = abs(switch[r] - 1)
        r += k


def girl(k):
    switch[k] = abs(switch[k] - 1)
    r = 1
    while True:
        if 0 <= k - r and k + r <= n:
            if switch[k - r] == switch[k + r]:
                switch[k - r] = abs(switch[k - r] - 1)
                switch[k + r] = abs(switch[k + r] - 1)
                r += 1
            else:
                break
        else:
            break


n = int(input())
switch = list(map(int, input().split()))
switch.insert(0, -1)

student = int(input())
for i in range(student):
    gender, num = map(int, input().split())
    if gender == 1:
        boy(num)
    else:
        girl(num)
switch.pop(0)

while switch:
    print(*switch[: 20])
    switch = switch[20:]

# print(*switch)
