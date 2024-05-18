BLANK = -1 
#수열에 비어있는 부분을 마이너스 1로 처리

def dfs(count, N, S, X):
    if count == N:
        print(*S)
        exit()
    
    for i in X:
        if i in S:
            continue
        next_idx = S.index(BLANK)
        if next_idx + i + 1 >= N * 2:
            break
        if S[next_idx + i + 1] != BLANK:
            continue

        S[next_idx] = i
        S[next_idx + i + 1] = i
        dfs(count+1, N, S, X)
        S[next_idx] = BLANK
        S[next_idx + i + 1] = BLANK

def solve(N, X):
    S = [BLANK] * (N * 2)
    dfs(0, N, S, X)
    print(-1)

N = int(input())
X = sorted(list(map(int, input().split())))
solve(N, X)