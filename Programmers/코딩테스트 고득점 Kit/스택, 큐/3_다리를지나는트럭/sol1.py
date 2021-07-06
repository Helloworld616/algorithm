# 개낚시문제... 순서 따윈 이 문제와 아무 상관 없다.


def solution(bridge_length, weight, truck_weights):
    answer = 0
    cross = []  # 다리를 건너는 트럭을 저장하는 리스트
    time = []   # 다리를 건너는 트럭의 이동 경과 시간을 저장하는 리스트

    # 트럭이 모두 다리를 건널 때까지 반복문 실행
    while truck_weights:
        # 다리가 다음 트럭을 견딜 수 있다면
        # 다음 트럭을 다리로 보낸다.
        if weight - sum(cross) >= truck_weights[0]:
            cross.append(truck_weights.pop(0))
            time.append(0)

        # 모든 트럭이 다리를 건넜다면 정답 반환
        # 마지막 트럭 순번에서 이후의 연산을 건너뛰고 바로 수학적으로 계산해서 반환한다.
        if len(truck_weights) == 0:
            return answer + bridge_length + 1

        # 시간 1초 경과
        answer += 1

        # 다리를 건너는 모든 트럭들의 이동 시간을 1초만큼 증가시킨다.
        for i in range(len(time)):
            time[i] += 1

        # 다리를 다 건넜을 경우
        # cross와 time에서 모두 뺴낸다.
        if time[0] == bridge_length:
            cross.pop(0)
            time.pop(0)


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))