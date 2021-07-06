def solution(priorities, location):
    answer = 0
    # 위치 이동을 저장할 리스트 생성
    spots = [i for i in range(len(priorities))]

    # priorities 안의 원소가 하나도 없을 때까지 반복문 실행
    while priorities:
        # 만약 맨 앞의 원소가 우선 순위가 가장 높으면
        if priorities[0] == max(priorities):
            # 원소와 원소의 위치 정보를 빼낸다.
            priorities.pop(0)
            spot = spots.pop(0)
            # 그리고 추출 횟수를 1 증가시킨다.
            answer += 1
            # 만약 나의 문서를 인쇄했다면 바로 정답 반환
            if spot == location:
                return answer
        # 우선순위가 다른 원소에게 밀린다면
        else:
            # 맨 뒤로 이동
            priorities.append(priorities.pop(0))
            spots.append(spots.pop(0))


priorities = [2, 1, 3, 2]
location = 2
# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
print(solution(priorities, location))