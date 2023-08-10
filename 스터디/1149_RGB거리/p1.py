import sys
input = sys.stdin.readline

red, blue, green = 0, 0, 0
n = int(input())
for _ in range(n):
    r, g, b = map(int, input().split())
    red, green, blue = r + min(blue, green), g + min(red, blue), b + min(red, green)

print(min(red, green, blue))