# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())

for i in range(1, T+1):
    tc = int(input())
    cards = list(map(int, list(input())))
    counter = [0] * 10
    for card in cards:
        counter[card] += 1
    max_num = 0
    max_count = counter[0]
    for idx in range(1, len(counter)):
        if max_count <= counter[idx]:
            max_num = idx
            max_count = counter[idx]
    print('#{} {} {}'.format(i, max_num, max_count))
