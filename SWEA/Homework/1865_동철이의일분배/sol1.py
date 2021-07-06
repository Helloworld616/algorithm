import sys
# sys.stdin = open('input - 복사본.txt')
sys.stdin = open('input.txt')


def cal(result):
    total = 1
    for number in result:
        total *= number
    return round(total * 100, 6)


def distribute(row, result, record):
    global ans
    if row == N:
        value = cal(result)
        if value > ans:
            ans = value
    else:
        for i in range(N):
            if i not in set(record) and percent[row][i]:
                result.append(percent[row][i])
                value = cal(result)
                if value > ans:
                    record.append(i)
                    distribute(row+1, result, record)
                    record.pop()
                result.pop()


# main
for tc in range(1, int(input())+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            percent[i][j] = percent[i][j] / 100

    # print(percent)
    ans = 0
    distribute(0, [], [])
    print('#%d %.6f' % (tc, ans))
