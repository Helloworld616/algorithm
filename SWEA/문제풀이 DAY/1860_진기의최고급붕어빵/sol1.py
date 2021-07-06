import sys
sys.stdin = open('input.txt')


def Bubble_Sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


def solution(client, M, K):
    fish = 0
    time = 0
    idx = 0

    while idx < len(client):
        if time > 0 and time % M == 0:
            fish += K

        while idx < len(client) and time == client[idx]:
            if fish < 1:
                return 'Impossible'
            else:
                fish -= 1
            idx += 1

        time += 1

    return 'Possible'


T = int(input())


for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    client = list(map(int, input().split()))
    Bubble_Sort(client)
    print('#{} {}'.format(tc, solution(client, M, K)))
