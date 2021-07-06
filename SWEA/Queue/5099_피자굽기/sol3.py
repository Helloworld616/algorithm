# 라이브강의 해설
import sys
sys.stdin = open('sample_input.txt')


T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 화덕의 크기, M: 피자의 개수

    pizza = list(map(int, input().split())) # 피자 입력

    # 화덕 생성
    firepot = []

    for i in range(N):
        firepot.append((i+1, pizza[i]))

    # 피자를 N번부터 넣어야 함.
    next_pizza = N
    last_pizza = -1

    while len(firepot) > 1:
        num, cheese = firepot.pop(0)

        cheese //= 2
        #last_pizza = num
        # 치즈의 양이 남아있다면
        if cheese:
            firepot.append((num, cheese))
        else:
            if next_pizza < M:
                firepot.append((next_pizza+1, pizza[next_pizza]))
                next_pizza += 1

    print("#{} {}".format(tc, firepot[0][0]))

