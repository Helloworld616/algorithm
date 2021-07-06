import sys
sys.stdin = open('sample_input.txt')


def Bubble_Sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    Bubble_Sort(arr)
    result = []
    first = len(arr)-1
    second = 0
    for _ in range(5):
        result.append(arr[first])
        result.append(arr[second])
        first -= 1
        second += 1

    print("#{}".format(tc), end = ' ')
    for i in range(len(result)):
        print(result[i], end = ' ')
    print()

