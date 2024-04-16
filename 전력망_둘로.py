def solution(n, wires):
    tree = {i+1 : dict() for i in range(n)}
    t = {i+1 : False for i in range(n)}
    for i in wires:
        tree[i[0]][i[1]]=0
        tree[i[1]][i[0]]=0
        
    def dfs(start):
        t[start]=True #노드를 방문하면 true로
        k=0 #k는 start 노드에의해 새로 연결되는 노드의 수 
        for next in tree[start]: #node와 연결되는 모든 간선 호출
            if not t[next]: #연결되는 노드를 거치지 않았을때
                x=dfs(next)+1#dfs를 했으므로 노드 하나를 더 연결함
                k+=x#next 간선을 통해 연결된 노드를 더함
                #ex start 7,next 8,9는 각각 1을 return 해주므로 k=3,dfs(7)은 3을 return함 
                tree[start][next]=x
        return k
    dfs(1)
    ans = 101
    for node in tree:
        for key in tree[node]:
            ans = min(abs(n-tree[node][key]-tree[node][key]),ans)
    return ans