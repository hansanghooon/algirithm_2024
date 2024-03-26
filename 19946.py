if __name__ == "__main__":
    N = int(input())
    k = 64
    while N % 2 == 0:
        N = N// 2
        k =k- 1
    print(k)