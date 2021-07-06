import sys
sys.stdin = open("input.txt")

from pprint import pprint

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    array = []
    for i in range(N):
        numbers = list(map(int, input().split()))
        array.append(numbers)

    total = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(N):
        for j in range(N):
            answer = 0
            for k in range(len(dx)):
                if i+dx[k] < 0 or i+dx[k] >= N or j+dy[k] < 0 or j+dy[k] >= N:
                    continue
                plus = array[i+dx[k]][j+dy[k]] - array[i][j]
                if plus < 0:
                    plus = 0 - plus
                answer += plus
            total += answer

    print("#{} {}".format(tc, total))