import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())
    matrix = []
    for i in range(100):
        array = list(map(int, input().split()))
        matrix.append(array)

    totals = []
    for i in range(100):
        total = 0
        for j in range(100):
            total += matrix[i][j]
        totals.append(total)

    for j in range(100):
        total = 0
        for i in range(100):
            total += matrix[i][j]
        totals.append(total)

    total = 0
    for i in range(100):
        total += matrix[i][i]
    totals.append(total)

    for i in range(100):
        total = 0
        for j in range(99, -1, -1):
            total += matrix[i][j]
        totals.append(total)

    max_total = totals[0]
    for i in range(1, len(totals)):
        if totals[i] > max_total:
            max_total = totals[i]
    print("#{} {}".format(tc, max_total))
