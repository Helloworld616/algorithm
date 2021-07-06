import sys
sys.stdin = open('input.txt')


def power(num, cnt):
    if cnt == 0:
        return 1
    return num * power(num, cnt-1)


# main
T = 10
for i in range(T):
    tc = int(input())
    num, cnt = map(int, input().split())
    print(f'#{tc} {power(num, cnt)}')
