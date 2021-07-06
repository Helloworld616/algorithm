import sys
sys.stdin = open('input.txt')
from collections import deque

for tc in range(1, 11):
    T = int(input())
    secret = deque(map(int, input().split()))
    delta = 1

    while True:
        if delta == 6:
            delta = 1
        if secret[0] - delta <= 0:
            secret.popleft()
            secret.append(0)
            break
        else:
            secret.append(secret.popleft() - delta)
            delta += 1

    print('#{} {}'.format(tc, ' '.join(map(str, secret))))