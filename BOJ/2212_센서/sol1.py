# 시간초과

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def Bubble_Sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# main
N = int(input())
K = int(input())
sensor = deque(set(list(map(int, input().split()))))

Bubble_Sort(sensor)

ans = 0
if K > len(sensor):
    print(ans)
else:
    while K-1:
        first = sensor.popleft()
        second = sensor.popleft()
        ans += second - first
        K -= 1
    ans += sensor[len(sensor)-1] - sensor[0]
    print(ans)
