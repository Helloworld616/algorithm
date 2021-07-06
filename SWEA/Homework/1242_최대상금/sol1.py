# 시간초과

import sys
sys.stdin = open('input.txt')


def cal(price):
    result = 0
    inc = 1
    for i in range(len(price) - 1, -1, -1):
        result += price[i] * inc
        inc *= 10
    return result


def swap(price, cnt, ans):
    if cnt == chance:
        compare = cal(price)
        if compare > ans[0]:
            ans[0] = compare
    else:
        for i in range(len(price)-1):
            for j in range(i, len(price)):
                price[i], price[j] = price[j], price[i]
                swap(price, cnt+1, ans)
                price[i], price[j] = price[j], price[i]


# main
T = int(input())
for tc in range(1, T+1):
    price, chance = input().split()

    price = list(map(int, list(price)))
    chance = int(chance)

    ans = [0]
    swap(price, 0, ans)
    print(ans)