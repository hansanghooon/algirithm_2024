from itertools import permutations

n, hp = map(int, input().split())  

def time_memo(time, damage, damage_memo_lst):
    global limit
    idx = 0
    while idx < limit:
        if damage_memo_lst[idx] != 0:
            idx += 1
            continue
        damage_memo_lst[idx] = damage
        idx += time
    return damage_memo_lst

def time_cnt(damage_memo_lst, hp):
    cnt = 0
    for i in range(len(damage_memo_lst)):
        if hp <= 0:
            break
        hp -= damage_memo_lst[i]
        cnt += 1
    return cnt


total_time = 0
total_damage = 0
lst_t_d = []

for i in range(n):
    time, damage = map(int, input().split())
    total_time += time
    total_damage += damage
    lst_t_d.append((time, damage))


limit = total_time*((hp//total_damage)+1)
lst = list(permutations(lst_t_d, n))
result = 1e10

for i in range(len(lst)):
    damage_memo_lst = [0 for _ in range(total_time*((hp//total_damage)+1))]
    for t, d in lst[i]:
        damage_memo_lst = time_memo(t, d, damage_memo_lst)
    result = min(result, time_cnt(damage_memo_lst, hp))
    


print(result)