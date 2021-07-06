import sys
sys.stdin = open("sample_input.txt")


def binary_search(target, left, right):
    global to_left
    global to_right

    if left <= right:
        mid = (left + right) // 2

        if target == A[mid]:
            return 1

        elif target < A[mid]:
            if not to_left:
                to_left = True
                to_right = False
                return binary_search(target, left, mid-1)
            else:
                return 0
        else:
            if not to_right:
                to_left = False
                to_right = True
                return binary_search(target, mid+1, right)
            else:
                return 0

    return 0


# main
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    ans = 0
    for element in B:
        to_right = False
        to_left = False
        ans += binary_search(element, 0, len(A)-1)
    
    print("#{} {}".format(tc, ans))

