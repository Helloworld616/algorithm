import sys
sys.stdin = open('sample_input.txt')


def binary_search(target, left, right, cnt):
    cnt += 1
    middle = (left + right) // 2

    if right - left <= 1:
        if target == middle:
            return cnt
        return 10000

    if target == middle:
        return cnt
    elif target < middle:
        return binary_search(target, left, middle, cnt)
    else:
        return binary_search(target, middle, right, cnt)


# main
T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    cnt = 0
    a = binary_search(A, 1, P, cnt)

    cnt = 0
    b = binary_search(B, 1, P, cnt)

    if a < b:
        print('#{} A'.format(tc))
    elif a > b:
        print('#{} B'.format(tc))
    else:
        print('#{} {}'.format(tc, 0))


