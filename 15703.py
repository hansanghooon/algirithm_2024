import sys
from collections import deque


def top(dq):

    result=0
    #현재 몇개가 쌓여있나
    top=0
    while len(dq):
        
        #현재 dice 숫자 
        cur_dice=dq.popleft()
        # print(len(dq))
        if cur_dice<top:
            result=result+1
            top=0

        else:
            top=top+1
            if len(dq)==0:
                result=result+1   




    return result





if __name__ == "__main__":
    N = int(input())
    numbers = sys.stdin.readline().strip()
    numbers=list(map(int, numbers.split()))
    numbers.sort()
    dq=deque(numbers)
    res=top(dq)
    print(res)