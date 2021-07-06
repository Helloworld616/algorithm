import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split())

circle = [i for i in range(1, N+1)]
idx = K-1
queue = deque()


while circle:
    queue.append(circle.pop(idx))
    if idx == len(circle):
            idx = 0
    for i in range(K-1):
        idx += 1
        if idx == len(circle):
            idx = 0
        
answer = '<'

while queue:
    if len(queue) == 1:
        answer += str(queue.popleft())
    else:
        answer += str(queue.popleft()) + ', '

answer += '>'
print(answer)
