# 이거 문제 설명이 왜 이런가 -_-;;; 설명이 거지 같아서 푸는 것보다 이해하는 시간이 더 걸린다.
# 이 문제가 왜 스택/큐에 있는지도 모르겠다.


def solution(prices):
    answer = []

    # prices의 원소를 하나씩 꺼내서 다음 인덱스에 위치한 원소들과 비교해본다!
    for i in range(len(prices)):
        # 가격이 떨어지지 않는 시간 0으로 초기화
        time = 0
        for j in range(i+1, len(prices)):
            # 비교할 때마다 시간이 1초 흐른다.
            time += 1
            # 만약 가격이 떨어졌다면 비교 중지
            if prices[i] > prices[j]:
                break
        # 정답 리스트에 time 추가
        answer.append(time)

    # 정답 반환
    return answer

