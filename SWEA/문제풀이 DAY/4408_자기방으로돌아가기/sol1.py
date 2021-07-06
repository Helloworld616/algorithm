import sys
sys.stdin = open('sample_input.txt')


def solution(rooms, start, end):
    for sdx in range(len(start)):
        for i in range(200):
            if rooms[0][i] == start[sdx] or rooms[2][i] == start[sdx]:
                s_idx = i
            if rooms[0][i] == end[sdx] or rooms[2][i] == end[sdx]:
                e_idx = i

        if s_idx > e_idx:
            s_idx, e_idx = e_idx, s_idx

        for idx in range(s_idx, e_idx + 1):
            rooms[1][idx] += 1

    answer = rooms[1][0]
    for i in range(1, 200):
        if rooms[1][i] > answer:
            answer = rooms[1][i]

    return answer


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    start = []
    end = []
    for _ in range(N):
        key, value = map(int, input().split())
        start.append(key)
        end.append(value)

    rooms = []
    roomA = []
    roomB = []
    hallway = [0] * 200
    for i in range(1, 401):
        if i % 2:
            roomA.append(i)
        else:
            roomB.append(i)
    rooms.append(roomA)
    rooms.append(hallway)
    rooms.append(roomB)
    #print(rooms)

    print('#{} {}'.format(tc, solution(rooms, start, end)))


