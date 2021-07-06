import sys
sys.stdin = open('sample_input.txt')


# 트럭에 실을 수 있는 최대 화물 무게를 계산하는 함수
def load():
    # 최대 화물 무게를 0으로 초기화
    max_weight = 0

    # 역순으로 정렬된 container에서 화물을 하나씩 꺼낸다.
    for box in container:
        # 화물이 현재 트럭의 적재 용량보다 작을 경우
        if box <= trucks[0]:
            max_weight += box  # max_weight에 화물 무게를 더하고
            trucks.pop(0)  # 현재 트럭을 trucks에서 제거 (= 다음 트럭으로 넘어감)
        # 더 이상 화물을 실을 트럭이 없을 경우 산출된 최대 화물 무게 반환
        if len(trucks) == 0:
            return max_weight

    # 연산이 정상적으로 끝났을 경우 산출된 최대 화물 무게를 반환
    return max_weight


# main
T = int(input())

for tc in range(1, T+1):
    # 컨테이너와 트럭의 개수 입력 받기
    N, M = map(int, input().split())
    # 컨테이너와 트럭의 용량을 리스트로 입력받기
    container = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    # 컨테이너와 트럭의 용량을 역순으로 정렬
    container.sort(reverse=True)
    trucks.sort(reverse=True)

    # 트럭에 실을 수 있는 최대 화물 무게 출력
    print('#{} {}'.format(tc, load()))
