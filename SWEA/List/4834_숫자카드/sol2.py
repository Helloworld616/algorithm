T = int(input())

for tc in range(1, T+1):
    # N : 카드의 개수
    N = int(input())
    card = input()

    # count 배열 생성
    count = [0] * 10

    max_count = -1
    max_num = -1

    for i in card:
        count[int(i)] += 1

    # 카드 숫자 세기
    for i in card:
        count[int(i)] += 1
        if max_count < count[int(i)]:
            max_count = count[int(i)]

    # for i in range(len(count)):
    #     # 이 곳에 등호가 들어간 이유를 잘 생각해보자...
    #     if max_count <= count[i]:
    #         max_num = i
    #         max_count = count[i]

    for i in range(len(count) - 1, -1. -1):
        if max_count == count[i]:
            max_num = i
            break

    print("{} {} {}".format(tc, max_num, max_count))