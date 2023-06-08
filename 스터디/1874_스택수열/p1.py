n = int(input())
stack = []
answer = []
now = 0
inp = 0
is_possible = True

while inp < n and is_possible:
    num = int(input())
    inp += 1

    while now < num:

        now += 1
        stack.append(now)
        answer.append("+")

        if now == num:
            stack.pop()
            answer.append("-")

    if now > num:
        last = stack.pop()
        if last != num:
            print("NO")
            answer = []
            is_possible = False
        else:
            answer.append("-")

print(*answer, sep="\n")