import sys
import heapq

def find_middle_number(numbers):
    max_heap = []  # 최대 힙
    min_heap = []  # 최소 힙

    #결괒 저장했다가 한꺼번에 프린트
    
    #heappop 자체가 가장 작은 원소를 return 하기 때문에, 최대값들의 최소값과, 최소값들의 최대값을 구해서 중앙값을 구함
    # max heap -> pop 시 heap 의 최대값들이 나옴, min-> 거꾸로 
    # max 의 경우 작은값들의 최대를 구하기 위해서 값에 - 를 곱해서 저장, 즉 pop 을 할경우 최대값이 나옴 
    result = []

    for num in numbers:
        
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        #두개중 작은거 
        if len(max_heap) == len(min_heap):
            result.append(min(-max_heap[0], min_heap[0]))
        else:
            result.append(-max_heap[0])

    return result

if __name__ == "__main__":
    N = int(input())
    numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]

    result = find_middle_number(numbers)
    for num in result:
        print(num)
