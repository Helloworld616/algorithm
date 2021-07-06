import sys
sys.stdin = open('input.txt')

for i in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    cnt = 0
    while cnt < dump:
        # 덤핑 전 최대, 최소값 구하기
        max_height = boxes[0]
        min_height = boxes[0]
        max_index = 0
        min_index = 0
        for idx in range(1, len(boxes)):
            if boxes[idx] > max_height:
                max_height = boxes[idx]
                max_index = idx
            if boxes[idx] < min_height:
                min_height = boxes[idx]
                min_index = idx

        # 덤핑
        boxes[max_index] -= 1
        boxes[min_index] += 1

        # 덤핑 후 최대, 최소값 구하기
        max_height = boxes[0]
        min_height = boxes[0]
        max_index = 0
        min_index = 0
        for idx in range(1, len(boxes)):
            if boxes[idx] > max_height:
                max_height = boxes[idx]
                max_index = idx
            if boxes[idx] < min_height:
                min_height = boxes[idx]
                min_index = idx

        # 최대, 최소값의 차이가 1 이하이면 루프 빠져나오기
        if max_height - min_height <= 1:
            answer = max_height - min_height
            break

        # 아닐 경우 answer에 차이 저장해두기
        else:
            answer = boxes[max_index] - boxes[min_index]
        cnt +=1
    print('#{} {}'.format(i, answer))




