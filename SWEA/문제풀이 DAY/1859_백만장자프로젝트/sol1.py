# 6번 테스트케이스 미통과, 시간초과
import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
     
    # 현재의 수보다 작은 수들의 갯수를 저장하는 counter 생성
    counter = [0] * N
    for i in range(1, N):
        for j in range(i):
            # 작은 수가 나올 경우 +1
            if price[j] < price[i]:
                counter[i] += 1
            # 큰 수가 나올 경우 다시 0으로 초기화
            else:
                counter[i] = 0
    print(counter)
    
    # counter에서 가장 큰 수 찾기
    max_cnt = 0
    for i in range(N):
        if counter[i] > max_cnt:
            max_cnt = counter[i]
            
    # 최대 이익 구하기
    profit = 0
    start = 0
    for i in range(N):
        # counter가 max_cnt와 같은 때 이익 계산
        if counter[i] == max_cnt:
            for j in range(start, i):
                # 현재의 가격이 과거의 가격보다 큰 경우에만 그 차이를 이익에 합산
                if price[i] > price[j]:
                    profit += price[i] - price[j]
            # 시작 지점을 i + 1로 변경
            start = i + 1
        # max_cnt가 현재부터 시작하는 범위의 counter 안에 없을 경우
        elif max_cnt not in set(counter[i:N]):
            # max_cnt 새로 구하기
            max_cnt = 0
            for j in range(i, N):
                if counter[j] > max_cnt:
                    max_cnt = counter[j]
            print(max_cnt, counter[i:N])

    print('#{} {}'.format(tc, profit))
