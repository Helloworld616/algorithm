# PASS
import heapq


def solution(scoville, K):
    answer = 0

    # 최소 힙 생성
    heap = []
    for spicy in scoville:
        heapq.heappush(heap, spicy)

    # 힙의 최소값이 K 이상이 될 때까지 반복문 실행
    while heap[0] < K:
        # 힙의 길이가 2 이상이어야 스코빌 지수 연산이 가능하다!
        # 스코빌 지수 연산 실행 후, 연산 횟수 1 증가
        if len(heap) >= 2:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
            answer += 1
        # 힙의 길이가 2보다 작으면 스코빌 지수 연산 불가
        # 불가능하다는 사실을 리턴
        else:
            return -1

    # 불가능하지 않으면 정답 리턴
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
