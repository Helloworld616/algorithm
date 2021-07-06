import sys
sys.stdin = open('input.txt')


def partition(arr, start, end):
    p = start

    for i in range(start, end):
        if arr[i] < arr[end]:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1

    arr[p], arr[end] = arr[end], arr[p]

    return p


def quick_sort(arr, start, end):
    if end - start > 0:
        p = partition(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)


# main
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, len(numbers)-1)
    print('#{} {}'.format(tc, ' '.join(list(map(str, numbers)))))
