import sys
sys.stdin = open("sample_input.txt")


def fight(f, s, first, second):
    if first == second:
        return -1
    elif (first == 3 and second == 1) or (first == 1 and second == 3):
        if first > second:
            return f
        else:
            return s
    else:
        if first < second:
            return f
        else:
            return s

# main
T = int(input())

for tc in range(1, T+1):
    players = list(map(int, input().split()))
    groups = []
    winners = []
    indice = []

    for i in range(0, len(players), 4):
        groups.append(players[i:i+4])

    for group in groups:
        winner = []
        for i in range(len(group)-1):
            for j in range(i+1, len(group)):
                win = fight(i, j, group[i], group[j])
                if win == -1:
                    winner.append(i)
                else:
                    winner.append(win)
        winners.append(winner)

    print(winners)


    # print("#{} {}".format(tc, ))

