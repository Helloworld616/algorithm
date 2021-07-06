import sys
sys.stdin = open('sample_input.txt')


def find_total(arr, row, record, total, result, N):
    if row == N:
        if len(result) == 0:
            result.append(total)
        else:
            result[0] = total
    else:
        for i in range(len(arr[row])):
            if i not in set(record):
                if len(result) == 0 or len(result) > 0 and total + arr[row][i] < result[0]:
                    total += arr[row][i]
                    record.append(i)
                    find_total(arr, row+1, record, total, result, N)
                    total -= arr[row][i]
                    record.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        row_num = list(map(int, input().split()))
        arr.append(row_num)

    result, record = [], []
    find_total(arr, 0, record, 0, result, N)

    print('#{} {}'.format(tc, result[0]))

