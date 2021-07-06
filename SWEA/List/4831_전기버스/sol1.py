import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for i in range(1, T+1):
    K, N, M = map(int, input().split())
    stop = list(map(int, input().split()))
    road = []
    for idx in range(N+1):
        if idx in stop:
            road.append(1)
        else:
            road.append(0)
    move = K
    charge = 0
    for location in range(len(road)):
        if (location + move) >= len(road)-1:
           break
        else:
            if move != 0 and (1 in road[location+1:location+move+1]):
                move -= 1
            else:
                if road[location]:
                    move = K-1
                    charge += 1
                else:
                    charge = 0
                    break
    print('#{} {}'.format(i, charge))



