import sys
# sys.stdin = open('input - 복사본.txt')
sys.stdin = open('input.txt')


def distribute(row, record):
    global ans, result
    if row == N:
        if result > ans:
            ans = result
    else:
        for i in range(N):
            if i not in set(record) and percent[row][i]:
                result *= percent[row][i]
                if result > ans:
                    record.append(i)
                    distribute(row+1, record)
                    record.pop()
                result /= percent[row][i]


# main
for tc in range(1, int(input())+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            percent[i][j] = percent[i][j] / 100

    ans = 0
    result = 1
    distribute(0, [])
    print('#%d %.6f' % (tc, round(ans * 100, 6)))
