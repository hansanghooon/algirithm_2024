import sys
input=sys.stdin.readline
L = int(input())

number_list = list(map(int, sys.stdin.readline().split()))

n = int(sys.stdin.readline())
number_list.sort() 
if n in number_list:
    print(0)
else:
    min = 0
    max = 0
    for num in number_list:            
        if num < n:     
            min = num
        elif num > n and max == 0:
            max = num
    max -= 1                   
    min += 1
    print((n-min)*(max-n+1) + (max-n))