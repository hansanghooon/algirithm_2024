import sys
input = sys.stdin.readline

R, C, W = map(int, input().strip().split())

dp = [[0] * 31 for _ in range(31)]
dp[0][0] = 1	# 맨 위 꼭짓점의 값
for i in range(1, 31):
    dp[i][0] = 1	# 왼쪽 가장자리 변들의 값을 모두 1로 설정
    dp[i][i] = 1	# 오른쪽 가장자리 변들의 값을 모두 1로 설정

for i in range(2, 31):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

Sum = 0
for w in range(W):  # 변의 길이
    for i in range(w+1):
        Sum += dp[w+R-1][i+C-1]
print(Sum)