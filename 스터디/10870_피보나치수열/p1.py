# 백준 10870. 피보나치수열


def fibonacci(n):
   if n == 0:
       return 0
   if n == 1:
       return 1
   else:
       return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(int(input())))