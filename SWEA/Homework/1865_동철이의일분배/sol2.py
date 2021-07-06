import sys
sys.stdin = open('input - 복사본.txt')


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
        flag = True
        for i in range(N):
            if percent[row][i] == 1.0:
                flag = False
                result.append(percent[row][i])
                distribute(row + 1, result, record)
                result.pop()
        if flag:
            for i in range(N):
                if i not in set(record) and percent[row][i]:
                    record.append(i)
                    result.append(percent[row][i])
                    distribute(row+1, result, record)
                    record.pop()
                    result.pop()


# main
for tc in range(1, int(input())+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]

    record= []
    for i in range(N):
        for j in range(N):
            if percent[i][j] == 100:
                record.append(j)
            percent[i][j] = percent[i][j] / 100

    ans = 0
    distribute(0, [], record)
    print('#%d %.6f' % (tc, ans))
