import math
import sys

input=sys.stdin.readline
n = int(input())

ans=[]
for _ in range(n):
    a, b = map(int, input().split())
    num = math.factorial(b) // (math.factorial(a) * math.factorial(b - a))
    ans.append(num)
    
for j in ans:
    print(j)