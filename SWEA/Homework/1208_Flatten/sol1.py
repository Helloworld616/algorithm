import sys
sys.stdin = open('input.txt')

for i in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    cnt = 0
    while cnt <= dump:
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
        if max_height - min_height <= 1:
            answer = max_height - min_height
            break
        else:
            answer = boxes[max_index] - boxes[min_index]
            boxes[max_index] -= 1
            boxes[min_index] += 1

        cnt +=1
    print('#{} {}'.format(i, answer))




