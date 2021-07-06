import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    profit = 0
    max_price = price[N-1]

    for i in range(len(price)-1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            profit += max_price - price[i]

    print('#{} {}'.format(tc, profit))
