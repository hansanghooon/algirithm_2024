import sys

input=sys.stdin.readline



n,m=map(int,input().strip().split())

# 이거 tmp 랑 ans가 바뀌어야됨 j번째는 고정인대 이전 결과에 가장 작은걸 넣어야지 거꾸로 했내ㅓ

ans_list=list(map(int,input().strip().split()))
for _ in range(n-1):
    tmp_list=list(map(int,input().strip().split()))
    
    for j in range(m):
        
        tmp_val=ans_list[j]
        ans_list[j]=9999999
        tmp_list[j]=tmp_list[j]+min(ans_list)
        
        ans_list[j]=tmp_val
    # print(ans_list)
    ans_list=tmp_list
    
print(min(ans_list))  