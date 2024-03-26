import sys


def run_away(pro,sung,board):

    # 교수님에서 성규까지 좌표차이
    # 교수님에서 성규까지의 직선의 기울기 구하기 위함           

    block=0
        
    x_min,x_max = min(pro[0],sung[0]),max(pro[0],sung[0])
    y_min,y_max = min(pro[1],sung[1]),max(pro[1],sung[1])

    

    for y in range(y_min,y_max+1):
        for x in range(x_min,x_max+1):
            if board[y][x]==1:
                block+=1

    if block>=3 and (pro[0]-sung[0])**2 + (pro[1]-sung[1])**2 >=25:
        if pro[0]==sung[0] or pro[1]==sung[1]:
            return True
        else:
            if (pro[0]-sung[0])**2 + (pro[1]-sung[1])**2 >=25:
                return True
    else:
        return False

    # if (x_max-x_min)**2+(y_max-y_min)**2 <25:
    #     return False

    # #x y 체크
    # for x in range(x_min,x_max+1):
    #     for y in range(y_min,y_max+1):
    #         if board[x][y]==1:
    #             block=block+1

    # if block >=3:
    #     return True
    # else:
    #     return False




if __name__ == "__main__":

    cord=0
    # 성규, 교수님 좌표 저장할 숫자, 나머지 학생들 저장할 숫자 리스트 만듬
    sung=0
    pro=0
    board = []

    N = int(input())    


    y_cord=0
    for i in range(N):
        numbers = list(map(int, sys.stdin.readline().strip().split())) 

        x_cord=0
        #1=학생 5=교수님 2=성규
        for element in numbers:
            if element==5:
                pro=[x_cord,y_cord]
            elif element==2:
                sung=[x_cord,y_cord]
                

            x_cord=x_cord+1
        y_cord=y_cord+1
        board.append(numbers)


    res=run_away(pro,sung,board)
    print(int(res))
    