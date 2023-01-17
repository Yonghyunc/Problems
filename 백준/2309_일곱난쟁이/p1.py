# acmicpc.net/problem/2309

dwarf = []
for _ in range(9):
    height = int(input())
    dwarf.append(height)

two = sum(dwarf) - 100

can = 0
breaker = False
for i in range(8):
    if not breaker:
        d1 = dwarf[i]
        can += d1
        for j in range(i + 1, 9):
            d2 = dwarf[j]
            can += d2
            if can == two:
                dwarf.remove(d1)
                dwarf.remove(d2)
                breaker = True
                break
            else:
                can -= d2
        else:
            can -= d1
    else:
        break
dwarf.sort()
print(*dwarf, sep='\n')
