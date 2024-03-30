import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self):
        self.neighbor = []
        self.visited = False

n, m = map(int, sys.stdin.readline().split()) 


graph = [ Node() for _ in range(n)]


# visiting
def visiting(node):
    node.visited = True
    
    for neighbor_node_idx in node.neighbor:
        if graph[neighbor_node_idx].visited ==False:
            visiting(graph[neighbor_node_idx])


for i in range(m):
    a,b= map(int, sys.stdin.readline().split())
    a=a-1
    b=b-1
    #0부터 저장할거라 -1 해줌
    graph[a].neighbor.append(b)
    graph[b].neighbor.append(a)


ans = 0 # 연결 노드의 수

idx=0


for i in range(n):
    #방문 안했으면 if문
    if graph[i].visited ==False :
        visiting(graph[i])
        ans += 1 # dfs 한 번 끝날 때마다 count+1

print(ans)