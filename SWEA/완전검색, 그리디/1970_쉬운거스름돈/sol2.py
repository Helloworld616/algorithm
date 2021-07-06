import sys
sys.stdin = open('input.txt')

won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T+1):
    money = int(input())
    need = ['0'] * len(won)

    for i in range(len(won)):
        if won[i] <= money:
            need[i] = str(money // won[i])
            money %= won[i]

    print('#{}'.format(tc))
    print('{}'.format(' '.join(need)))
