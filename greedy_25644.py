import sys

def find_max_profit(daily_price_list):


    lowest=daily_price_list[0]
    cuurent_max_profit=0

    for i in daily_price_list:

        if  i<=lowest:
            lowest=i
            continue
        
        if  cuurent_max_profit< i-lowest:
            cuurent_max_profit=i-lowest

    return cuurent_max_profit

if __name__ == "__main__":
    N = int(input())
    numbers = sys.stdin.readline().strip()
    numbers=list(map(int, numbers.split()))
    print(numbers)
    result = find_max_profit(numbers)
    print(result)