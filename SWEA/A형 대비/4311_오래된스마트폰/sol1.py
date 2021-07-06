# 시간초과

import sys
sys.stdin = open("sample_sample_input.txt")
from itertools import permutations


def cal(number, cnt):
    global ans

    if number == W:
        ans = cnt
        return

    for p in p_result:
        next_number = number
        str_p = str(p)

        for i in range(5):
            if op_list[i]:
                if i == 0:
                    next_number = int(str(number) + str_p)
                elif i == 1:
                    next_number = number + p
                elif i == 2:
                    next_number = number - p
                elif i == 3:
                    next_number = number * p
                elif i == 4 and p != 0:
                    next_number = number // p

                if 0 <= next_number <= 999 and not visited[next_number]:
                    visited[next_number] = True

                    if i == 0:
                        next_cnt = cnt + len(str_p)
                        if next_cnt < ans:
                            cal(next_number, next_cnt)
                        next_cnt -= cnt + len(str_p)
                    else:
                        if next_number == W:
                            next_cnt = cnt + len(str_p) + 2
                            if next_cnt < ans:
                                cal(next_number, next_cnt)
                            next_cnt -= cnt + len(str_p) + 2
                        else:
                            next_cnt = cnt + len(str_p) + 1
                            if next_cnt < ans:
                                cal(next_number, next_cnt)
                            next_cnt -= cnt + len(str_p) + 1

                    visited[next_number] = False


# main
T = int(input())

for tc in range(1, T+1):
    N, O, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    W = int(input())

    n_set = set(numbers)
    o_set = set(operators)
    ans = float('inf')

    if W in n_set:
        ans = 1
    elif W < 2 * min(numbers) and 2 not in o_set and 4 not in o_set:
        ans = -1
    elif 2 * max(numbers) < W and 1 not in o_set and 3 not in o_set:
        ans = -1
    else:
        n_change = list(map(str, numbers))
        perms = []
        for i in range(1, 4):
            perms += permutations(n_change, i)

        p_result = []
        for perm in perms:
            if 1 < len(perm) and perm[0] == '0':
                continue
            p_result.append(int(''.join(perm)))

        op_list = [True] + [False] * 4
        for operator in operators:
            op_list[operator] = True

        if W in p_result:
            ans = len(str(W))

        visited = [False] * 1000

        visited[0] = True
        for p in p_result:
            if p == W:
                ans = len(str(p))
            else:
                if p == 0:
                    continue
                visited[p] = True
                cal(p, len(str(p)))
                visited[p] = False

        if ans == float('inf'):
            ans = -1

    print("#{} {}".format(tc, ans))
