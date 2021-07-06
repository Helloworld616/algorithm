import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def combination(player, record, result, start, idx):
    if len(record) == N//2:
        total1 = 0
        for i in range(len(record)-1):
            for j in range(i + 1, len(record)):
                total1 += player[record[i]][record[j]]

        remain = []
        for i in range(N):
            if i not in set(record):
                remain.append(i)

        total2 = 0
        for i in range(len(remain) - 1):
            for j in range(i + 1, len(remain)):
                total2 += player[remain[i]][remain[j]]

        result.append(abs(total2 - total1))

    else:
        for i in range(start, len(player[idx])):
            record.append(i)
            combination(player, record, result, i+1, idx+1)
            record.pop()


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
player = [[0]*(i+1) for i in range(N-1)]

for i in range(0, N-1):
    for j in range(i+1, N):
        player[i].append(matrix[i][j] + matrix[j][i])

result = []
combination(player, [0], result, 1, 0)
print(min(result))