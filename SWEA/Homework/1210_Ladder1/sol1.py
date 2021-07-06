import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    ladders = []
    for i in range(100):
        ladder = list(map(int, input().split()))
        ladder.insert(0, 0)
        ladder.append(0)
        ladders.append(ladder)

    for idx in range(1, 101):
        row = 0
        col = idx
        if ladders[row][col] == 1:
            flag = True
            while flag:
                down = True
                if down:
                    while True:
                        row += 1
                        if row == 99:
                            if ladders[row][col] == 2:
                                answer = idx - 1
                            down = False
                            left = False
                            right = False
                            flag = False
                            break
                        if ladders[row][col - 1] != 0:
                            down = False
                            left = True
                            right = False
                            break
                        if ladders[row][col + 1] != 0:
                            down = False
                            left = False
                            right = True
                            break
                if left:
                    while True:
                        col -= 1
                        if ladders[row + 1][col] != 0:
                            down = True
                            left = False
                            right = False
                            break
                if right:
                    while True:
                        col += 1
                        if ladders[row + 1][col] != 0:
                            down = True
                            left = False
                            right = False
                            break
    print('#{} {}'.format(tc, answer))







