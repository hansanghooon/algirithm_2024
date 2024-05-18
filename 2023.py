import math
import sys
sys.setrecursionlimit(100000)
n =input()




def prime_check(n):
    
    if n<4:
        return True


    for i in range(2, 1+math.ceil(math.sqrt(n))):
        if n%i ==0:
            return False
    return True
          



def dfs(num):
    if len(str(num))==n:
        print(num)
    else:
        for i in [1,3,5,7,9]:

            if prime_check(10*num+i):
                dfs(10*num+i)


start=[2,3,5,7]


for i in start:
    dfs(i)