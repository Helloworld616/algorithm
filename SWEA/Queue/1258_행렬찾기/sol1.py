import sys
sys.stdin = open('input.txt')


def get_info(matrix):
    info = []
    cnt = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                r = 0
                c = 0
                cnt += 1
                for k in range(j, N):
                    if matrix[i][k] != 0:
                        r += 1
                    else:
                        break
                for k in range(i, N):
                    if matrix[k][j] != 0:
                        c += 1
                    else:
                        break
                info.append([c, r, r * c])

                for k in range(c):
                    for l in range(r):
                        matrix[i + k][j + l] = 0

    return info, cnt


def partition(arr, start, end, idx):
    p = start

    for i in range(start, end):
        if arr[i][idx] < arr[end][idx] or (arr[i][idx] == arr[end][idx] and arr[i][idx-2] < arr[end][idx-2]):
            arr[i], arr[p] = arr[p], arr[i]
            p += 1

    arr[end], arr[p] = arr[p], arr[end]

    return p


def quick_sort(arr, start, end, idx):
    if end - start > 0:
        p = partition(arr, start, end, idx)
        quick_sort(arr, start, p-1, idx)
        quick_sort(arr, p+1, end, idx)


T = int(input())


for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    info, cnt = get_info(matrix)
    quick_sort(info, 0, len(info)-1, 2)

    print('#{} {}'.format(tc, cnt), end=' ')
    for i in range(len(info)):
        print('{} {}'.format(info[i][0], info[i][1]), end=' ')
    print()

