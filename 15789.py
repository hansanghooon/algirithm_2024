import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappop,heappush


# 각 국가들의 동맹국들을 일종의 군집으로 만들어놓고 각 군집의 크기를 비교 해 동맹국의수(힘) 을 구함
def bfs(i):
    queue = deque()
    queue.append(i)
    check[i] = i
    cnt = 1
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if not check[next]:
                queue.append(next)
                check[next] = i
                cnt += 1
    return cnt

N, M = map(int, input().split())
graph = {i: [] for i in range(1,N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
check = {i:0 for i in range(1,N+1)}
count_set = []
C, H, K = map(int, input().split())
#각 동맹국들을 힘을 기준으로 heap에다가 넣어놓음, 넣을 떄 -1 을 곱해서 min heap을 max heap으로 이용
for i in range(1,N+1):
    if not check[i]:
        c = bfs(i)
        heappush(count_set,(-c,i))
        if check[C] == i:
            init_power = c

# 동맹 가능한 숫자만큼 heap에서 pop을 해 왕국이 가질 수 있는 힘을 계산함
power = init_power
while count_set and K > 0:
    cur_union_cnt, king = heappop(count_set)
    if check[king] != check[C] and check[king] != check[H]:
        power -= cur_union_cnt
        K -= 1
print(power)
