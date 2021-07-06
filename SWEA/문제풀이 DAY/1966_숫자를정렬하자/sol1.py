import sys
sys.stdin = open('input.txt')

def Bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    Bubble_sort(arr)
    print('#{}'.format(tc), end = ' ')
    for idx in range(len(arr)):
        if idx == len(arr)-1:
            print(arr[idx])
        else:
            print(arr[idx], end = ' ')


