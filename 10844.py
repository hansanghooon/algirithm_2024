

n=int(input())



#시작 array
ans_arr=[0,1,1,1,1,1,1,1,1,1]

tmp=[0 for i in range(10)]

for iter in range(n-1):

    for i in range(10):
        if i==0:
            tmp[i]=ans_arr[1]
        
        elif 0<i <9:
            tmp[i]=ans_arr[i-1]+ans_arr[i+1]

        tmp[9]=ans_arr[8]

    ans_arr,tmp=tmp,ans_arr


print(sum(ans_arr))

print(ans_arr)