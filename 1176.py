import sys; input = sys.stdin.readline

def dfs(i, v):
    if v == (1 << N) - 1: # 모든 학생들이 섰다면 가능한 배열이므로 1 반환
        return 1
    if ~dp[i][v]: # 저장되어 있는 dp면 저장된 dp 반환
        return dp[i][v]

    # 아직 서지 않은 학생 중 키 차이가 K를 초과하는 학생을 찾아 dfs를 한다.
    dp[i][v] = 0
    for j in range(N):
        if not v & (1 << j) and abs(H[i] - H[j]) > K:
            dp[i][v] += dfs(j, v | (1 << j))
    return dp[i][v]

N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]

dp = [[-1] * (1 << N) for _ in range(N)]
result = 0
for i in range(N): # 처음 서는 학생은 1번 학생부터 N번 학생까지 차례대로 시도해본다.
    result += dfs(i, 1 << i)
print(result)