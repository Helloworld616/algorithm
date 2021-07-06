import sys
sys.stdin = open('sample_input.txt')
from collections import deque


T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    pizza = deque()
    fire = deque()

    for i in range(M):
        pizza.append((numbers[i], i+1))

    for i in range(N):
        fire.append(pizza.popleft())

    while len(fire) > 1:
        melt = fire.popleft()
        if melt[0] == 0 and len(pizza) > 0:
            fire.insert(0, pizza.popleft())
        elif melt[0] != 0:
            fire.append((melt[0]//2, melt[1]))

    print('#{} {}'.format(tc, fire[0][1]))