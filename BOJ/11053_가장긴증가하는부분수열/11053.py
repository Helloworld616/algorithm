import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
length = [0 for _ in range(n)]


for i in range(n):
    length[i] = 1
    for j in range(i):
        if sequence[j] < sequence[i] and length[i] < length[j] + 1:
            length[i] = length[j] + 1

print(max(length))