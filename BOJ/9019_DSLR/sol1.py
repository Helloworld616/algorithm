import sys
from collections import deque
sys.stdin = open('input.txt')


def D(num):
    return (2 * num) % 10000


def S(num):
    if num == 0:
        return 9999
    return num - 1


def L(num):
    string = str(num)
    if len(string) < 4:
        string += '0'
    else:
        string = string[1:] + string[0]
    return int(string)


def R(num):
    string = str(num)
    if len(string) == 1:
        string = string[0] + '000'
    elif len(string) == 2:
        string = string[1] + '00' + string[0]
    elif len(string) == 3:
        string = string[2] + '0' + string[0:2]
    else:
        string = string[3] + string[0:3]
    return int(string)


def bfs(A, B):
    queue = deque()
    queue.append((A, ''))
    visit = [False] * 10000

    while queue:
        number = queue.popleft()
        d = D(number[0])
        s = S(number[0])
        l = L(number[0])
        r = R(number[0])

        if d == B:
            return number[1] + 'D'
        elif not visit[d]:
            visit[d] = True
            queue.append((d, number[1] + 'D'))

        if s == B:
            return number[1] + 'S'
        elif not visit[s]:
            visit[s] = True
            queue.append((s, number[1] + 'S'))

        if l == B:
            return number[1] + 'L'
        elif not visit[l]:
            visit[l] = True
            queue.append((l, number[1] + 'L'))

        if r == B:
            return number[1] + 'R'
        elif not visit[r]:
            visit[r] = True
            queue.append((r, number[1] + 'R'))


# main
T = int(input())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(bfs(A, B))
