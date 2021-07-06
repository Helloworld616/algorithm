# Fail

import sys
from collections import deque
sys.stdin = open('sample_input.txt')


def babygin(player):
    sorted_player = sorted(player)
    print(sorted_player)
    diff = sorted_player[1] - sorted_player[0]
    is_babygin = False

    for i in range(2, len(sorted_player)):
        compare = sorted_player[i] - sorted_player[i-1]
        if (diff == 0 or diff == 1) and diff == compare:
            is_babygin = True
        if is_babygin:
            return True
        diff = compare

    return False


def fight(queue):
    cnt = 0
    player1 = []
    player2 = []
    while queue:
        if not cnt % 2:
            player1.append(queue.popleft())
            if len(player1) >= 3 and babygin(player1):
                return 1
        else:
            player2.append(queue.popleft())
            if len(player2) >= 3 and babygin(player2):
                return 2
        cnt += 1

    return 0


# main
T = int(input())

for tc in range(1, T+1):
    queue = deque(map(int, input().split()))
    print('#{} {}'.format(tc, fight(queue)))
