
# 정답 코드, deque를 사용해서 pop 을 이용해 메모리 사용이 더 적다. 
from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)





# 오류 코드, 로직은 동일하나 필요한 부분을 전부 리스트로 구현해 메모리 사용이 많아 메모리 초과가 떳다.
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self):

        self.visited = False
        #비어있나
        self.empty=False

graph=[]
n=0
m=0
day=1
check=1

#bfs visiting
def bfs_visiting(node_idx_list):
    global graph
    global day
    global check
    #최종적으로 도착하는 리스트가 없으면, 함수를 종료
    if len(node_idx_list)==0:
        return 

    #다음 으로 갈 노드 리스트들
    day_plus=0
    next_node_idx_list=[]

    
    for cord in node_idx_list:
        row=cord[0]
        col=cord[1]
        
        if graph[row][col].visited==True:
            continue
            
        

        
        check=check+1
        #ㅇ유지
        if graph[row][col].empty ==False and graph[row][col].visited==False:
            day_plus=1
            
            graph[row][col].visited=True

            # print("위치",row,col)
            next_row=[row+1,row-1]
            #조건 
            next_row_check= [[x,col] for x in next_row if 0 <= x < m]
            
            next_col=[col+1,col-1]
            next_col_check=[[row,x] for x in next_col if 0 <= x < n]

            for k in next_row_check:
                # print(k[0],k[1])
                next_node_idx_list.append([k[0],k[1]])
            for k in next_col_check:
                next_node_idx_list.append([k[0],k[1]])

            
                 
            
    # print("done")
    # print(len(next_node_idx_list))
    #리스트 안의 값들이 모두 비어있으면 값을 안더해줄거임
    day=day+day_plus
    bfs_visiting(next_node_idx_list)
    return 




n, m = map(int, sys.stdin.readline().split()) 

graph = [[Node() for _ in range(n)] for _ in range(m)  ]

start_idx=[]


day=-1
check=0

for i in range(m):

    line= list(map(int, sys.stdin.readline().split()))

    for j in range(len(line)):
        # print(j)
        if line[j]==-1:
            graph[i][j].empty=True
            graph[i][j].visited=True
        elif line[j]==1:
            start_idx.append([i,j])


bfs_visiting(start_idx)

# print("\n\n")
# print(check)
# print(day)

check=0
for i in range(n):
    for j in range(m):

        # print(graph[i][j].visited)
        if graph[j][i].visited==True:
            check=check+1
        
if check < n*m:
    
    print(-1)
else:
    print(day)
