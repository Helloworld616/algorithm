# 갑자기 난이도가 확 뛰어서 당황했던 문제... 힙 큐를 두 개 써야한다는 아이디어를 떠올리기가 힘들었습니다.

import heapq


def solution(jobs):
    N = len(jobs)  # 전체 작업 갯수 (평균으로 나눌 때 필요)
    total = 0  # 전체 소요 시간
    start = 0  # 현재 작업 시작 시간

    heapq.heapify(jobs)  # jobs를 "시작 시간"을 기준으로 최소 힙으로 변환
    queue = []  # "소요 시간" 기준 최소 힙을 만들기 위한 전처리

    # jobs와 queue가 모두 없어질 때까지 작업 수행
    while jobs or queue:
        # 아직 작업이 존재하고, 그 작업의 시작 시간이 start 이하인 경우
        # 현재 작업이 끝난 후 바로 수행할 수 있으므로 jobs에서 빼내서 queue에 넣어준다.
        # 이 때 넣어주는 기준은 "소요 시간"이다!
        while jobs and jobs[0][0] <= start:
            job = heapq.heappop(jobs)
            heapq.heappush(queue, (job[1], job))

        # 위 단계에서 아무런 작업도 들어오지 않았을 경우
        # jobs의 가장 첫 번째 작업의 시작 시간을 start로 설정
        if not queue:
            start = jobs[0][0]
        # 위 단계에서 작업이 하나라도 들어왔을 경우
        # 큐에서 작업을 하나씩 빼내서 순차적으로 소요 시간과 시작 시간에 더해준다!
        else:
            job = heapq.heappop(queue)[1]
            total += start - job[0] + job[1]
            start += job[1]

    # 최종적으로 산출된 소요 시간을 작업 갯수로 나눈 몫을 반환 (소수점은 버리므로!)
    return total // N


print(solution([[0, 3], [1, 9], [2, 6]]))  # 9
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))  # 72
print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))  # 15