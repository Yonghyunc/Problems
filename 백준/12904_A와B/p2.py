s = input()
t = input()
while len(t) > len(s):
    if t[-1] == "B":
        t = t[-2::-1]
    else:
        t = t[:-1]
print(1 if s == t else 0)