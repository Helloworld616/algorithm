import sys
sys.stdin = open("input.txt")

from pprint import pprint

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    array = []
    edge1 = [-1] * 7
    edge2 = [-1] * 7

    array.append(edge1)
    for i in range(N):
        numbers = list(map(int, input().split()))
        numbers.insert(0, -1)
        numbers.append(-1)
        array.append(numbers)
    array.append(edge2)

    total = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            answer = 0
            for k in range(len(dx)):
                if array[i+dx[k]][j+dy[k]] >= 0:
                    plus = array[i+dx[k]][j+dy[k]] - array[i][j]
                    if plus < 0:
                        plus = 0 - plus
                    answer += plus
            total += answer

    print("#{} {}".format(tc, total))







