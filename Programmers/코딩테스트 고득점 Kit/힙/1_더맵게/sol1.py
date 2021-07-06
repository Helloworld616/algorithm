# 실패


def heap_move(heap, idx):
    print(heap, idx)
    if idx <= len(heap) // 2 and (heap[idx] > heap[idx * 2] or heap[idx] > heap[idx * 2 + 1]):
        if heap[idx * 2] < heap[idx * 2 + 1]:
            heap[idx], heap[idx * 2] = heap[idx * 2], heap[idx]
            heap_move(heap, idx * 2)
        else:
            heap[idx], heap[idx * 2 + 1] = heap[idx * 2 + 1], heap[idx]
            heap_move(heap, idx * 2 + 1)


def solution(scoville, K):
    answer = 0
    scoville.sort()
    scoville.insert(0, 0)

    while scoville[1] < K:
        if len(scoville) >= 3:
            scoville.append(scoville.pop(1) + scoville.pop(1) * 2)
            heap_move(scoville, 1)
            print(scoville)
            answer += 1
        else:
            return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))