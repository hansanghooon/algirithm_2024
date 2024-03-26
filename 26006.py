import sys

if __name__ == "__main__":

    N = list(map(int, sys.stdin.readline().strip().split())) 

    #nxn 체스판
    n=N[0]
    #퀸 개수
    num_queen=N[1]

    #킹 입력

    king=list(map(int, sys.stdin.readline().strip().split())) 

    king_x=king[1]
    king_y=king[0]
    
    # 구십도 회전시켜서 대각축을 x,y축처럼 맞춰서 생각
    king_diag_x=king_x+king_y
    king_diag_y=king_y-king_x

 



    #퀸 입력
    #퀸이 움직일수 있는 좌표를 파악
    queen_x=set()
    queen_y=set()
    #대각의 경우 왼쪽 위와 오른쪽 아래를 잇는걸 1 반대를 2로 저장
    
    #보드판 자체를 대각으로 회전시켜 x와 y축의 개념으로 생각할것임,
    queen_diag_x=set()
    queen_diag_y=set()

    for _ in range(num_queen):

        queen=list(map(int, sys.stdin.readline().strip().split())) 
        queen_x.add(queen[1])
        queen_y.add(queen[0])
        queen_diag_x.add(queen[1]+queen[0])
        queen_diag_y.add(queen[0]-queen[1])

    #킹이 움직일수 있는 위치
    king_x_next=[king_x]
    king_y_next=[king_y]
    king_diag_x_next=[]
    king_diag_y_next=[]

    # x값이 n을 넘어가거나 1보다 작아지는 오류     
    if (king_x+1) <= n:
        king_x_next.append(king_x+1)
        # diagonal 을 넣어주기 위해 y조건 검사
        if (king_y+1) <= n:
            king_diag_y_next.append(king_diag_y+1)

        if (king_y > 1):
            king_diag_x_next.append(king_diag_x+1)


    if  king_x >1:

        king_x_next.append(king_x-1)

        if (king_y+1) <= n:
            king_diag_x_next.append(king_diag_x-1)

        if (king_y > 1):
            king_diag_y_next.append(king_diag_y-1)

    if (king_y+1) <= n:
        king_y_next.append(king_y+1)

    if (king_y > 1):
        king_y_next.append(king_y-1)



    #check 상태 인지 체크
    if king_x in queen_x or king_y in queen_y or king_diag_x in queen_diag_x or king_diag_y in queen_diag_y:
        
        res='CHECKMATE'



        for a in king_x_next:
            # king의 움직인 상태에서의 x좌표가 queen 에 없고
            if a not in queen_x:
                #당시 y 좌표가  queen y 에도 없으면
                 for b in king_y_next:
                    if b not in queen_y:

                        #그리고 각 대각선이 queen의 대각선에도 없다면
                        for c in king_diag_x_next:
                            if c not in queen_diag_x:
                                #그리고 각 대각선이 queen의 대각선에도 없다면
                                for d in king_diag_y_next:
                                    if d not in queen_diag_y:

                                        res='CHECK'
                                        break

        #     if ((king_x_next[_] in queen_x ) or (king_y_next[_] in queen_y)) or ( (king_diag_x_next[_] in queen_diag_x ) or (king_diag_y_next[_]  in queen_diag_y) ):
        #         pass
        #     else:
        #         res='CHECK'

    #check 아닐 떄 스테일 메이트인지 체크    
    else:
        
        res='STALEMATE'

        for a in king_x_next:
            # king의 움직인 상태에서의 x좌표가 queen 에 없고
            if a not in queen_x:
                #당시 y 좌표가  queen y 에도 없으면
                 for b in king_y_next:
                    if b not in queen_y:
                        #그리고 각 대각선이 queen의 대각선에도 없다면
                        for c in king_diag_x_next:
                            if c not in queen_diag_x:
                                #그리고 각 대각선이 queen의 대각선에도 없다면
                                for d in king_diag_y_next:
                                    if d not in queen_diag_y:
                                        res='NONE'
                                        break


    print(res)      
            
        
            