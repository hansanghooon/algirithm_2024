import sys
import math

#이진수 1 개수 새기
def count_ones(n):
    if n<=0:
        return 0
    count = 0
    while n:
        if n%2 ==1:
            count=count+1
        
        n=n//2
    


    return count


# 각 1의 개수 새기
def count_one_check(num):
    binary_count=0
    
    for i in range(N):
        
        binary_count = binary_count+ count_ones(num[i])

    return binary_count


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().strip().split())) 
    result = count_one_check(numbers)
    # 2 곱하는 횟수, 최대값의 log 값 
    if max(numbers) !=0:
        
        result = int(result )+ int( math.floor(math.log2(max(numbers))) )
    print(result)


