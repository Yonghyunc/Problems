
n = int(input())
colors = input()

blue_cnt = 1
red_cnt = 1
before = ""
for color in colors:
    if color == "B":
        if before != "B":
            blue_cnt += 1
        before = "B"
    else:
        if before != "R":
            red_cnt += 1
        before = "R"
print(min(blue_cnt, red_cnt))