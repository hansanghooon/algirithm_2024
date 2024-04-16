import math
import heapq
def solution(coin, cards):
    answer=0
    win_number=len(cards)+1
    
    draw_deck=[0 for _ in range(len(cards)+2)]
    
    count_win_num=0
    
    deck_idx=(len(cards)//3)-1
    for k in range(len(cards)):
        
        number=cards[k]
        
        #k 의 짝 구하기
        partner= win_number-number
        
        partner_idx=cards.index(partner)
        
        if  k<=deck_idx and  partner_idx <=deck_idx:
            count_win_num=count_win_num+1
            
            # print('count_win_num')
            # print(k,number,partner,partner_idx)
            
        draw_deck[k]=partner_idx
        draw_deck[partner_idx]=k
        
    count_win_num=count_win_num//2
    

    # 도착할 수 있는 최종 라운드
    
    
    final_round=((len(cards)//3)+coin)//2+1
    
    # print(final_round,deck_idx,count_win_num)
    
    count_win_num=count_win_num+1
    count=0
    while count_win_num:
        answer=answer+1
        
        # if answer==final_round:
        #     return answer
        
        if len(cards)<(deck_idx+2):
            return answer
        a,b=draw_deck[deck_idx+1],draw_deck[deck_idx+2]
        # 카드를 미리 뽑지 않고, 현제값과 짝이 되는 값이 이전에 있었으면 그때 가서 coin을 2개 소모해서 둘 다 뽑음
        
        print(count_win_num)
        deck_idx=deck_idx+2  
        for i in [a,b]:
            
            if i<=deck_idx:
                # 짝이 이미 시작 덱에 있으면
                if i<=((len(cards)//3)-1):
                    if 0<coin:
                        coin=coin-1
                        count_win_num=count_win_num+1
                # 없으면 우선순위가 떨어지므로(coin을 2개 써야 하니까) count를 통해 따로 저장하고
                # 승리수가 모자라면 꺼내서 확인하는식
                
                else:
                    count=count+1
            
        count_win_num=count_win_num-1
        if count_win_num==0 and 1<coin and 1<=count:
            count=count-1
            coin=coin-2
            count_win_num=count_win_num+1
    

    
    return answer