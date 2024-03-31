import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self):
        self.neighbor = []
        self.visited = False

n, m,start = map(int, sys.stdin.readline().split()) 


graph = [ Node() for _ in range(n)]

ans_list=[0 for _ in range(n)]
ans_list[start-1]=1
cnt=1
# visiting
def visiting(node):
    global cnt
    cnt=cnt+1
    node.visited = True
    node.neighbor.sort()
    
    for neighbor_node_idx in node.neighbor:
        if graph[neighbor_node_idx].visited ==False:
            ans_list[neighbor_node_idx]=cnt    
            visiting(graph[neighbor_node_idx])

for i in range(m):
    a,b= map(int, sys.stdin.readline().split())
    a=a-1
    b=b-1
    #0부터 저장할거라 -1 해줌
    graph[a].neighbor.append(b)
    graph[b].neighbor.append(a)


visiting(graph[start-1])

for i in ans_list:
    print(i)
