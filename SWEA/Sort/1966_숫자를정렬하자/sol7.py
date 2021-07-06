import sys
sys.stdin = open("input.txt")


def partition(arr, start, end):
    pivot = start

    for i in range(start, end):
        if arr[i] < arr[end]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            pivot += 1

    arr[pivot], arr[end] = arr[end], arr[pivot]

    return pivot


def quick_sort(arr, start, end):
    if end > start:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)


# main
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, len(numbers)-1)

    print("#{} {}".format(tc, ' '.join(list(map(str, numbers)))))

