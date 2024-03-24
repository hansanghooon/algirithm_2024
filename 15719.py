import sys



def duplicate_number( numbers): 
    sum_numbers = 0
    temp = ""
    for num in numbers:
        if num.isdigit():
            temp += num
        elif num == " ":
            sum_numbers += int(temp)
            temp = ""
            
    sum_numbers += int(temp)
    
    return sum_numbers 

if __name__ == "__main__":
    N = int(input())
    numbers = sys.stdin.read()
    ans=dupl