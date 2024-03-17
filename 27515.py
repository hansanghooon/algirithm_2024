import sys
import math
def calculate_sequence(N):
    res = 0
    for _ in range(N):
        op = sys.stdin.readline().strip()
        sign = op[0]  # 덧셈뺄셈
        number = int(op[1:])  # 숫자 
        if sign == '+':
            res += number
        elif sign == '-':
            res -= number
        if res<1:
            print(0)
        else:
            lognum=math.floor(math.log2(res))
            print(2**lognum)
        
    return res

N = int(sys.stdin.readline().strip())
result = calculate_sequence(N)