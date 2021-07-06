import sys


def check(awful, result, idx, cnt, N):
    if len(result) == 3:
        for combination in awful:
            chk = 0
            for number in result:
                if number in combination:
                    chk += 1
                    if chk == 2: return
        cnt[0] += 1
    else:
        for i in range(idx, N):
            result.append(i)
            check(awful, result, i+1, cnt, N)
            result.pop()



N, M = map(int, sys.stdin.readline().split())

awful = []

for i in range(M):
    combination = list(map(int, sys.stdin.readline().split()))
    awful.append(combination)

cnt = [0]
check(awful, [], 1, cnt, N+1)
print(cnt[0])
