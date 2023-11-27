'''
이 경우 메모리초과
'''

from collections import deque

s = input()
t = input()

answer = 0
words = deque([s])
while words:
    word = words.popleft()
    print(word)
    if word == t:
        answer = 1
        break
    if len(word) < len(t):
        a = word[::] + "A"
        b = word[::-1] + "B"
        words.append(a)
        if a != b:
            words.append(b)
print(answer)