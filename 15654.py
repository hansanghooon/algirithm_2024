import sys


n,m=map(int,sys.stdin.readline().split())


numbers=list(map(int,sys.stdin.readline().split()))
numbers.sort()

s=[]
def dfs():
    
    if len(s)==m:
        
        print(" ".join(map(str,s)))
        return
    
    for i in numbers:
        if i in s:
            continue
        
        s.append(i)
        dfs()
        s.pop()

dfs()